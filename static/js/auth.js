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

async function sendEmailLink() {
    const email = emailInput.value.trim();
    if (!email) {
        showNotification('Please enter your email address.', 'error');
        return;
    }

    try {
        showLoading();
        const actionCodeSettings = {
            url: window.location.origin + '/dashboard',
            handleCodeInApp: true,
        };        
        // Save email for later use
        localStorage.setItem('emailForSignIn', email);
        
        showNotification('Magic link sent! Check your email.', 'success');
        closeModal();
    } catch (error) {
        console.error('Email link error:', error);
        showNotification('Failed to send magic link. Please try again.', 'error');
    } finally {
        hideLoading();
    }
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