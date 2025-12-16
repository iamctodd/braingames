# Brain Games - Code Examples & Integration Guide

Quick reference for how to integrate the new features into your existing code.

---

## Integration Points

### 1. Update Existing Templates

Every template that extends `base.html` automatically gets:
- Dark mode support
- Theme toggle button
- Avatar display in navbar
- Better responsive design

**No changes needed to existing game templates!** They automatically inherit the new navbar.

---

## 2. Logging Game Sessions

When a user completes a game, call this to log it:

### In Memory Training Game (example)
```javascript
async function endGame(finalScore) {
    // Calculate difficulty based on sequence length
    const difficulty = sequenceLength <= 5 ? 'easy' : 
                       sequenceLength <= 10 ? 'medium' : 'hard';
    
    // Log the session
    const response = await fetch('/api/game-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            gameType: 'memory',
            score: finalScore,
            difficulty: difficulty,
            duration: Math.floor((Date.now() - gameStartTime) / 1000),
            sequence: gameSequence,  // Optional: for replay
            moves: playerMoves       // Optional: for replay
        })
    });
    
    const data = await response.json();
    if (data.success) {
        console.log('Session saved:', data.sessionId);
        // Show celebration, confetti, etc.
        celebrateVictory();
    }
}
```

### In Problem Solving Game
```javascript
async function submitCaseSolution(caseId, solutionText) {
    // Evaluate solution (you define scoring logic)
    const score = evaluateSolution(solutionText);
    
    // Log it
    await fetch('/api/game-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            gameType: 'problem_solving',
            score: score,
            difficulty: 'medium',  // Adjust based on case difficulty
            duration: timeSpentSeconds,
            caseId: caseId
        })
    });
}
```

### In TBI Memory Game
```javascript
async function completeMemoryRound(wordsRemembered, totalWords) {
    const score = (wordsRemembered / totalWords) * 100;
    const difficulty = totalWords <= 5 ? 'easy' : 
                       totalWords <= 10 ? 'medium' : 'hard';
    
    await fetch('/api/game-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            gameType: 'tbi_memory',
            score: Math.floor(score),
            difficulty: difficulty,
            duration: timeSpentSeconds
        })
    });
}
```

---

## 3. Accessing User Data

### Get current user in Flask
```python
def get_current_user():
    from firebase_admin import firestore
    user_id = session.get('user_id')
    if not user_id:
        return None
    
    db = firestore.client()
    user_doc = db.collection('users').document(user_id).get()
    if user_doc.exists:
        return user_doc.to_dict()
    return None

# Use it:
current_user = get_current_user()
if current_user:
    print(current_user['displayName'])
    print(current_user['avatar'])
    print(current_user['stats'])
```

### Get user stats in JavaScript
```javascript
async function getUserStats(userId) {
    const response = await fetch(`/api/user/${userId}/stats`);
    const stats = await response.json();
    
    console.log('Total games:', stats.totalGamesPlayed);
    console.log('Best score:', stats.bestScore);
    console.log('Current streak:', stats.currentStreak);
    
    // Update UI
    document.getElementById('stats').innerHTML = `
        <p>Games: ${stats.totalGamesPlayed}</p>
        <p>Best: ${stats.bestScore}</p>
        <p>Streak: ${stats.currentStreak} 🔥</p>
    `;
}
```

---

## 4. Dynamic Difficulty Adjustment

Example: Adjust game parameters based on selected difficulty

### Memory Training
```javascript
const DIFFICULTY_SETTINGS = {
    easy: {
        startLength: 3,
        speed: 1000,      // ms per color
        pause: 2000       // ms between colors
    },
    medium: {
        startLength: 5,
        speed: 800,
        pause: 1500
    },
    hard: {
        startLength: 7,
        speed: 600,
        pause: 1000
    }
};

function startGameWithDifficulty(difficulty = 'medium') {
    const settings = DIFFICULTY_SETTINGS[difficulty];
    gameSequence = [];
    currentLength = settings.startLength;
    colorSpeed = settings.speed;
    pauseBetweenFlashes = settings.pause;
    
    // Log difficulty for session
    currentDifficulty = difficulty;
    
    playRound();
}
```

### Problem Solving
```javascript
const CASES_BY_DIFFICULTY = {
    easy: [
        { id: 1, title: 'Betty\'s Bakery', complexity: 'low' },
        { id: 2, title: 'Office Schedule', complexity: 'low' }
    ],
    medium: [
        { id: 3, title: 'Team Communication', complexity: 'medium' },
        { id: 4, title: 'Customer Service', complexity: 'medium' }
    ],
    hard: [
        { id: 5, title: 'Multi-Department Crisis', complexity: 'high' },
        { id: 6, title: 'Budget & Quality Balance', complexity: 'high' }
    ]
};

function selectDifficulty(difficulty) {
    const cases = CASES_BY_DIFFICULTY[difficulty];
    currentCase = cases[Math.floor(Math.random() * cases.length)];
    currentDifficulty = difficulty;
    
    displayCase(currentCase);
}
```

---

## 5. Displaying User Avatar Everywhere

### In templates
```html
<!-- Profile page -->
<img src="{{ user.avatar or '/static/img/default-avatar.png' }}"
     alt="Avatar"
     class="w-32 h-32 rounded-full">

<!-- Leaderboard row -->
<img src="{{ entry.avatar or '/static/img/default-avatar.png' }}"
     alt="{{ entry.displayName }}"
     class="w-10 h-10 rounded-full">

<!-- Comment/session -->
<div class="flex gap-3">
    <img id="avatar-{{ session.userId }}"
         src="{{ session.userAvatar or '/static/img/default-avatar.png' }}"
         alt="User"
         class="w-8 h-8 rounded-full">
    <div>
        <p class="font-bold">{{ session.displayName }}</p>
        <p>Score: {{ session.score }}</p>
    </div>
</div>
```

### Dynamic avatar updates
```javascript
// When avatar changes, update all instances
function updateAllAvatars(userId, newAvatarUrl) {
    document.querySelectorAll(`[data-avatar-user="${userId}"]`).forEach(img => {
        img.src = newAvatarUrl;
        // Add fade animation
        img.style.opacity = '0';
        setTimeout(() => img.style.opacity = '1', 100);
    });
}

// Usage:
updateAllAvatars('user123', 'https://...');
```

---

## 6. Calculating Scores Consistently

### Score calculation helper
```python
def calculate_game_score(game_type, metrics):
    """
    Calculate score based on game type and metrics
    """
    base_score = 0
    
    if game_type == 'memory':
        # Score based on sequence length achieved
        sequence_length = metrics.get('sequenceLength', 3)
        base_score = sequence_length * 100
        
    elif game_type == 'problem_solving':
        # Score based on solution quality (1-100)
        quality = metrics.get('solutionQuality', 50)
        efficiency = metrics.get('efficiency', 1.0)  # Time factor
        base_score = quality * efficiency
        
    elif game_type == 'tbi_memory':
        # Score based on words remembered
        remembered = metrics.get('wordsRemembered', 0)
        total = metrics.get('totalWords', 10)
        base_score = (remembered / total) * 100
    
    # Apply difficulty multiplier
    difficulty = metrics.get('difficulty', 'medium')
    multipliers = {'easy': 1.0, 'medium': 1.5, 'hard': 2.0}
    multiplier = multipliers.get(difficulty, 1.0)
    
    final_score = int(base_score * multiplier)
    return max(0, final_score)  # Ensure non-negative

# Usage in Flask:
@app.route('/api/calculate-score', methods=['POST'])
def calculate_score():
    data = request.get_json()
    score = calculate_game_score(data['gameType'], data['metrics'])
    return jsonify({'score': score})
```

---

## 7. Custom Styling for Dark Mode

### Add to base.html or components.css
```css
/* Override default Tailwind for better dark mode */
@layer components {
    .card {
        @apply bg-white dark:bg-gray-800 rounded-lg shadow dark:shadow-lg;
    }
    
    .card-header {
        @apply bg-gray-50 dark:bg-gray-700 border-b dark:border-gray-600 px-6 py-4;
    }
    
    .btn-primary {
        @apply bg-blue-500 hover:bg-blue-600 dark:bg-blue-600 dark:hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition;
    }
    
    .btn-secondary {
        @apply bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 text-gray-900 dark:text-white px-4 py-2 rounded-lg transition;
    }
    
    .input-field {
        @apply bg-white dark:bg-gray-700 border dark:border-gray-600 rounded px-3 py-2 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400;
    }
    
    .text-muted {
        @apply text-gray-600 dark:text-gray-400;
    }
}

/* Custom animations */
@keyframes slideDown {
    from { transform: translateY(-10px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.animate-slide-down {
    animation: slideDown 0.3s ease-out;
}
```

---

## 8. TBI-Specific Features

### Adaptive difficulty progression
```javascript
// Track user performance
class TBIGameTracker {
    constructor() {
        this.consecutiveSuccesses = 0;
        this.consecutiveFailures = 0;
        this.currentDifficulty = 'easy';
    }
    
    recordResult(success) {
        if (success) {
            this.consecutiveSuccesses += 1;
            this.consecutiveFailures = 0;
            
            // Increase difficulty after 3 successes
            if (this.consecutiveSuccesses >= 3) {
                this.advanceDifficulty();
            }
        } else {
            this.consecutiveFailures += 1;
            this.consecutiveSuccesses = 0;
            
            // Decrease difficulty after 2 failures
            if (this.consecutiveFailures >= 2) {
                this.decreaseDifficulty();
            }
        }
    }
    
    advanceDifficulty() {
        const difficulties = ['easy', 'medium', 'hard'];
        const currentIndex = difficulties.indexOf(this.currentDifficulty);
        if (currentIndex < difficulties.length - 1) {
            this.currentDifficulty = difficulties[currentIndex + 1];
            this.showCelebration('Great job! Difficulty increased! 🎉');
        }
        this.consecutiveSuccesses = 0;
    }
    
    decreaseDifficulty() {
        const difficulties = ['easy', 'medium', 'hard'];
        const currentIndex = difficulties.indexOf(this.currentDifficulty);
        if (currentIndex > 0) {
            this.currentDifficulty = difficulties[currentIndex - 1];
        }
        this.consecutiveFailures = 0;
    }
    
    showCelebration(message) {
        const element = document.createElement('div');
        element.textContent = message;
        element.className = 'fixed top-4 left-1/2 transform -translate-x-1/2 bg-green-500 text-white px-4 py-2 rounded-lg';
        document.body.appendChild(element);
        
        setTimeout(() => element.remove(), 3000);
    }
}

// Usage:
const tracker = new TBIGameTracker();
tracker.recordResult(true);  // Success
tracker.recordResult(true);  // Success
tracker.recordResult(true);  // Success → Difficulty increases
```

---

## 9. Mobile-Specific Considerations

### Touch-friendly buttons
```html
<!-- Make buttons bigger for mobile -->
<button class="px-6 py-4 text-lg md:px-4 md:py-2 md:text-sm">
    Play Game
</button>

<!-- Min-width 48px × 48px per touch guidelines -->
<style>
    button {
        min-width: 48px;
        min-height: 48px;
    }
</style>
```

### Responsive game boards
```html
<!-- Games scale properly -->
<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2 sm:gap-3 md:gap-4">
    <button class="aspect-square">1</button>
    <button class="aspect-square">2</button>
    <!-- etc -->
</div>
```

---

## 10. Analytics Integration

### Track page views
```javascript
// Send pageview to analytics
function trackPageView(pageName) {
    gtag('event', 'page_view', {
        'page_title': pageName,
        'page_path': window.location.pathname
    });
}

// Call on important pages:
// trackPageView('memory_game');
// trackPageView('leaderboards');
```

### Track game completion
```javascript
function trackGameCompletion(gameType, score, difficulty) {
    gtag('event', 'game_completed', {
        'game_type': gameType,
        'score': score,
        'difficulty': difficulty
    });
}

// In your game end handler:
// trackGameCompletion('memory', 850, 'hard');
```

---

## 11. Testing Your Integrations

### Test dark mode
```javascript
// In console:
document.documentElement.classList.add('dark');  // Enable dark
document.documentElement.classList.remove('dark');  // Disable
```

### Test avatar upload
```javascript
// Manually set avatar in Firestore Console
// Then refresh page and check navbar

// Or test via JavaScript:
window.AvatarManager.uploadAvatar(fileFromInput);
```

### Test leaderboards
```javascript
// Manually create game sessions in Firestore:
db.collection('game_sessions').add({
    userId: 'user123',
    gameType: 'memory',
    score: 850,
    difficulty: 'hard',
    timestamp: new Date()
});

// Then refresh leaderboards page
```

---

## 12. Monitoring & Debugging

### Check Firestore data
```javascript
// In browser console:
firebase.firestore().collection('game_sessions').limit(5).get().then(snap => {
    snap.docs.forEach(doc => console.log(doc.data()));
});
```

### Check authentication
```javascript
// In browser console:
firebase.auth().onAuthStateChanged(user => {
    if (user) {
        console.log('Logged in as:', user.email);
        console.log('UID:', user.uid);
    } else {
        console.log('Not logged in');
    }
});
```

### Monitor performance
```javascript
// Add to base.html:
window.addEventListener('load', () => {
    const perfData = window.performance.timing;
    const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
    console.log('Page load time:', pageLoadTime + 'ms');
    
    // Track slow loads
    if (pageLoadTime > 3000) {
        console.warn('Page load slow:', pageLoadTime + 'ms');
    }
});
```

---

## Next Steps

1. **Implement the 3 quick wins** using this guide
2. **Test thoroughly** with the checklist
3. **Monitor user feedback** and adjust
4. **Plan Phase 2** (analytics, badges, friend system)

Good luck! 🚀
