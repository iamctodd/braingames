# Brain Games - Implementation Checklist

Print this out! Check items off as you go. 📋

---

## PRE-WORK (Do This First)

- [ ] Read `00_START_HERE.md`
- [ ] Read `IMPLEMENTATION_GUIDE.md` sections 1-3
- [ ] Clone/download all code files to your computer
- [ ] Verify Firebase project is set up:
  - [ ] Authentication enabled (Google, Email/Password)
  - [ ] Firestore database created
  - [ ] Storage bucket created
- [ ] Have your Flask app running locally (localhost:5000)

**Estimated time:** 15 minutes

---

## FEATURE 1: DARK MODE ✨

### Setup
- [ ] Copy `theme.js` to `static/js/theme.js`
- [ ] Update `base.html` with theme configuration script
- [ ] Add `darkMode: 'class'` to Tailwind config

### Implementation
- [ ] Add theme toggle button to navbar
- [ ] Add `dark:` variants to CSS (at least in navbar + main container)
- [ ] Create/update `/settings` route to save theme preference
- [ ] Test localStorage persistence (DevTools → Application → LocalStorage)

### Testing
- [ ] Click theme toggle button
- [ ] Colors change smoothly
- [ ] Refresh page → theme persists
- [ ] System preference detected on first load
- [ ] Works on mobile (swipe or hamburger menu)

### Status
- [ ] ✅ DONE

**Time spent:** _____ minutes

---

## FEATURE 2: AVATAR UPLOAD 🖼️

### Firebase Setup
- [ ] Go to Firebase Console → Storage
- [ ] Click "Get Started"
- [ ] Update Storage Rules to allow avatar uploads:
  ```javascript
  match /avatars/{userId}/{allPaths=**} {
    allow read: if true;
    allow write, delete: if request.auth.uid == userId;
  }
  ```

### Code Setup
- [ ] Copy `avatar-manager.js` to `static/js/avatar-manager.js`
- [ ] Include in `base.html`: `<script src="/static/js/avatar-manager.js"></script>`
- [ ] Add users collection to Firestore (if not exists)

### Create Profile Page
- [ ] Create `templates/profile.html` using template from guide
- [ ] Add profile route to Flask app:
  ```python
  @app.route('/profile')
  @app.route('/profile/<user_id>')
  def profile(user_id=None):
      # See app-routes.py for implementation
  ```

### Update Navbar
- [ ] Add avatar image to navbar:
  ```html
  <img id="navbar-avatar" src="..." class="w-8 h-8 rounded-full">
  ```
- [ ] Link to profile page when clicked

### Testing
- [ ] Go to `/profile`
- [ ] Click camera icon to upload avatar
- [ ] Select image from computer
- [ ] Watch spinner appear while uploading
- [ ] Image displays after upload
- [ ] Avatar shows in navbar
- [ ] Refresh page → avatar persists
- [ ] Avatar appears in leaderboards

### Status
- [ ] ✅ DONE

**Time spent:** _____ minutes

---

## FEATURE 3: GLOBAL LEADERBOARDS 🏆

### Firestore Logging
- [ ] Every game completion logs to `game_sessions` collection
- [ ] Session includes: userId, gameType, score, difficulty, timestamp
- [ ] Add logging call at end of each game:
  ```javascript
  await fetch('/api/game-session', {
      method: 'POST',
      body: JSON.stringify({gameType, score, difficulty, duration})
  })
  ```

### Flask Routes
- [ ] Copy these from `app-routes.py` to your `app.py`:
  - [ ] `get_leaderboard(game_type)` 
  - [ ] `get_analytics_data(game_type)`
  - [ ] `calculate_user_stats(sessions)`
  - [ ] `log_game_session()` 

### Frontend Code
- [ ] Copy `leaderboard-manager.js` to `static/js/leaderboard-manager.js`
- [ ] Include in `base.html`: `<script src="/static/js/leaderboard-manager.js"></script>`

### Create Leaderboards Page
- [ ] Create `templates/leaderboards.html` using template from guide
- [ ] Add route to Flask:
  ```python
  @app.route('/leaderboards')
  def leaderboards():
      return render_template('leaderboards.html')
  ```
- [ ] Add link to navbar

### Testing
- [ ] Play a game and complete it
- [ ] Check Firestore → game_sessions collection for new entry
- [ ] Go to `/leaderboards`
- [ ] Click different game type buttons
- [ ] Click different timeframe buttons (all-time, month, week)
- [ ] Your score appears in top 10
- [ ] Your rank shows (e.g., "Top 15%")
- [ ] Avatar displays next to your name
- [ ] Data updates in real-time

### Status
- [ ] ✅ DONE

**Time spent:** _____ minutes

---

## POST-IMPLEMENTATION

### Testing Checklist
- [ ] Dark mode works on desktop
- [ ] Dark mode works on mobile
- [ ] Avatar upload works
- [ ] Leaderboards display correctly
- [ ] No console errors (DevTools → Console)
- [ ] No Firebase errors
- [ ] All pages load quickly

### Performance Check
- [ ] Lighthouse score (DevTools → Lighthouse)
- [ ] Mobile responsiveness (DevTools → Device Toolbar)
- [ ] Page load time < 3 seconds

### Deployment
- [ ] Commit code to GitHub
- [ ] Push to Render
- [ ] Test live app
- [ ] Share with users!

### Status
- [ ] ✅ DONE

---

## TIME TRACKING

| Feature | Estimated | Actual | Notes |
|---------|-----------|--------|-------|
| Dark Mode | 30 min | ___ | |
| Avatar Upload | 60 min | ___ | |
| Leaderboards | 90 min | ___ | |
| Testing | 30 min | ___ | |
| **TOTAL** | **3 hrs** | ___ | |

---

## WHAT'S NEXT?

Once all 3 features are live, your next priorities (in order):

### Week 2 (Optional, but recommended)
1. **Performance Analytics** (2 hours)
   - [ ] Chart.js for line/bar graphs
   - [ ] Show score progression
   - [ ] Display stats by game type

2. **Achievement Badges** (2 hours)
   - [ ] First Game badge
   - [ ] 7-Day Streak badge
   - [ ] Top 10 Global badge
   - [ ] Display on profile

3. **Difficulty Levels** (1 hour)
   - [ ] Easy/Medium/Hard buttons
   - [ ] Adjust parameters per difficulty
   - [ ] Award bonus points for harder modes

### Week 3
- Friend system
- Daily challenges
- Notifications

### Week 4
- Shareable result cards
- Admin dashboard

See `BRAIN_GAMES_ROADMAP.md` for full details.

---

## TROUBLESHOOTING

### Dark Mode not working?
- [ ] Check `theme.js` is loaded
- [ ] Check Tailwind `darkMode: 'class'` is set
- [ ] Check `<html>` element has `class="dark"` when toggled
- [ ] Open DevTools Console for errors

### Avatar upload fails?
- [ ] Check Firebase Storage rules are correct
- [ ] Check user is authenticated
- [ ] Check image size < 5MB
- [ ] Check DevTools Network tab for 403 errors

### Leaderboards show no data?
- [ ] Check game sessions exist in Firestore
- [ ] Check `gameType` matches (case-sensitive)
- [ ] Check user IDs match between collections
- [ ] Open DevTools Network tab → /api/leaderboards/memory

### Still stuck?
- [ ] Check browser console (DevTools → Console)
- [ ] Check Firebase console logs
- [ ] Review the step in `IMPLEMENTATION_GUIDE.md` again
- [ ] Copy exact code from provided files

---

## SUCCESS INDICATORS

You'll know you're done when:

✅ Users can toggle dark mode  
✅ Users have profile pictures  
✅ Leaderboards show live rankings  
✅ App feels modern & professional  
✅ No broken features  
✅ Mobile works great  

---

## CELEBRATION CHECKLIST

Once you're done, celebrate by:
- [ ] Taking a screenshot of the new leaderboards
- [ ] Sharing with your team
- [ ] Getting feedback from users
- [ ] Planning next features
- [ ] Pushing to production! 🚀

---

## Quick Code Reference

### Log a game session
```javascript
logGameSession('memory', 850, 'hard', 300);
```

### Toggle dark mode
```javascript
window.toggleTheme();
```

### Trigger avatar upload
```javascript
window.triggerAvatarUpload();
```

### Get leaderboard data
```javascript
LeaderboardManager.loadLeaderboard('memory', 'alltime');
```

---

Good luck! You've got this. 💪

Print this page and check off items as you go. It feels great to see progress!

Questions? Check the guide files first — they have detailed answers.

Let's make Brain Games amazing! 🧠✨
