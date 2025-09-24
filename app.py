from flask import Flask, render_template, jsonify, request, session
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

@app.route('/test-firebase')
def test_firebase():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Firebase Test</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
    <div class="max-w-md mx-auto bg-white rounded-lg shadow p-6">
        <h1 class="text-xl font-bold mb-4">Firebase Connection Test</h1>
        <div id="test-results" class="space-y-2"></div>
        <button id="test-btn" class="bg-blue-600 text-white px-4 py-2 rounded mt-4">
            Test Firebase
        </button>
    </div>

    <script type="module">
        import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js';
        import { getAuth, onAuthStateChanged } from 'https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js';
        
        const results = document.getElementById('test-results');
        
        function addResult(message, success = true) {
            const div = document.createElement('div');
            div.className = `p-2 rounded ${success ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`;
            div.textContent = message;
            results.appendChild(div);
            console.log(message);
        }
        
        try {
            // Your Firebase config - REPLACE WITH REAL VALUES
            const firebaseConfig = {
                apiKey: "your-actual-api-key-here",
                authDomain: "braingames-5ded7.firebaseapp.com",
                projectId: "braingames-5ded7",
                storageBucket: "braingames-5ded7.appspot.com",
                messagingSenderId: "123456789",
                appId: "your-actual-app-id"
            };
            
            addResult("✅ Firebase config loaded");
            
            const app = initializeApp(firebaseConfig);
            addResult("✅ Firebase app initialized");
            
            const auth = getAuth();
            addResult("✅ Firebase Auth ready");
            
            onAuthStateChanged(auth, (user) => {
                if (user) {
                    addResult(`✅ User logged in: ${user.email}`);
                } else {
                    addResult("ℹ️ No user logged in");
                }
            });
            
            document.getElementById('test-btn').addEventListener('click', () => {
                addResult("🔄 Auth state listener is working!");
            });
            
        } catch (error) {
            addResult(`❌ Firebase Error: ${error.message}`, false);
            console.error('Firebase error:', error);
        }
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)