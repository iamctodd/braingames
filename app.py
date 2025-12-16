from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Score storage file
SCORES_FILE = 'scores.json'

def load_scores():
    """Load scores from JSON file"""
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            return json.load(f)
    return {'memory': [], 'problem_solving': [], 'tbi_memory': []}

def save_scores(scores):
    """Save scores to JSON file"""
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f, indent=2)

def add_score(game_type, score, difficulty='medium'):
    """Add a new score"""
    scores = load_scores()
    scores[game_type].append({
        'score': score,
        'difficulty': difficulty,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    # Keep only last 100 scores per game
    scores[game_type] = scores[game_type][-100:]
    save_scores(scores)

def get_best_score(game_type):
    """Get best score for a game"""
    scores = load_scores()
    if scores[game_type]:
        return max(s['score'] for s in scores[game_type])
    return 0

def get_game_stats(game_type):
    """Get stats for a game"""
    scores = load_scores()
    game_scores = scores[game_type]
    if not game_scores:
        return {'best': 0, 'average': 0, 'total': 0}
    
    return {
        'best': max(s['score'] for s in game_scores),
        'average': round(sum(s['score'] for s in game_scores) / len(game_scores)),
        'total': len(game_scores)
    }

def get_all_games_stats():
    """Get stats for all games"""
    return {
        'memory': get_game_stats('memory'),
        'problem_solving': get_game_stats('problem_solving'),
        'tbi_memory': get_game_stats('tbi_memory')
    }

def get_recent_scores(limit=10):
    """Get recent scores across all games"""
    scores = load_scores()
    all_scores = []
    for game_type, game_scores in scores.items():
        for score in game_scores:
            all_scores.append({
                'game': game_type.replace('_', ' ').title(),
                'game_type': game_type,
                **score
            })
    # Sort by date, newest first
    all_scores.sort(key=lambda x: x['date'], reverse=True)
    return all_scores[:limit]

@app.route('/')
def index():
    stats = get_all_games_stats()
    recent = get_recent_scores(10)
    
    return render_template('index.html',
        memory_best=stats['memory']['best'],
        memory_total=stats['memory']['total'],
        problem_best=stats['problem_solving']['best'],
        problem_total=stats['problem_solving']['total'],
        tbi_best=stats['tbi_memory']['best'],
        tbi_total=stats['tbi_memory']['total'],
        total_games=stats['memory']['total'] + stats['problem_solving']['total'] + stats['tbi_memory']['total'],
        recent_scores=recent
    )

@app.route('/dashboard')
def dashboard():
    stats = get_all_games_stats()
    return render_template('dashboard.html', stats=stats)

@app.route('/history')
def history():
    scores = load_scores()
    # Combine all scores with game type info
    all_scores = []
    for game_type, game_scores in scores.items():
        for score in game_scores:
            all_scores.append({
                'game': game_type.replace('_', ' ').title(),
                'game_type': game_type,
                **score
            })
    # Sort by date, newest first
    all_scores.sort(key=lambda x: x['date'], reverse=True)
    return render_template('history.html', scores=all_scores)

@app.route('/games/memory')
def memory():
    stats = get_game_stats('memory')
    return render_template('games/memory.html', best_score=stats['best'], total_games=stats['total'])

@app.route('/games/problem-solving')
def problem_solving():
    stats = get_game_stats('problem_solving')
    return render_template('games/problem_solving.html', best_score=stats['best'], total_games=stats['total'])

@app.route('/games/tbi-memory')
def tbi_memory():
    stats = get_game_stats('tbi_memory')
    return render_template('games/tbi_memory.html', best_score=stats['best'], total_games=stats['total'])

# API endpoint to save score
@app.route('/api/save-score', methods=['POST'])
def save_score():
    """Save a game score"""
    data = request.json
    game_type = data.get('game_type')
    score = data.get('score')
    difficulty = data.get('difficulty', 'medium')
    
    add_score(game_type, score, difficulty)
    
    return jsonify({
        'success': True,
        'best_score': get_best_score(game_type),
        'message': 'Score saved!'
    })

if __name__ == '__main__':
    print("🧠 Brain Games - Beautiful Home Page")
    print("✓ http://127.0.0.1:5000/")
    print("✓ http://127.0.0.1:5000/dashboard")
    print("✓ http://127.0.0.1:5000/history")
    app.run(debug=True)
