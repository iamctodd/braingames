from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os
from datetime import datetime, timedelta
import hashlib

app = Flask(__name__)
app.secret_key = 'brain-games-secret-key-2025'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

USERS_FILE = 'users.json'
SCORES_FILE = 'scores.json'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Initialize default users if file doesn't exist
def init_default_users():
    if not os.path.exists(USERS_FILE):
        users = {
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
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f, indent=2)

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
        data = request.json
        success, msg = create_user(data.get('email'), data.get('password'), data.get('display_name'))
        return jsonify({'success': success, 'message': msg})
    return render_template('auth/signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        success, result = verify_user(data.get('email'), data.get('password'))
        if success:
            session.permanent = True
            session['user_id'] = data.get('email')
            return jsonify({'success': True})
        return jsonify({'success': False, 'message': result})
    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

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

if __name__ == '__main__':
    app.run(debug=True) # Just updated
