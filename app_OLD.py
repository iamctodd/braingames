# ============================================================================
# BRAIN GAMES APP - SIMPLIFIED VERSION (Works without Firebase setup)
# ============================================================================

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from functools import wraps
from datetime import datetime, timedelta
import os
import copy

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Demo data storage (in production, use Firebase)
DEMO_USERS = {
    'test_user': {
        'email': 'test@example.com',
        'displayName': 'Test User',
        'avatar': None,
        'bio': 'This is a demo user',
        'stats': {
            'totalGamesPlayed': 0,
            'totalMinutesPlayed': 0,
            'currentStreak': 0
        },
        'preferences': {
            'emailNotifications': True,
            'pushNotifications': False,
            'profileVisibility': 'public'
        }
    }
}

DEMO_SESSIONS = []

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
    if not user_id:
        return None
    
    # Return from demo data
    if user_id in DEMO_USERS:
        user_data = copy.deepcopy(DEMO_USERS[user_id])
        user_data['id'] = user_id
        return user_data
    
    return None


def get_safe_user(user_id):
    """Get user safely with deep copy"""
    if user_id in DEMO_USERS:
        user_data = copy.deepcopy(DEMO_USERS[user_id])
        user_data['id'] = user_id
        return user_data
    return None


# ============================================================================
# AUTHENTICATION ROUTES
# ============================================================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        
        if email and password:
            # Demo mode: create user in demo data
            user_id = email.replace('@', '_').replace('.', '_')
            
            if user_id not in DEMO_USERS:
                DEMO_USERS[user_id] = {
                    'email': email,
                    'displayName': email.split('@')[0],
                    'avatar': None,
                    'bio': '',
                    'stats': {
                        'totalGamesPlayed': 0,
                        'totalMinutesPlayed': 0,
                        'currentStreak': 0
                    },
                    'preferences': {
                        'emailNotifications': True,
                        'pushNotifications': False,
                        'profileVisibility': 'public'
                    }
                }
            
            session['user_id'] = user_id
            session['email'] = email
            return redirect(url_for('dashboard'))
        
        return render_template('login.html', error='Please enter email and password')
    
    return render_template('login.html')


@app.route('/signin')
def signin():
    """Redirect to login"""
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    return redirect(url_for('index'))


# ============================================================================
# MAIN ROUTES
# ============================================================================

@app.route('/')
def index():
    """Home/Landing page"""
    return render_template('index.html')


@app.route('/dashboard')
@login_required
def dashboard():
    """Enhanced dashboard with stats"""
    user_id = session.get('user_id')
    user = get_firebase_user()
    
    if not user:
        return redirect(url_for('login'))
    
    # Get recent sessions for this user
    user_sessions = [s for s in DEMO_SESSIONS if s.get('userId') == user_id]
    recent_sessions = user_sessions[-10:] if user_sessions else []
    
    stats = calculate_user_stats(recent_sessions)
    
    return render_template('dashboard.html',
                         user=user,
                         stats=stats,
                         recentSessions=recent_sessions)


# ============================================================================
# GAME ROUTES
# ============================================================================

@app.route('/games/memory')
def memory_game():
    """Memory Training Game"""
    user = None
    if 'user_id' in session:
        user = get_firebase_user()
    return render_template('games/memory.html', user=user)


@app.route('/games/problem-solving')
def problem_solving_game():
    """Problem Solving Game"""
    user = None
    if 'user_id' in session:
        user = get_firebase_user()
    return render_template('games/problem_solving.html', user=user)


@app.route('/games/tbi-memory')
def tbi_memory_game():
    """TBI Memory Game"""
    user = None
    if 'user_id' in session:
        user = get_firebase_user()
    return render_template('games/tbi_memory.html', user=user)


# ============================================================================
# PROFILE ROUTES
# ============================================================================

@app.route('/profile')
@app.route('/profile/<user_id>')
def profile(user_id=None):
    """Display user profile"""
    # If no user_id provided, show current user's profile
    if user_id is None:
        if 'user_id' not in session:
            return redirect(url_for('login'))
        user_id = session['user_id']
    
    # Check if user exists
    if user_id not in DEMO_USERS:
        print(f"DEBUG: User {user_id} not found in DEMO_USERS")
        print(f"DEBUG: Available users: {list(DEMO_USERS.keys())}")
        return render_template('404.html'), 404
    
    try:
        # Get safe copy of user
        user = get_safe_user(user_id)
        
        if not user:
            return render_template('404.html'), 404
        
        # Get user's game sessions
        user_sessions = [s for s in DEMO_SESSIONS if s.get('userId') == user_id]
        
        stats = calculate_user_stats(user_sessions)
        
        # Check if it's the current user viewing
        is_owner = session.get('user_id') == user_id
        
        return render_template('profile.html',
                             user=user,
                             stats=stats,
                             sessions=user_sessions,
                             is_owner=is_owner)
    
    except Exception as e:
        print(f"Profile error: {e}")
        import traceback
        traceback.print_exc()
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
    
    try:
        # Update demo user
        if user_id in DEMO_USERS:
            user_data = DEMO_USERS[user_id]
            
            # Update fields
            user_data['displayName'] = data.get('displayName', user_data.get('displayName', 'User'))
            user_data['bio'] = data.get('bio', user_data.get('bio', ''))
            user_data['theme'] = data.get('theme', 'light')
            
            # Update preferences
            user_data['preferences'] = {
                'emailNotifications': data.get('emailNotifications', True),
                'pushNotifications': data.get('pushNotifications', False),
                'profileVisibility': data.get('profileVisibility', 'public')
            }
            
            # Handle avatar - store as base64 data URL
            if data.get('avatar'):
                user_data['avatar'] = data.get('avatar')
        
        return jsonify({'success': True, 'message': 'Settings updated'})
    
    except Exception as e:
        print(f"Settings error: {e}")
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
    
    try:
        # Filter sessions by game type
        filtered_sessions = [s for s in DEMO_SESSIONS if s.get('gameType') == game_type]
        
        # Sort by score descending
        filtered_sessions.sort(key=lambda x: x.get('score', 0), reverse=True)
        
        # Group by user and get top score
        results = []
        seen_users = set()
        rank = 1
        
        for session_data in filtered_sessions:
            user_id = session_data.get('userId')
            
            if user_id not in seen_users:
                seen_users.add(user_id)
                
                user_data = get_safe_user(user_id)
                if not user_data:
                    user_data = {'displayName': 'Unknown User', 'avatar': None}
                
                results.append({
                    'rank': rank,
                    'userId': user_id,
                    'displayName': user_data.get('displayName', 'Anonymous'),
                    'avatar': user_data.get('avatar'),
                    'score': session_data.get('score'),
                    'difficulty': session_data.get('difficulty', 'medium'),
                    'timestamp': session_data.get('timestamp')
                })
                
                rank += 1
                if len(results) >= 10:
                    break
        
        # Get current user's rank
        user_rank = None
        if session.get('user_id'):
            current_user_id = session.get('user_id')
            for entry in results:
                if entry['userId'] == current_user_id:
                    user_rank = entry['rank']
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
    
    try:
        # Get user's sessions
        user_sessions = [s for s in DEMO_SESSIONS if s.get('userId') == user_id]
        
        stats = calculate_user_stats(user_sessions)
        
        return render_template('analytics.html',
                             user=user,
                             stats=stats,
                             sessions=user_sessions)
    
    except Exception as e:
        print(f"Analytics error: {e}")
        return render_template('analytics.html', error=str(e))


@app.route('/api/analytics/<game_type>')
@login_required
def get_analytics_data(game_type):
    """Get analytics data for charts (JSON)"""
    user_id = session.get('user_id')
    
    try:
        # Get sessions for this game type
        user_sessions = [s for s in DEMO_SESSIONS 
                        if s.get('userId') == user_id and s.get('gameType') == game_type]
        
        # Sort by timestamp
        user_sessions.sort(key=lambda x: x.get('timestamp', ''))
        
        # Prepare data for charts
        scores = [s.get('score', 0) for s in user_sessions]
        dates = [s.get('timestamp', '')[:10] for s in user_sessions]
        
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
    
    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        # Create demo session
        session_data = {
            'userId': user_id,
            'gameType': data.get('gameType'),
            'score': data.get('score'),
            'difficulty': data.get('difficulty', 'medium'),
            'duration': data.get('duration', 0),
            'timestamp': datetime.utcnow().isoformat(),
            'sequence': data.get('sequence', []),
            'moves': data.get('moves', [])
        }
        
        DEMO_SESSIONS.append(session_data)
        
        # Update user stats
        if user_id in DEMO_USERS:
            user = DEMO_USERS[user_id]
            user['stats']['totalGamesPlayed'] += 1
            user['stats']['totalMinutesPlayed'] += int(data.get('duration', 0) / 60)
        
        return jsonify({'success': True, 'sessionId': len(DEMO_SESSIONS) - 1})
    
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
        key=lambda x: x.get('timestamp', ''),
        reverse=True
    )
    
    streak = 0
    current_date = datetime.utcnow().date()
    
    for session in sessions_sorted:
        session_date = session.get('timestamp', '')
        if not session_date:
            continue
        
        try:
            if isinstance(session_date, str):
                session_date = datetime.fromisoformat(session_date[:10]).date()
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
        except:
            break
    
    return streak


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("🧠 Brain Games App Starting...")
    print("✓ Running in DEMO MODE (no Firebase required)")
    print("✓ Login with any email/password")
    print("✓ All data stored in memory (resets on restart)")
    app.run(debug=True)