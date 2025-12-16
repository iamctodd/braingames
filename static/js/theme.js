/**
 * Brain Games - Theme System
 * Handles light/dark mode toggle with Firebase persistence
 */

const ThemeManager = {
  LIGHT: 'light',
  DARK: 'dark',
  STORAGE_KEY: 'braingames_theme',

  /**
   * Initialize theme on page load
   */
  init() {
    // Check user preference in Firestore, then localStorage, then system preference
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        // Logged in: get preference from Firestore
        this.loadFromFirestore(user.uid);
      } else {
        // Not logged in: use localStorage or system preference
        this.loadFromLocalStorage();
      }
    });
  },

  /**
   * Load theme from Firestore (logged-in users)
   */
  loadFromFirestore(userId) {
    const db = firebase.firestore();
    db.collection('users').doc(userId).get().then((doc) => {
      if (doc.exists && doc.data().theme) {
        this.setTheme(doc.data().theme, false);
      } else {
        // Fallback to system preference
        this.loadFromLocalStorage();
      }
    }).catch(() => {
      // If Firestore fails, use localStorage
      this.loadFromLocalStorage();
    });
  },

  /**
   * Load theme from localStorage or system preference
   */
  loadFromLocalStorage() {
    const saved = localStorage.getItem(this.STORAGE_KEY);
    
    if (saved) {
      this.setTheme(saved, false);
    } else {
      // Check system preference
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      this.setTheme(prefersDark ? this.DARK : this.LIGHT, false);
    }
  },

  /**
   * Set theme and persist
   */
  setTheme(theme, persist = true) {
    const html = document.documentElement;
    
    if (theme === this.DARK) {
      html.classList.add('dark');
      html.setAttribute('data-theme', 'dark');
    } else {
      html.classList.remove('dark');
      html.setAttribute('data-theme', 'light');
    }

    // Update toggle button if it exists
    this.updateToggleButton(theme);

    // Persist preference
    if (persist) {
      localStorage.setItem(this.STORAGE_KEY, theme);
      
      // Save to Firestore if user is logged in
      const user = firebase.auth().currentUser;
      if (user) {
        const db = firebase.firestore();
        db.collection('users').doc(user.uid).update({ theme })
          .catch((error) => console.warn('Could not save theme preference:', error));
      }
    }
  },

  /**
   * Toggle between light and dark
   */
  toggle() {
    const current = document.documentElement.classList.contains('dark')
      ? this.DARK
      : this.LIGHT;
    const next = current === this.DARK ? this.LIGHT : this.DARK;
    this.setTheme(next, true);
  },

  /**
   * Update toggle button appearance
   */
  updateToggleButton(theme) {
    const toggle = document.getElementById('theme-toggle');
    if (toggle) {
      toggle.setAttribute('data-theme', theme);
      // Update icon text/aria-label as needed
      toggle.setAttribute('aria-label', 
        `Switch to ${theme === this.DARK ? 'light' : 'dark'} mode`
      );
    }
  },

  /**
   * Get current theme
   */
  getCurrent() {
    return document.documentElement.classList.contains('dark')
      ? this.DARK
      : this.LIGHT;
  }
};

// Initialize on DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => ThemeManager.init());
} else {
  ThemeManager.init();
}

// Expose to global scope for HTML onclick handlers
window.toggleTheme = () => ThemeManager.toggle();
