# Brain Games - Flask Route Handlers (Add to app.py)
# These are new routes to support the modernization features

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from functools import wraps
from datetime import datetime, timedelta
import os

# ============================================================================
# DECORATORS & HELPERS
# ============================================================================

def login_required(f):
    """Decorator to require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def get_firebase_user():
    """Get current user from session"""
    user_id = session.get('user_id')
    if user_id:
        from firebase_admin import firestore
        db = firestore.client()
        return db.collection('users').document(user_id).get().to_dict()
    return None

# ============================================================================
# PROFILE & SETTINGS ROUTES
# ============================================================================

@app.route('/profile')
@app.route('/profile/<user_id>')
def profile(user_id=None):
    """Display user profile"""
    if user_id is None:
        # Show current user's profile
        if 'user_id' not in session:
            return redirect(url_for('login'))
        user_id = session['user_id']
    
    from firebase_admin import firestore
    db = firestore.client()
    
    try:
        user_doc = db.collection('users').document(user_id).get()
        if not user_doc.exists:
            return render_template('404.html'), 404
        
        user = user_doc.to_dict()
        user['id'] = user_id
        
        # Get user's game statistics
        game_sessions = db.collection('game_sessions')\
            .where('userId', '==', user_id)\
            .order_by('timestamp', direction=firestore.Query.DESCENDING)\
            .limit(100)\
            .stream()
        
        sessions_list = [doc.to_dict() for doc in game_sessions]
        
        # Calculate stats
        stats = calculate_user_stats(sessions_list)
        
        # Check if it's the current user viewing
        is_owner = session.get('user_id') == user_id
        
        return render_template('profile.html',
                             user=user,
                             stats=stats,
                             sessions=sessions_list,
                             is_owner=is_owner)
    
    except Exception as e:
        print(f"Profile error: {e}")
        return render_template('500.html'), 500


@app.route('/settings')
@login_required
def settings():
    """User settings page"""
    user = get_firebase_user()
    return render_template('settings.html', user=user)


@app.route('/api/settings/update', methods=['POST'])
@login_required
def update_settings():
    """Update user settings"""
    data = request.get_json()
    user_id = session.get('user_id')
    
    from firebase_admin import firestore
    db = firestore.client()
    
    try:
        # Update preferences
        db.collection('users').document(user_id).update({
            'preferences.emailNotifications': data.get('emailNotifications', True),
            'preferences.pushNotifications': data.get('pushNotifications', False),
            'preferences.profileVisibility': data.get('profileVisibility', 'public'),
            'bio': data.get('bio', ''),
            'displayName': data.get('displayName', 'User')
        })
        
        return jsonify({'success': True, 'message': 'Settings updated'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ============================================================================
# LEADERBOARDS ROUTES
# ============================================================================

@app.route('/leaderboards')
def leaderboards():
    """Leaderboards page"""
    return render_template('leaderboards.html')


@app.route('/api/leaderboards/<game_type>')
def get_leaderboard(game_type):
    """Get leaderboard data for a game type"""
    timeframe = request.args.get('timeframe', 'alltime')
    
    from firebase_admin import firestore
    from datetime import datetime, timedelta
    
    db = firestore.client()
    
    try:
        # Build query
        query = db.collection('game_sessions')\
            .where('gameType', '==', game_type)\
            .order_by('score', direction=firestore.Query.DESCENDING)\
            .limit(100)
        
        # Apply timeframe filter
        if timeframe == 'week':
            since = datetime.utcnow() - timedelta(days=7)
            query = query.where('timestamp', '>=', since)
        elif timeframe == 'month':
            since = datetime.utcnow() - timedelta(days=30)
            query = query.where('timestamp', '>=', since)
        
        # Execute query
        results = []
        seen_users = set()
        rank = 1
        
        for doc in query.stream():
            session_data = doc.to_dict()
            user_id = session_data.get('userId')
            
            # Only include first score per user
            if user_id not in seen_users:
                seen_users.add(user_id)
                
                # Get user info
                user_doc = db.collection('users').document(user_id).get()
                user_data = user_doc.to_dict() if user_doc.exists else {}
                
                results.append({
                    'rank': rank,
                    'userId': user_id,
                    'displayName': user_data.get('displayName', 'Anonymous'),
                    'avatar': user_data.get('avatar'),
                    'score': session_data.get('score'),
                    'difficulty': session_data.get('difficulty'),
                    'timestamp': session_data.get('timestamp').isoformat() if session_data.get('timestamp') else None
                })
                
                rank += 1
                if len(results) >= 10:
                    break
        
        # Get current user's rank if logged in
        user_rank = None
        if session.get('user_id'):
            current_user_id = session.get('user_id')
            all_users = set()
            for doc in query.stream():
                user_id = doc.to_dict().get('userId')
                if user_id not in all_users:
                    all_users.add(user_id)
                    if user_id == current_user_id:
                        user_rank = len(all_users)
                        break
        
        return jsonify({
            'leaderboard': results,
            'userRank': user_rank,
            'gameType': game_type,
            'timeframe': timeframe
        })
    
    except Exception as e:
        print(f"Leaderboard error: {e}")
        return jsonify({'error': str(e)}), 400

# ============================================================================
# ANALYTICS & STATS ROUTES
# ============================================================================

@app.route('/analytics')
@login_required
def analytics():
    """User analytics page"""
    user_id = session.get('user_id')
    user = get_firebase_user()
    
    from firebase_admin import firestore
    db = firestore.client()
    
    try:
        # Get all sessions for this user
        sessions = db.collection('game_sessions')\
            .where('userId', '==', user_id)\
            .order_by('timestamp', direction=firestore.Query.DESCENDING)\
            .stream()
        
        sessions_list = [doc.to_dict() for doc in sessions]
        stats = calculate_user_stats(sessions_list)
        
        return render_template('analytics.html',
                             user=user,
                             stats=stats,
                             sessions=sessions_list)
    
    except Exception as e:
        print(f"Analytics error: {e}")
        return render_template('analytics.html', error=str(e))


@app.route('/api/analytics/<game_type>')
@login_required
def get_analytics_data(game_type):
    """Get analytics data for charts (JSON)"""
    user_id = session.get('user_id')
    
    from firebase_admin import firestore
    db = firestore.client()
    
    try:
        # Get sessions for this game type
        sessions = db.collection('game_sessions')\
            .where('userId', '==', user_id)\
            .where('gameType', '==', game_type)\
            .order_by('timestamp')\
            .stream()
        
        sessions_list = [doc.to_dict() for doc in sessions]
        
        # Prepare data for charts
        scores = [s.get('score', 0) for s in sessions_list]
        dates = [s.get('timestamp').strftime('%Y-%m-%d') if s.get('timestamp') else '' for s in sessions_list]
        
        # Calculate trends
        if len(scores) >= 2:
            improvement = ((scores[-1] - scores[0]) / scores[0] * 100) if scores[0] > 0 else 0
            average = sum(scores) / len(scores)
            best = max(scores)
            worst = min(scores)
        else:
            improvement = 0
            average = scores[0] if scores else 0
            best = scores[0] if scores else 0
            worst = scores[0] if scores else 0
        
        return jsonify({
            'scores': scores,
            'dates': dates,
            'stats': {
                'improvement': round(improvement, 1),
                'average': round(average, 0),
                'best': best,
                'worst': worst,
                'total_games': len(scores)
            }
        })
    
    except Exception as e:
        print(f"Analytics data error: {e}")
        return jsonify({'error': str(e)}), 400

# ============================================================================
# GAME SESSION LOGGING
# ============================================================================

@app.route('/api/game-session', methods=['POST'])
@login_required
def log_game_session():
    """Log a completed game session"""
    data = request.get_json()
    user_id = session.get('user_id')
    
    from firebase_admin import firestore
    db = firestore.client()
    
    try:
        # Save session
        session_ref = db.collection('game_sessions').document()
        session_ref.set({
            'userId': user_id,
            'gameType': data.get('gameType'),
            'score': data.get('score'),
            'difficulty': data.get('difficulty', 'medium'),
            'duration': data.get('duration', 0),
            'timestamp': firestore.server_timestamp(),
            'sequence': data.get('sequence', []),
            'moves': data.get('moves', [])
        })
        
        # Update user stats
        db.collection('users').document(user_id).update({
            'stats.totalGamesPlayed': firestore.Increment(1),
            'stats.totalMinutesPlayed': firestore.Increment(int(data.get('duration', 0) / 60))
        })
        
        # Check for badges (optional)
        check_badges(user_id)
        
        return jsonify({'success': True, 'sessionId': session_ref.id})
    
    except Exception as e:
        print(f"Session logging error: {e}")
        return jsonify({'error': str(e)}), 400

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def calculate_user_stats(sessions):
    """Calculate statistics from game sessions"""
    if not sessions:
        return {
            'totalGamesPlayed': 0,
            'totalMinutesPlayed': 0,
            'currentStreak': 0,
            'bestScore': 0,
            'averageScore': 0,
            'gameBreakdown': {}
        }
    
    total_games = len(sessions)
    total_minutes = sum(s.get('duration', 0) for s in sessions) // 60
    best_score = max((s.get('score', 0) for s in sessions), default=0)
    avg_score = sum(s.get('score', 0) for s in sessions) / total_games if total_games > 0 else 0
    
    # Game breakdown
    game_breakdown = {}
    for s in sessions:
        game_type = s.get('gameType', 'unknown')
        if game_type not in game_breakdown:
            game_breakdown[game_type] = 0
        game_breakdown[game_type] += 1
    
    # Calculate streak (simplified)
    streak = calculate_streak(sessions)
    
    return {
        'totalGamesPlayed': total_games,
        'totalMinutesPlayed': total_minutes,
        'currentStreak': streak,
        'bestScore': best_score,
        'averageScore': round(avg_score, 0),
        'gameBreakdown': game_breakdown
    }


def calculate_streak(sessions):
    """Calculate current day streak from sessions"""
    if not sessions:
        return 0
    
    sessions_sorted = sorted(
        sessions,
        key=lambda x: x.get('timestamp'),
        reverse=True
    )
    
    streak = 0
    current_date = datetime.utcnow().date()
    
    for session in sessions_sorted:
        session_date = session.get('timestamp')
        if not session_date:
            continue
        
        if isinstance(session_date, str):
            session_date = datetime.fromisoformat(session_date).date()
        else:
            session_date = session_date.date()
        
        if session_date == current_date:
            streak += 1
            current_date -= timedelta(days=1)
        elif session_date == current_date - timedelta(days=1):
            streak += 1
            current_date -= timedelta(days=1)
        else:
            break
    
    return streak


def check_badges(user_id):
    """Check and award badges to user"""
    from firebase_admin import firestore
    db = firestore.client()
    
    # This is a simplified version
    # In production, you'd have more complex badge logic
    
    try:
        # Get user stats
        user_doc = db.collection('users').document(user_id).get()
        if not user_doc.exists:
            return
        
        stats = user_doc.to_dict().get('stats', {})
        total_games = stats.get('totalGamesPlayed', 0)
        
        # Award badges based on milestones
        badges_to_award = []
        
        if total_games == 1:
            badges_to_award.append('first_game')
        if total_games == 10:
            badges_to_award.append('ten_games')
        if total_games == 50:
            badges_to_award.append('fifty_games')
        if total_games == 100:
            badges_to_award.append('hundred_games')
        
        # Add badges to user
        if badges_to_award:
            current_badges = user_doc.to_dict().get('badges', [])
            for badge in badges_to_award:
                if badge not in current_badges:
                    current_badges.append(badge)
            
            db.collection('users').document(user_id).update({
                'badges': current_badges
            })
    
    except Exception as e:
        print(f"Badge check error: {e}")


# ============================================================================
# DASHBOARD ENHANCEMENTS
# ============================================================================

@app.route('/dashboard')
@login_required
def dashboard():
    """Enhanced dashboard with stats"""
    user_id = session.get('user_id')
    user = get_firebase_user()
    
    from firebase_admin import firestore
    db = firestore.client()
    
    try:
        # Get recent sessions
        sessions = db.collection('game_sessions')\
            .where('userId', '==', user_id)\
            .order_by('timestamp', direction=firestore.Query.DESCENDING)\
            .limit(10)\
            .stream()
        
        recent_sessions = []
        for doc in sessions:
            session_data = doc.to_dict()
            session_data['id'] = doc.id
            recent_sessions.append(session_data)
        
        stats = calculate_user_stats(recent_sessions)
        
        return render_template('dashboard.html',
                             user=user,
                             stats=stats,
                             recentSessions=recent_sessions)
    
    except Exception as e:
        print(f"Dashboard error: {e}")
        return render_template('dashboard.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
