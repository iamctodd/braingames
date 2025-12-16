# Brain Games - Quick Wins Implementation Guide
## Get Started in One Weekend!

This guide walks you through implementing the **3 Quick Wins** that will make your app feel 100% more modern:
1. **Dark Mode** ✨
2. **Avatar Upload** 🖼️
3. **Global Leaderboards** 🏆

---

## Prerequisites
- Your Brain Games Flask app running locally
- Firebase project set up with:
  - Authentication enabled
  - Firestore database
  - Storage bucket (for avatars)
- Basic understanding of Flask templates and JavaScript

---

## STEP 1: Dark Mode Implementation (30 minutes)

### 1.1 - Update Firebase Config in base.html
Replace your current `<head>` section with the updated `base-updated.html` provided.

Key additions:
```html
<!-- Dark mode config for Tailwind -->
<script>
    tailwind.config = {
        darkMode: 'class',  // ← This enables dark mode
        // ... rest of config
    }
</script>
```

### 1.2 - Add theme.js to your project
```bash
# Copy to your static/js folder
cp theme.js static/js/theme.js
```

### 1.3 - Include in base.html before closing </body>
```html
<script src="/static/js/theme.js"></script>
```

### 1.4 - Add theme toggle button to navbar
In your navbar (in base.html), add this button:
```html
<button id="theme-toggle" 
        onclick="window.toggleTheme()"
        class="p-2 rounded-lg dark:bg-gray-700 bg-gray-100 text-gray-700 dark:text-yellow-400">
    <!-- Sun/Moon icons here -->
</button>
```

### 1.5 - Update CSS in all game templates
Add `dark:` variants to your existing Tailwind classes:

**Before:**
```html
<div class="bg-white text-gray-900">
```

**After:**
```html
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-white">
```

### 1.6 - Update Firestore schema
Add theme preference to user document:
```javascript
// In Firebase console, manually add to a test user:
{
  theme: "dark"  // or "light"
}
```

Or let app.py handle it:
```python
# In update_settings route (from app-routes.py):
db.collection('users').document(user_id).update({
    'theme': 'dark'
})
```

### Testing:
1. Load your app
2. Click the theme toggle button (sun/moon icon)
3. Check that colors change smoothly
4. Refresh page - theme persists ✓

**Time estimate:** 30 minutes

---

## STEP 2: Avatar Upload System (60 minutes)

### 2.1 - Enable Firebase Storage
1. Go to Firebase Console → Storage
2. Click "Get Started"
3. Accept default security rules (we'll update them)
4. Wait for initialization

### 2.2 - Set Firebase Storage Rules
In Firebase Console → Storage → Rules, replace with:

```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /avatars/{userId}/{allPaths=**} {
      allow read: if true;
      allow write, delete: if request.auth.uid == userId;
    }
  }
}
```

This allows:
- Anyone to VIEW avatars (public read)
- Only users to UPLOAD/DELETE their own avatars

### 2.3 - Add avatar-manager.js
```bash
cp avatar-manager.js static/js/avatar-manager.js
```

Add to base.html:
```html
<script src="/static/js/avatar-manager.js"></script>
```

### 2.4 - Create Profile Page (templates/profile.html)
Create a new file with avatar upload:

```html
{% extends "base.html" %}

{% block content %}
<div class="max-w-4xl mx-auto">
    <!-- Profile Header -->
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-8 mb-6">
        <div class="flex items-center gap-6">
            <!-- Avatar -->
            <div class="relative">
                <img id="profile-avatar" 
                     src="{{ user.avatar or '/static/img/default-avatar.png' }}"
                     alt="Profile"
                     class="w-32 h-32 rounded-full object-cover border-4 border-blue-500">
                
                {% if is_owner %}
                <button onclick="window.triggerAvatarUpload()"
                        class="absolute bottom-0 right-0 bg-blue-500 hover:bg-blue-600 text-white p-2 rounded-full">
                    📷
                </button>
                {% endif %}
            </div>

            <!-- User Info -->
            <div class="flex-1">
                <h1 class="text-3xl font-bold dark:text-white">{{ user.displayName or user.email }}</h1>
                <p class="text-gray-600 dark:text-gray-400 mt-2">{{ user.bio or 'No bio yet' }}</p>
                
                <div class="mt-4 grid grid-cols-3 gap-4">
                    <div>
                        <p class="text-sm text-gray-600 dark:text-gray-400">Games Played</p>
                        <p class="text-2xl font-bold dark:text-white">{{ stats.totalGamesPlayed }}</p>
                    </div>
                    <div>
                        <p class="text-sm text-gray-600 dark:text-gray-400">Best Score</p>
                        <p class="text-2xl font-bold dark:text-white">{{ stats.bestScore }}</p>
                    </div>
                    <div>
                        <p class="text-sm text-gray-600 dark:text-gray-400">Streak</p>
                        <p class="text-2xl font-bold dark:text-white">{{ stats.currentStreak }} 🔥</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Avatar Upload Form (hidden) -->
    <input type="file" id="avatar-input" style="display: none;" accept="image/*">
    
    <!-- Hidden drop zone (optional) -->
    <div id="avatar-drop-zone" style="display: none;"></div>

    <!-- Recent Games -->
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-8">
        <h2 class="text-xl font-bold dark:text-white mb-4">Recent Games</h2>
        <table class="w-full">
            <thead>
                <tr class="border-b dark:border-gray-700">
                    <th class="text-left px-4 py-2 dark:text-gray-300">Game</th>
                    <th class="text-left px-4 py-2 dark:text-gray-300">Score</th>
                    <th class="text-left px-4 py-2 dark:text-gray-300">Difficulty</th>
                    <th class="text-left px-4 py-2 dark:text-gray-300">Date</th>
                </tr>
            </thead>
            <tbody>
                {% for session in sessions[:10] %}
                <tr class="border-b dark:border-gray-700 hover:dark:bg-gray-700">
                    <td class="px-4 py-3 dark:text-gray-300">
                        {{ session.gameType|replace('_', ' ')|title }}
                    </td>
                    <td class="px-4 py-3 font-bold dark:text-green-400">{{ session.score }}</td>
                    <td class="px-4 py-3">
                        <span class="px-2 py-1 rounded dark:bg-gray-700 capitalize">
                            {{ session.difficulty }}
                        </span>
                    </td>
                    <td class="px-4 py-3 text-sm dark:text-gray-400">
                        {{ session.timestamp.strftime('%Y-%m-%d') if session.timestamp else 'N/A' }}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
{% endblock %}
```

### 2.5 - Create Edit Profile Route in app.py
Add this to your Flask app (or use the routes from app-routes.py):

```python
@app.route('/api/profile/update', methods=['POST'])
@login_required
def update_profile():
    """Update user profile (displayName, bio)"""
    data = request.get_json()
    user_id = session.get('user_id')
    
    from firebase_admin import firestore
    db = firestore.client()
    
    try:
        db.collection('users').document(user_id).update({
            'displayName': data.get('displayName', ''),
            'bio': data.get('bio', '')
        })
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

### 2.6 - Update Navigation to Show Avatar
In base.html navbar, update the avatar display:

```html
<img id="navbar-avatar" 
     src="{{ current_user.avatar or '/static/img/default-avatar.png' }}"
     alt="Avatar"
     class="w-8 h-8 rounded-full object-cover cursor-pointer"
     onclick="window.location.href='/profile'">
```

### Testing:
1. Go to `/profile` page
2. Click the 📷 button next to avatar
3. Select an image from your computer
4. Watch it upload and display ✓
5. Refresh page - avatar persists in Firestore ✓

**Time estimate:** 60 minutes

---

## STEP 3: Global Leaderboards (90 minutes)

### 3.1 - Create game_sessions collection structure
Each time a user completes a game, save to Firestore:

```javascript
// Collection: game_sessions
{
  sessionId: "auto-generated",
  userId: "user123",
  gameType: "memory",        // or "problem_solving", "tbi_memory"
  score: 850,
  difficulty: "hard",        // or "easy", "medium"
  duration: 300,             // seconds
  timestamp: "2025-01-15T14:30:00Z",
  sequence: [...],           // for replay
  moves: [...]               // for replay
}
```

### 3.2 - Update game templates to log sessions
When a game ends, call the API:

```javascript
// In your memory game, problem_solving, etc. - after game completes:
async function logGameSession(gameType, score, difficulty, durationSeconds) {
    try {
        const response = await fetch('/api/game-session', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                gameType: gameType,      // "memory"
                score: score,            // 850
                difficulty: difficulty,  // "hard"
                duration: durationSeconds, // 300
                sequence: [],           // optional
                moves: []               // optional
            })
        });
        
        const data = await response.json();
        if (data.success) {
            console.log('Session logged:', data.sessionId);
            // Show celebration, update stats, etc.
        }
    } catch (error) {
        console.error('Error logging session:', error);
    }
}
```

### 3.3 - Add routes from app-routes.py to your Flask app
Copy these functions from app-routes.py into your `app.py`:
- `get_leaderboard(game_type)`
- `calculate_user_stats(sessions)`

They handle querying Firestore and formatting the data.

### 3.4 - Add leaderboard-manager.js
```bash
cp leaderboard-manager.js static/js/leaderboard-manager.js
```

Add to base.html:
```html
<script src="/static/js/leaderboard-manager.js"></script>
```

### 3.5 - Create Leaderboards Page (templates/leaderboards.html)
Create a new file:

```html
{% extends "base.html" %}

{% block content %}
<div class="max-w-6xl mx-auto">
    <!-- Header -->
    <div class="mb-8">
        <h1 class="text-3xl font-bold dark:text-white mb-2">🏆 Global Leaderboards</h1>
        <p class="text-gray-600 dark:text-gray-400">
            See how you rank against other players
        </p>
    </div>

    <!-- Game Type Tabs -->
    <div class="flex gap-2 mb-6 border-b dark:border-gray-700">
        <button data-game-type="memory" class="active px-4 py-2 border-b-2 border-blue-500 font-semibold dark:text-white">
            🧩 Memory Training
        </button>
        <button data-game-type="problem_solving" class="px-4 py-2 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white">
            💡 Problem Solving
        </button>
        <button data-game-type="tbi_memory" class="px-4 py-2 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white">
            🎯 TBI Memory
        </button>
    </div>

    <!-- Timeframe Tabs -->
    <div class="flex gap-2 mb-6">
        <button data-timeframe="alltime" class="active px-3 py-2 rounded-lg dark:bg-gray-700 bg-gray-100 text-sm font-medium dark:text-white">
            All Time
        </button>
        <button data-timeframe="month" class="px-3 py-2 rounded-lg text-sm font-medium text-gray-600 dark:text-gray-400">
            This Month
        </button>
        <button data-timeframe="week" class="px-3 py-2 rounded-lg text-sm font-medium text-gray-600 dark:text-gray-400">
            This Week
        </button>
    </div>

    <!-- Leaderboard Table -->
    <div id="leaderboard-table">
        <div class="text-center py-12">
            <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
            <p class="mt-4 text-gray-600 dark:text-gray-400">Loading leaderboard...</p>
        </div>
    </div>
</div>

<!-- Include styles for tabs -->
<style>
    [data-game-type].active,
    [data-timeframe].active {
        @apply border-blue-500 dark:border-blue-400;
    }
</style>
{% endblock %}
```

### 3.6 - Add Leaderboards link to navbar
In base.html, add to navigation:
```html
<a href="/leaderboards" class="text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white">
    Leaderboards
</a>
```

### 3.7 - Update Flask routes
Add these routes to your `app.py` (from app-routes.py):

```python
@app.route('/leaderboards')
def leaderboards():
    return render_template('leaderboards.html')

@app.route('/api/leaderboards/<game_type>')
def get_leaderboard(game_type):
    # See app-routes.py for full implementation
    pass
```

### Testing:
1. Complete a game and observe the session logging
2. Go to `/leaderboards`
3. Watch the data load
4. Switch between game types, timeframes
5. See your rank highlighted ✓

**Time estimate:** 90 minutes

---

## Summary: What You've Built

| Feature | Time | Impact |
|---------|------|--------|
| Dark Mode | 30 min | ✨ Modern, professional feel |
| Avatar Upload | 60 min | 🖼️ Personal identity & connection |
| Leaderboards | 90 min | 🏆 Competition & engagement |
| **Total** | **3 hours** | **100% improvement in perceived quality** |

---

## Common Issues & Fixes

### Dark Mode not persisting?
- Check `theme.js` is loaded BEFORE other scripts
- Verify Firestore has `theme` field on users
- Check browser localStorage (DevTools → Application → Local Storage)

### Avatar upload fails?
- Check Firebase Storage bucket name in your config
- Verify auth user exists in Firestore users collection
- Check browser console for errors (DevTools → Console)

### Leaderboard shows no data?
- Verify game sessions are being logged (check Firestore collections)
- Confirm `gameType` matches exactly (case-sensitive)
- Check API response in Network tab (DevTools → Network)

### Styling looks off?
- Make sure Tailwind CSS is properly configured with `darkMode: 'class'`
- Clear browser cache (Cmd+Shift+R or Ctrl+Shift+R)
- Verify you're using full Tailwind CDN script

---

## Next Steps

Once these 3 are live:
1. **Run analytics** — See which games users prefer
2. **Add daily challenges** — Increase daily retention
3. **Implement badges** — Celebrate milestones
4. **Create tutorials** — Onboard new users better

---

## Files Provided

- ✅ `theme.js` — Dark mode system
- ✅ `avatar-manager.js` — Avatar upload handling
- ✅ `leaderboard-manager.js` — Leaderboards display
- ✅ `base-updated.html` — Enhanced navbar & structure
- ✅ `app-routes.py` — Flask route handlers
- ✅ `BRAIN_GAMES_ROADMAP.md` — Full 8-week plan

---

## Questions?

Each JavaScript file is heavily commented. Read the comments for:
- How functions work
- What API endpoints they call
- How data flows through the system

Good luck! 🚀