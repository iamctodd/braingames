from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os
from datetime import datetime
import hashlib

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

# File storage
SCORES_FILE = 'scores.json'
USERS_FILE = 'users.json'

# ============================================================================
# USER MANAGEMENT
# ============================================================================

def load_users():
    """Load users from JSON file"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save users to JSON file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def hash_password(password):
    """Hash password for storage"""
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(email, password, display_name):
    """Create new user"""
    users = load_users()
    if email in users:
        return False, "Email already exists"
    
    users[email] = {
        'password': hash_password(password),
        'display_name': display_name,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'avatar': None
    }
    save_users(users)
    return True, "User created successfully"

def verify_user(email, password):
    """Verify user credentials"""
    users = load_users()
    if email not in users:
        return False, "User not found"
    
    if users[email]['password'] != hash_password(password):
        return False, "Incorrect password"
    
    return True, users[email]

def get_current_user():
    """Get current logged in user"""
    if 'user_id' in session:
        users = load_users()
        if session['user_id'] in users:
            return session['user_id'], users[session['user_id']]
    return None, None

# ============================================================================
# SCORE MANAGEMENT
# ============================================================================

def load_scores():
    """Load scores from JSON file"""
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_scores(scores):
    """Save scores to JSON file"""
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f, indent=2)

def add_score(user_id, game_type, score, difficulty='medium'):
    """Add a new score"""
    scores = load_scores()
    
    if user_id not in scores:
        scores[user_id] = {'memory': [], 'problem_solving': [], 'tbi_memory': []}
    
    scores[user_id][game_type].append({
        'score': score,
        'difficulty': difficulty,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    
    # Keep last 100 scores per game
    scores[user_id][game_type] = scores[user_id][game_type][-100:]
    save_scores(scores)

def get_best_score(user_id, game_type):
    """Get best score for a game"""
    scores = load_scores()
    if user_id not in scores or not scores[user_id][game_type]:
        return 0
    return max(s['score'] for s in scores[user_id][game_type])

def get_game_stats(user_id, game_type):
    """Get stats for a game"""
    scores = load_scores()
    if user_id not in scores:
        return {'best': 0, 'average': 0, 'total': 0}
    
    game_scores = scores[user_id][game_type]
    if not game_scores:
        return {'best': 0, 'average': 0, 'total': 0}
    
    return {
        'best': max(s['score'] for s in game_scores),
        'average': round(sum(s['score'] for s in game_scores) / len(game_scores)),
        'total': len(game_scores)
    }

def get_all_games_stats(user_id):
    """Get stats for all games"""
    return {
        'memory': get_game_stats(user_id, 'memory'),
        'problem_solving': get_game_stats(user_id, 'problem_solving'),
        'tbi_memory': get_game_stats(user_id, 'tbi_memory')
    }

def get_leaderboard(game_type, limit=10):
    """Get leaderboard for a game"""
    users = load_users()
    scores = load_scores()
    
    leaderboard = []
    for user_id, user_data in users.items():
        if user_id in scores and scores[user_id][game_type]:
            best = max(s['score'] for s in scores[user_id][game_type])
            total = len(scores[user_id][game_type])
            leaderboard.append({
                'user_id': user_id,
                'display_name': user_data['display_name'],
                'score': best,
                'games_played': total
            })
    
    # Sort by score descending
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    return leaderboard[:limit]

# ============================================================================
# ROUTES - AUTHENTICATION
# ============================================================================

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """User signup"""
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('password')
        display_name = data.get('display_name')
        
        success, message = create_user(email, password, display_name)
        return jsonify({'success': success, 'message': message})
    
    return render_template('auth/signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('password')
        
        success, result = verify_user(email, password)
        if success:
            session['user_id'] = email
            return jsonify({'success': True, 'message': 'Logged in successfully'})
        else:
            return jsonify({'success': False, 'message': result})
    
    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    """User logout"""
    session.clear()
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    """User profile page"""
    user_id, user_data = get_current_user()
    if not user_id:
        return redirect(url_for('login'))
    
    stats = get_all_games_stats(user_id)
    return render_template('profile.html', user=user_data, user_id=user_id, stats=stats)

# ============================================================================
# ROUTES - PAGES
# ============================================================================

@app.route('/')
def index():
    """Home page"""
    user_id, user_data = get_current_user()
    
    if user_id:
        stats = get_all_games_stats(user_id)
        total_games = stats['memory']['total'] + stats['problem_solving']['total'] + stats['tbi_memory']['total']
        
        return render_template('index.html',
            logged_in=True,
            user=user_data,
            memory_best=stats['memory']['best'],
            memory_total=stats['memory']['total'],
            problem_best=stats['problem_solving']['best'],
            problem_total=stats['problem_solving']['total'],
            tbi_best=stats['tbi_memory']['best'],
            tbi_total=stats['tbi_memory']['total'],
            total_games=total_games
        )
    else:
        return render_template('index.html', logged_in=False)

@app.route('/dashboard')
def dashboard():
    """Dashboard"""
    user_id, user_data = get_current_user()
    if not user_id:
        return redirect(url_for('login'))
    
    stats = get_all_games_stats(user_id)
    return render_template('dashboard.html', user=user_data, stats=stats)

@app.route('/history')
def history():
    """Score history"""
    user_id, user_data = get_current_user()
    if not user_id:
        return redirect(url_for('login'))
    
    scores = load_scores()
    all_scores = []
    
    if user_id in scores:
        for game_type, game_scores in scores[user_id].items():
            for score in game_scores:
                all_scores.append({
                    'game': game_type.replace('_', ' ').title(),
                    'game_type': game_type,
                    **score
                })
    
    all_scores.sort(key=lambda x: x['date'], reverse=True)
    return render_template('history.html', user=user_data, scores=all_scores)

@app.route('/leaderboards')
def leaderboards():
    """Global leaderboards"""
    user_id, user_data = get_current_user()
    
    memory_lb = get_leaderboard('memory', 10)
    problem_lb = get_leaderboard('problem_solving', 10)
    tbi_lb = get_leaderboard('tbi_memory', 10)
    
    return render_template('leaderboards.html', 
        user=user_data,
        memory_leaderboard=memory_lb,
        problem_leaderboard=problem_lb,
        tbi_leaderboard=tbi_lb
    )

# ============================================================================
# ROUTES - GAMES
# ============================================================================

@app.route('/games/memory')
def memory():
    """Memory game"""
    user_id, user_data = get_current_user()
    best_score = get_best_score(user_id, 'memory') if user_id else 0
    total_games = get_game_stats(user_id, 'memory')['total'] if user_id else 0
    return render_template('games/memory.html', user=user_data, best_score=best_score, total_games=total_games)

@app.route('/games/problem-solving')
def problem_solving():
    """Problem solving game"""
    user_id, user_data = get_current_user()
    best_score = get_best_score(user_id, 'problem_solving') if user_id else 0
    total_games = get_game_stats(user_id, 'problem_solving')['total'] if user_id else 0
    return render_template('games/problem_solving.html', user=user_data, best_score=best_score, total_games=total_games)

@app.route('/games/tbi-memory')
def tbi_memory():
    """TBI memory game"""
    user_id, user_data = get_current_user()
    best_score = get_best_score(user_id, 'tbi_memory') if user_id else 0
    total_games = get_game_stats(user_id, 'tbi_memory')['total'] if user_id else 0
    return render_template('games/tbi_memory.html', user=user_data, best_score=best_score, total_games=total_games)

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route('/api/save-score', methods=['POST'])
def save_score():
    """Save a game score"""
    user_id, user_data = get_current_user()
    if not user_id:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    data = request.json
    game_type = data.get('game_type')
    score = data.get('score')
    difficulty = data.get('difficulty', 'medium')
    
    add_score(user_id, game_type, score, difficulty)
    
    return jsonify({
        'success': True,
        'best_score': get_best_score(user_id, game_type),
        'message': 'Score saved!'
    })

@app.route('/api/current-user')
def current_user():
    """Get current user info"""
    user_id, user_data = get_current_user()
    if user_id:
        return jsonify({'user_id': user_id, 'user': user_data})
    return jsonify({'user_id': None, 'user': None})

if __name__ == '__main__':
    print("🧠 Brain Games - With User Accounts & Leaderboards")
    print("✓ http://127.0.0.1:5000/")
    app.run(debug=True)

# ============================================================================
# PASSWORD RESET ENDPOINT
# ============================================================================

@app.route('/forgot-password', methods=['GET'])
def forgot_password():
    """Forgot password page"""
    return render_template('auth/forgot_password.html')

@app.route('/api/reset-password', methods=['POST'])
def reset_password():
    """Reset user password"""
    data = request.json
    email = data.get('email')
    new_password = data.get('new_password')
    
    users = load_users()
    
    if email not in users:
        return jsonify({'success': False, 'message': 'Email not found'}), 404
    
    if len(new_password) < 6:
        return jsonify({'success': False, 'message': 'Password must be at least 6 characters'}), 400
    
    # Update password
    users[email]['password'] = hash_password(new_password)
    save_users(users)
    
    return jsonify({'success': True, 'message': 'Password reset successfully'})
