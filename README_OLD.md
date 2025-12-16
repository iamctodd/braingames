# Brain Games App - Flask + Firebase Setup

A unified brain training platform combining Memory Training, Problem Solving, and TBI Memory games with secure Firebase authentication.

## Quick Setup

### 1. Firebase Configuration

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project or use existing one
3. Enable Authentication:
   - Go to Authentication > Sign-in method
   - Enable Google and Email/Password providers
   - For passwordless: Enable Email link (passwordless sign-in)
4. Get your Firebase config:
   - Go to Project Settings > General > Your apps
   - Add a web app and copy the config object

### 2. Update Firebase Config

Replace the placeholder config in `templates/base.html`:

```javascript
const firebaseConfig = {
    apiKey: "your-actual-api-key",
    authDomain: "your-project.firebaseapp.com",
    projectId: "your-project-id",
    storageBucket: "your-project.appspot.com",
    messagingSenderId: "123456789",
    appId: "your-app-id"
};
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Project Structure

Create this folder structure:

```
brain-games-app/
├── app.py
├── requirements.txt
├── static/
│   ├── js/
│   │   └── auth.js
│   └── img/
│       └── default-avatar.png
└── templates/
    ├── base.html
    ├── index.html
    ├── dashboard.html
    └── games/
        ├── memory.html
        ├── problem_solving.html
        └── tbi_memory.html
```

### 5. Run the App

```bash
python app.py
```

Visit `http://localhost:5000`

## Features

### ✅ Authentication
- Google Sign-in
- Passwordless email links
- Apple Sign-in ready (needs Apple Developer setup)
- Secure session management

### ✅ Games Included
- **Memory Training**: Pattern sequence memorization
- **Problem Solving**: Real-world case studies (template ready)
- **TBI Memory**: Specialized exercises (template ready)

### ✅ User Experience
- Mobile-responsive design with Tailwind CSS
- Progress tracking and statistics
- Unified dashboard
- Secure data persistence

## Integrating Your Existing Games

### Memory Game
The template includes a fully functional memory game. You can:
1. Customize difficulty levels
2. Add new pattern types
3. Modify scoring system

### Problem Solving Game
Create `templates/games/problem_solving.html` with your case studies:

```html
{% extends "base.html" %}
{% block content %}
<!-- Your existing case study content here -->
{% endblock %}
```

### TBI Memory Game  
Create `templates/games/tbi_memory.html` with your specialized exercises:

```html
{% extends "base.html" %}
{% block content %}
<!-- Your existing TBI memory exercises here -->
{% endblock %}
```

## Deployment Options

### Option 1: Render (Free Tier)
1. Connect your GitHub repo to Render
2. Set environment variables in Render dashboard
3. Deploy automatically on git push

### Option 2: Heroku
```bash
# Add Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy to Heroku
git init
git add .
git commit -m "Initial commit"
heroku create your-app-name
git push heroku main
```

### Option 3: Netlify + Serverless
Convert to static site with API functions for backend features.

## Security Best Practices

### Production Checklist
- [ ] Change `app.secret_key` to a secure random string
- [ ] Set up proper Firebase security rules
- [ ] Enable HTTPS/SSL certificates
- [ ] Implement rate limiting
- [ ] Add input validation
- [ ] Set up error logging
- [ ] Configure CORS properly
- [ ] Use environment variables for secrets

### Environment Variables
Create a `.env` file:
```
FLASK_SECRET_KEY=your-super-secure-secret-key
FIREBASE_SERVICE_ACCOUNT=path-to-service-account.json
DATABASE_URL=your-database-url
```

Load in `app.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()
app.secret_key = os.getenv('FLASK_SECRET_KEY')
```

## Database Integration

### Option 1: Firebase Firestore
```python
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin
cred = credentials.Certificate('path-to-service-account.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Save user data
def save_user_score(user_id, game_type, score):
    doc_ref = db.collection('users').document(user_id)
    doc_ref.collection('scores').add({
        'game_type': game_type,
        'score': score,
        'timestamp': firestore.SERVER_TIMESTAMP
    })
```

### Option 2: PostgreSQL/SQLite
```python
import sqlite3

def init_db():
    conn = sqlite3.connect('brain_games.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS user_scores (
            id INTEGER PRIMARY KEY,
            user_id TEXT NOT NULL,
            game_type TEXT NOT NULL,
            score INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.close()
```

## API Endpoints

### Game Data Endpoints
- `POST /api/games/memory/score` - Save memory game score
- `POST /api/games/problem-solving/response` - Save case study response  
- `POST /api/games/tbi-memory/progress` - Save TBI memory progress
- `GET /api/games/stats` - Get user statistics
- `GET /api/games/leaderboard` - Get leaderboard data

### User Management
- `POST /api/auth/login` - Handle Firebase auth
- `POST /api/auth/logout` - Clear session
- `GET /api/auth/user` - Get current user
- `GET /api/user/profile` - Get user profile
- `PUT /api/user/profile` - Update user profile

## Customization Guide

### Styling with Tailwind
The template uses Tailwind CSS via CDN. For custom styling:

1. **Colors**: Modify the color scheme in `base.html`
2. **Components**: Create reusable component classes
3. **Responsive**: Use Tailwind's responsive prefixes (sm:, md:, lg:)
4. **Dark Mode**: Add dark mode support with `dark:` classes

### Adding New Games
1. Create new HTML template in `templates/games/`
2. Add route in `app.py`:
```python
@app.route('/games/your-new-game')
def your_new_game():
    return render_template('games/your_new_game.html')
```
3. Add game card to dashboard
4. Implement scoring/progress APIs

### Analytics Integration
Add Google Analytics, Mixpanel, or custom analytics:

```html
<!-- In base.html head -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## Troubleshooting

### Common Issues

1. **Firebase Config Errors**: Ensure all config values are correct
2. **CORS Issues**: Add proper CORS headers for API calls
3. **Mobile Responsive**: Test on actual devices, not just browser dev tools
4. **Session Issues**: Check Flask secret key and session configuration

### Debug Mode
```python
# In app.py for development only
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Logging
```python
import logging
logging.basicConfig(level=logging.INFO)
app.logger.info('Application started')
```

## Performance Optimization

### Frontend
- Minimize JavaScript bundle size
- Use lazy loading for game assets
- Implement service worker for offline play
- Optimize images and use WebP format

### Backend  
- Implement caching with Redis
- Use database connection pooling
- Add request rate limiting
- Optimize database queries

## Next Steps

1. **Test the basic setup** with memory game
2. **Integrate your existing games** into the templates
3. **Set up production database** (Firebase/PostgreSQL)
4. **Deploy to your preferred platform**
5. **Add analytics and monitoring**
6. **Implement user feedback system**
7. **Add social features** (sharing scores, challenges)

## Support

For issues with this template:
1. Check Firebase console for auth errors
2. Verify all environment variables are set
3. Test with browser developer tools
4. Check Flask logs for backend errors

The template is designed to be modular - you can start with basic auth and one game, then gradually add features and integrate your existing games.