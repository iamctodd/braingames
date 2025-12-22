from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os
from datetime import datetime, timedelta
import hashlib
import secrets

app = Flask(__name__)
app.secret_key = 'brain-games-secret-key-2025'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

USERS_FILE = 'users.json'
SCORES_FILE = 'scores.json'
RESET_TOKENS_FILE = 'reset_tokens.json'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Initialize default users
def init_default_users():
    default_users = {
        "demo@braingames.com": {
            "password": hash_password("demo123"),
            "display_name": "Demo User",
            "created_at": "2025-12-16 12:00:00",
            "avatar": None
        },
        "email@ctoddlombardo.com": {
            "password": hash_password("123456"),
            "display_name": "C TODD LOMBARDO",
            "created_at": "2025-12-17 18:25:23",
            "avatar": None
        }
    }
    
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as f:
                users = json.load(f)
            # Merge default users into existing file
            for email, data in default_users.items():
                if email not in users:
                    users[email] = data
            with open(USERS_FILE, 'w') as f:
                json.dump(users, f, indent=2)
        except:
            with open(USERS_FILE, 'w') as f:
                json.dump(default_users, f, indent=2)
    else:
        with open(USERS_FILE, 'w') as f:
            json.dump(default_users, f, indent=2)

init_default_users()

# ============================================================================
# USER FUNCTIONS
# ============================================================================

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_users(users):
    try:
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f, indent=2)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save users: {e}")
        return False

def create_user(email, password, display_name):
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
    return True, "Account created"

def verify_user(email, password):
    users = load_users()
    if email not in users:
        return False, "User not found"
    if users[email]['password'] != hash_password(password):
        return False, "Wrong password"
    return True, users[email]

def get_current_user():
    if 'user_id' in session:
        users = load_users()
        if session['user_id'] in users:
            return session['user_id'], users[session['user_id']]
    return None, None

# ============================================================================
# PASSWORD RESET FUNCTIONS
# ============================================================================

def load_reset_tokens():
    if os.path.exists(RESET_TOKENS_FILE):
        try:
            with open(RESET_TOKENS_FILE, 'r') as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
                return {}
        except Exception as e:
            print(f"[ERROR] Failed to load reset tokens: {e}")
            return {}
    return {}

def save_reset_tokens(tokens):
    try:
        with open(RESET_TOKENS_FILE, 'w') as f:
            json.dump(tokens, f, indent=2)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save reset tokens: {e}")
        return False

def create_reset_token(email):
    """Create a password reset token for a user"""
    users = load_users()
    if email not in users:
        return None
    
    token = secrets.token_urlsafe(32)
    tokens = load_reset_tokens()
    
    tokens[token] = {
        'email': email,
        'created_at': datetime.now().isoformat(),
        'expires_at': (datetime.now() + timedelta(hours=24)).isoformat()
    }
    save_reset_tokens(tokens)
    return token

def verify_reset_token(token):
    """Verify a password reset token and return email if valid"""
    tokens = load_reset_tokens()
    if token not in tokens:
        return None
    
    token_data = tokens[token]
    try:
        expires_at = datetime.fromisoformat(token_data['expires_at'])
    except:
        return None
    
    if datetime.now() > expires_at:
        # Token expired, delete it
        del tokens[token]
        save_reset_tokens(tokens)
        return None
    
    return token_data['email']

def reset_password(token, new_password):
    """Reset password using a valid token"""
    email = verify_reset_token(token)
    if not email:
        return False, "Invalid or expired token"
    
    users = load_users()
    users[email]['password'] = hash_password(new_password)
    save_users(users)
    
    # Delete the token
    tokens = load_reset_tokens()
    if token in tokens:
        del tokens[token]
        save_reset_tokens(tokens)
    
    return True, "Password reset successful"

# ============================================================================
# SCORE FUNCTIONS
# ============================================================================

def load_scores():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_scores(scores):
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f, indent=2)

def add_score(user_id, game_type, score, difficulty='medium'):
    scores = load_scores()
    if user_id not in scores:
        scores[user_id] = {'memory': [], 'problem_solving': [], 'tbi_memory': []}
    scores[user_id][game_type].append({
        'score': score,
        'difficulty': difficulty,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    scores[user_id][game_type] = scores[user_id][game_type][-100:]
    save_scores(scores)

def get_best_score(user_id, game_type):
    scores = load_scores()
    if user_id not in scores or not scores[user_id][game_type]:
        return 0
    return max(s['score'] for s in scores[user_id][game_type])

def get_game_stats(user_id, game_type):
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
    return {
        'memory': get_game_stats(user_id, 'memory'),
        'problem_solving': get_game_stats(user_id, 'problem_solving'),
        'tbi_memory': get_game_stats(user_id, 'tbi_memory')
    }

def get_leaderboard(game_type, limit=10):
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
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    return leaderboard[:limit]

# ============================================================================
# ROUTES
# ============================================================================

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        display_name = request.form.get('display_name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        
        if not display_name or len(display_name) < 2:
            return render_template('auth/signup.html', error='Display name must be at least 2 characters')
        
        if not email or len(email) < 5:
            return render_template('auth/signup.html', error='Email must be at least 5 characters')
        
        if not password or len(password) < 5:
            return render_template('auth/signup.html', error='Password must be at least 5 characters')
        
        success, msg = create_user(email, password, display_name)
        if success:
            session.permanent = True
            session['user_id'] = email
            return redirect(url_for('index'))
        return render_template('auth/signup.html', error=msg)
    
    return render_template('auth/signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        
        success, result = verify_user(email, password)
        if success:
            session.permanent = True
            session['user_id'] = email
            return redirect(url_for('index'))
        
        return render_template('auth/login.html', error='Invalid email or password')
    
    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        
        token = create_reset_token(email)
        if token:
            # TODO: Send email with reset link
            # For now, just show the reset link
            reset_link = url_for('reset_password_route', token=token, _external=True)
            return render_template('auth/forgot_password.html', 
                message=f'Password reset link: {reset_link}')
        
        return render_template('auth/forgot_password.html',
            message='If an account exists with that email, you will receive a password reset link.')
    
    return render_template('auth/forgot_password.html')

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password_route(token):
    email = verify_reset_token(token)
    if not email:
        return render_template('auth/reset_password.html', error='Invalid or expired reset link'), 400
    
    if request.method == 'POST':
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        if len(password) < 5:
            return render_template('auth/reset_password.html', 
                error='Password must be at least 5 characters', token=token)
        
        if password != confirm_password:
            return render_template('auth/reset_password.html',
                error='Passwords do not match', token=token)
        
        success, msg = reset_password(token, password)
        if success:
            return redirect(url_for('login'))
        return render_template('auth/reset_password.html', error=msg, token=token)
    
    return render_template('auth/reset_password.html', token=token)

@app.route('/')
def index():
    user_id, user_data = get_current_user()
    if user_id:
        stats = get_all_games_stats(user_id)
        total = stats['memory']['total'] + stats['problem_solving']['total'] + stats['tbi_memory']['total']
        return render_template('index.html', logged_in=True, user=user_data, total_games=total,
            memory_best=stats['memory']['best'], memory_total=stats['memory']['total'],
            problem_best=stats['problem_solving']['best'], problem_total=stats['problem_solving']['total'],
            tbi_best=stats['tbi_memory']['best'], tbi_total=stats['tbi_memory']['total'])
    return render_template('index.html', logged_in=False)

@app.route('/dashboard')
def dashboard():
    user_id, user_data = get_current_user()
    if not user_id:
        return redirect(url_for('login'))
    stats = get_all_games_stats(user_id)
    return render_template('dashboard.html', user=user_data, stats=stats)

@app.route('/history')
def history():
    user_id, user_data = get_current_user()
    if not user_id:
        return redirect(url_for('login'))
    scores = load_scores()
    all_scores = []
    if user_id in scores:
        for game_type, game_scores in scores[user_id].items():
            for score in game_scores:
                all_scores.append({'game': game_type.replace('_', ' ').title(), 'game_type': game_type, **score})
    all_scores.sort(key=lambda x: x['date'], reverse=True)
    return render_template('history.html', user=user_data, scores=all_scores)

@app.route('/profile')
def profile():
    user_id, user_data = get_current_user()
    if not user_id:
        return redirect(url_for('login'))
    stats = get_all_games_stats(user_id)
    return render_template('profile.html', user=user_data, user_id=user_id, stats=stats)

@app.route('/leaderboards')
def leaderboards():
    user_id, user_data = get_current_user()
    memory_lb = get_leaderboard('memory', 10)
    problem_lb = get_leaderboard('problem_solving', 10)
    tbi_lb = get_leaderboard('tbi_memory', 10)
    return render_template('leaderboards.html', user=user_data, memory_leaderboard=memory_lb, problem_leaderboard=problem_lb, tbi_leaderboard=tbi_lb)

@app.route('/games/memory')
def memory():
    user_id, user_data = get_current_user()
    best_score = get_best_score(user_id, 'memory') if user_id else 0
    total_games = get_game_stats(user_id, 'memory')['total'] if user_id else 0
    return render_template('games/memory.html', user=user_data, best_score=best_score, total_games=total_games)

@app.route('/games/problem-solving')
def problem_solving():
    user_id, user_data = get_current_user()
    best_score = get_best_score(user_id, 'problem_solving') if user_id else 0
    total_games = get_game_stats(user_id, 'problem_solving')['total'] if user_id else 0
    return render_template('games/problem_solving.html', user=user_data, best_score=best_score, total_games=total_games)

@app.route('/games/tbi-memory')
def tbi_memory():
    user_id, user_data = get_current_user()
    best_score = get_best_score(user_id, 'tbi_memory') if user_id else 0
    total_games = get_game_stats(user_id, 'tbi_memory')['total'] if user_id else 0
    return render_template('games/tbi_memory.html', user=user_data, best_score=best_score, total_games=total_games)

@app.route('/api/save-score', methods=['POST'])
def save_score():
    user_id, user_data = get_current_user()
    if not user_id:
        return jsonify({'success': False}), 401
    data = request.json
    add_score(user_id, data.get('game_type'), data.get('score'), data.get('difficulty', 'medium'))
    return jsonify({'success': True, 'best_score': get_best_score(user_id, data.get('game_type'))})

@app.route('/api/upload-avatar', methods=['POST'])
def upload_avatar():
    user_id, user_data = get_current_user()
    if not user_id:
        return jsonify({'success': False}), 401
    data = request.json
    users = load_users()
    users[user_id]['avatar'] = data.get('avatar')
    save_users(users)
    return jsonify({'success': True})

@app.route('/api/update-profile', methods=['POST'])
def update_profile():
    user_id, user_data = get_current_user()
    if not user_id:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    data = request.json
    display_name = data.get('display_name', '').strip()
    
    if not display_name or len(display_name) < 2:
        return jsonify({'success': False, 'message': 'Display name must be at least 2 characters'})
    
    users = load_users()
    users[user_id]['display_name'] = display_name
    save_users(users)
    
    return jsonify({'success': True, 'message': 'Profile updated'})

@app.route('/api/change-password', methods=['POST'])
def change_password():
    user_id, user_data = get_current_user()
    if not user_id:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    data = request.json
    current_password = data.get('current_password', '')
    new_password = data.get('new_password', '')
    
    # Verify current password
    users = load_users()
    if users[user_id]['password'] != hash_password(current_password):
        return jsonify({'success': False, 'message': 'Current password is incorrect'})
    
    if len(new_password) < 5:
        return jsonify({'success': False, 'message': 'New password must be at least 5 characters'})
    
    # Update password
    users[user_id]['password'] = hash_password(new_password)
    save_users(users)
    
    return jsonify({'success': True, 'message': 'Password changed successfully'})

@app.route('/api/delete-account', methods=['POST'])
def delete_account():
    user_id, user_data = get_current_user()
    if not user_id:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    data = request.json
    email = data.get('email', '').strip()
    
    # Verify email matches
    if email != user_id:
        return jsonify({'success': False, 'message': 'Email does not match'})
    
    # Delete user
    users = load_users()
    if user_id in users:
        del users[user_id]
        save_users(users)
    
    # Delete scores
    scores = load_scores()
    if user_id in scores:
        del scores[user_id]
        save_scores(scores)
    
    # Clear session
    session.clear()
    
    return jsonify({'success': True, 'message': 'Account deleted'})

if __name__ == '__main__':
    app.run(debug=True)