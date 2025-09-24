from flask import Flask, render_template, jsonify, request, session, redirect
from functools import wraps
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'  # Change this in production

# Decorator to require authentication
def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Auth endpoints
@app.route('/api/auth/login', methods=['POST'])
def login():
    """Handle Firebase auth token verification"""
    data = request.get_json()
    # In production, verify the Firebase ID token here
    # For now, we'll trust the frontend auth
    user_data = data.get('user')
    session['user'] = user_data
    return jsonify({'success': True, 'user': user_data})

@app.route('/debug-session')
def debug_session():
    return jsonify({
        'session_data': dict(session),
        'has_user': 'user' in session,
        'session_keys': list(session.keys())
    })

@app.route('/logout')
def logout_page():
    # Clear Flask session
    session.clear()
    # Redirect to home with success message
    return redirect('/?message=signed-out')

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({'success': True})

@app.route('/api/auth/user')
def get_user():
    return jsonify({'user': session.get('user')})

# Game-specific API endpoints
@app.route('/api/games/memory/score', methods=['POST'])
@require_auth
def save_memory_score():
    data = request.get_json()
    user_id = session['user']['uid']
    score = data.get('score')
    # Save to database in production
    return jsonify({'success': True, 'message': 'Score saved'})

@app.route('/api/games/problem-solving/response', methods=['POST'])
@require_auth
def save_problem_solving_response():
    data = request.get_json()
    user_id = session['user']['uid']
    case_id = data.get('case_id')
    response = data.get('response')
    # Save to database in production
    return jsonify({'success': True, 'message': 'Response saved'})

@app.route('/api/games/tbi-memory/progress', methods=['POST'])
@require_auth
def save_tbi_progress():
    data = request.get_json()
    user_id = session['user']['uid']
    progress = data.get('progress')
    # Save to database in production
    return jsonify({'success': True, 'message': 'Progress saved'})

# Game routes
@app.route('/games/memory')
def memory_game():
    return render_template('games/memory.html')

@app.route('/games/problem-solving')
def problem_solving_game():
    return render_template('games/problem_solving.html')

@app.route('/games/tbi-memory')
def tbi_memory_game():
    return render_template('games/tbi_memory.html')

@app.route('/signin')
def signin_page():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Sign In - Brain Games</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <div class="text-center mb-6">
            <h1 class="text-2xl font-bold">🧠 Brain Games</h1>
            <p class="text-gray-600">Sign in to continue</p>
        </div>
        
        <form action="/manual-login" method="POST" class="space-y-4">
            <div>
                <input type="email" name="email" placeholder="Enter your email" required
                       class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            <div>
                <input type="password" name="password" placeholder="Enter your password" required
                       class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            <button type="submit" class="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700">
                Sign In
            </button>
        </form>
        
        <div class="mt-4 text-center">
            <p class="text-sm text-gray-600">
                For demo: any email + any password works
            </p>
        </div>
    </div>
</body>
</html>
    '''

@app.route('/manual-login', methods=['POST'])
def manual_login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Simple validation - for demo, any email/password works
    if email and password:
        session['user'] = {
            'uid': 'demo-user',
            'email': email,
            'displayName': email.split('@')[0]
        }
        return redirect('/dashboard')
    else:
        return redirect('/signin?error=invalid')

if __name__ == '__main__':
    app.run(debug=True)