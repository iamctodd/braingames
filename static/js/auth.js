// Auth state management
let currentUser = null;

// DOM elements
const authModal = document.getElementById('auth-modal');
const closeAuthModal = document.getElementById('close-auth-modal');
const googleSigninBtn = document.getElementById('google-signin');
const emailSigninBtn = document.getElementById('email-signin');
const emailInput = document.getElementById('email-input');
const navAuthSection = document.getElementById('nav-auth-section');
const loadingSpinner = document.getElementById('loading-spinner');

// Initialize auth state
document.addEventListener('DOMContentLoaded', () => {
    // Check for email link sign-in
    if (window.isSignInWithEmailLink && window.isSignInWithEmailLink(window.auth, window.location.href)) {
        handleEmailLinkSignIn();
    }

    // Listen for auth state changes
    window.onAuthStateChanged(window.auth, (user) => {
        if (user) {
            handleAuthSuccess(user);
        } else {
            handleAuthSignOut();
        }
    });

    // Set up event listeners
    setupEventListeners();
});

function setupEventListeners() {
    // Modal controls
    closeAuthModal.addEventListener('click', closeModal);
    authModal.addEventListener('click', (e) => {
        if (e.target === authModal) closeModal();
    });

    // Google Sign-in
    googleSigninBtn.addEventListener('click', signInWithGoogle);

    // Email Sign-up and Sign-in
    document.getElementById('email-signup').addEventListener('click', signUpWithEmail);
    document.getElementById('email-signin').addEventListener('click', signInWithEmail);
    
    // Enter key handlers
    document.getElementById('password-input').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') signUpWithEmail();
    });
    emailInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') signUpWithEmail();
    });
}

function showModal() {
    authModal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    authModal.classList.add('hidden');
    document.body.style.overflow = 'auto';
}

function showLoading() {
    loadingSpinner.classList.remove('hidden');
}

function hideLoading() {
    loadingSpinner.classList.add('hidden');
}

async function signInWithGoogle() {
    try {
        showLoading();
        const provider = new window.GoogleAuthProvider();
        const result = await window.signInWithPopup(window.auth, provider);
        console.log('Google sign-in successful:', result.user);
    } catch (error) {
        console.error('Google sign-in error:', error);
        showNotification('Sign-in failed. Please try again.', 'error');
    } finally {
        hideLoading();
    }
}

async function signUpWithEmail() {
    const email = emailInput.value.trim();
    const password = document.getElementById('password-input').value;
    
    if (!email || !password) {
        showNotification('Please enter both email and password.', 'error');
        return;
    }
    
    if (password.length < 6) {
        showNotification('Password must be at least 6 characters.', 'error');
        return;
    }

    try {
        showLoading();
        const result = await window.createUserWithEmailAndPassword(window.auth, email, password);
        console.log('Email sign-up successful:', result.user);
        showNotification('Account created successfully!', 'success');
    } catch (error) {
        console.error('Email sign-up error:', error);
        let message = 'Sign-up failed. Please try again.';
        if (error.code === 'auth/email-already-in-use') {
            message = 'Email already in use. Try signing in instead.';
        } else if (error.code === 'auth/weak-password') {
            message = 'Password is too weak. Please choose a stronger password.';
        } else if (error.code === 'auth/invalid-email') {
            message = 'Invalid email address.';
        }
        showNotification(message, 'error');
    } finally {
        hideLoading();
    }
}

async function signInWithEmail() {
    const email = emailInput.value.trim();
    const password = document.getElementById('password-input').value;
    
    if (!email || !password) {
        showNotification('Please enter both email and password.', 'error');
        return;
    }

    try {
        showLoading();
        const result = await window.signInWithEmailAndPassword(window.auth, email, password);
        console.log('Email sign-in successful:', result.user);
        showNotification('Welcome back!', 'success');
    } catch (error) {
        console.error('Email sign-in error:', error);
        let message = 'Sign-in failed. Please check your credentials.';
        if (error.code === 'auth/user-not-found') {
            message = 'No account found. Try signing up first.';
        } else if (error.code === 'auth/wrong-password') {
            message = 'Incorrect password.';
        } else if (error.code === 'auth/invalid-email') {
            message = 'Invalid email address.';
        }
        showNotification(message, 'error');
    } finally {
        hideLoading();
    }
}

// Remove magic link functions for now - focus on working auth
// async function sendEmailLink() { ... }
// function showMagicLinkMode() { ... }
}

async function handleEmailLinkSignIn() {
    try {
        showLoading();
        let email = localStorage.getItem('emailForSignIn');
        
        if (!email) {
            email = window.prompt('Please provide your email for confirmation');
        }

        const result = await window.signInWithEmailLink(window.auth, email, window.location.href);
        localStorage.removeItem('emailForSignIn');
        
        console.log('Email link sign-in successful:', result.user);
    } catch (error) {
        console.error('Email link sign-in error:', error);
        showNotification('Sign-in failed. Please try again.', 'error');
    } finally {
        hideLoading();
    }
}

async function handleAuthSuccess(user) {
    currentUser = user;
    closeModal();
    
    // Send user data to Flask backend
    try {
        const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user: {
                    uid: user.uid,
                    email: user.email,
                    displayName: user.displayName,
                    photoURL: user.photoURL
                }
            })
        });
        
        if (response.ok) {
            updateNavAuth(user);
            showNotification(`Welcome, ${user.displayName || user.email}!`, 'success');
            
            // Redirect to dashboard if on home page
            if (window.location.pathname === '/') {
                window.location.href = '/dashboard';
            }
        }
    } catch (error) {
        console.error('Login API error:', error);
    }
}

function handleAuthSignOut() {
    currentUser = null;
    updateNavAuth(null);
    
    // Clear Flask session
    fetch('/api/auth/logout', { method: 'POST' });
    
    // Redirect to home if on protected page
    if (window.location.pathname.startsWith('/dashboard') || window.location.pathname.startsWith('/games')) {
        window.location.href = '/';
    }
}

function updateNavAuth(user) {
    if (user) {
        navAuthSection.innerHTML = `
            <div class="flex items-center space-x-4">
                <img src="${user.photoURL || '/static/img/default-avatar.png'}" 
                     alt="Profile" class="w-8 h-8 rounded-full">
                <span class="hidden sm:inline text-gray-700">${user.displayName || user.email}</span>
                <button id="sign-out-btn" class="text-gray-500 hover:text-gray-700">
                    Sign Out
                </button>
            </div>
        `;
        
        document.getElementById('sign-out-btn').addEventListener('click', signOut);
    } else {
        navAuthSection.innerHTML = `
            <button id="sign-in-btn" class="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                Sign In
            </button>
        `;
        
        document.getElementById('sign-in-btn').addEventListener('click', showModal);
    }
}

async function signOut() {
    try {
        await window.signOut(window.auth);
        showNotification('Signed out successfully!', 'success');
    } catch (error) {
        console.error('Sign out error:', error);
    }
}

function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `fixed top-4 right-4 z-50 px-4 py-2 rounded-md text-white ${
        type === 'success' ? 'bg-green-500' : 
        type === 'error' ? 'bg-red-500' : 
        'bg-blue-500'
    }`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 4000);
}

// Utility functions for games
function requireAuth(callback) {
    if (!currentUser) {
        showNotification('Please sign in to continue.', 'error');
        showModal();
        return false;
    }
    callback();
    return true;
}

async function saveGameData(endpoint, data) {
    if (!currentUser) return false;
    
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        return response.ok;
    } catch (error) {
        console.error('Save game data error:', error);
        return false;
    }
}

// Global activity tracking function
function addActivity(userId, type, title, description) {
    const activities = JSON.parse(localStorage.getItem(`activities_${userId}`) || '[]');
    const newActivity = {
        icon: getActivityIcon(type),
        title: title,
        description: description,
        time: 'Just now',
        type: type,
        timestamp: Date.now()
    };
    
    // Add to beginning of array
    activities.unshift(newActivity);
    
    // Keep only last 10 activities
    const recentActivities = activities.slice(0, 10);
    
    // Update timestamps to be relative
    updateActivityTimes(recentActivities);
    
    localStorage.setItem(`activities_${userId}`, JSON.stringify(recentActivities));
    
    // If we're on the dashboard, refresh the activity display
    if (window.location.pathname === '/dashboard') {
        setTimeout(() => {
            if (typeof loadRecentActivity === 'function') {
                loadRecentActivity(userId);
            }
        }, 100);
    }
}

function getActivityIcon(type) {
    const icons = {
        'memory': '🧩',
        'problem-solving': '💡',
        'tbi-memory': '🎯',
        'achievement': '🏆',
        'progress': '📈',
        'game': '🎮',
        'case': '📝',
        'exercise': '🔄'
    };
    return icons[type] || '🎯';
}

function updateActivityTimes(activities) {
    const now = Date.now();
    activities.forEach(activity => {
        const timeDiff = now - (activity.timestamp || now);
        const minutes = Math.floor(timeDiff / 60000);
        const hours = Math.floor(minutes / 60);
        const days = Math.floor(hours / 24);
        
        if (minutes < 1) {
            activity.time = 'Just now';
        } else if (minutes < 60) {
            activity.time = `${minutes} minute${minutes !== 1 ? 's' : ''} ago`;
        } else if (hours < 24) {
            activity.time = `${hours} hour${hours !== 1 ? 's' : ''} ago`;
        } else {
            activity.time = `${days} day${days !== 1 ? 's' : ''} ago`;
        }
    });
}