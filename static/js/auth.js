// Auth state management
let currentUser = null;

// DOM elements
const authModal = document.getElementById('auth-modal');
const closeAuthModal = document.getElementById('close-auth-modal');
const googleSigninBtn = document.getElementById('google-signin');
const emailSignupBtn = document.getElementById('email-signup');
const emailSigninBtn = document.getElementById('email-signin');
const emailInput = document.getElementById('email-input');
const passwordInput = document.getElementById('password-input');
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
    if (closeAuthModal) {
        closeAuthModal.addEventListener('click', closeModal);
    }
    if (authModal) {
        authModal.addEventListener('click', (e) => {
            if (e.target === authModal) closeModal();
        });
    }

    // Authentication buttons
    if (googleSigninBtn) {
        googleSigninBtn.addEventListener('click', signInWithGoogle);
    }
    if (emailSignupBtn) {
        emailSignupBtn.addEventListener('click', signUpWithEmail);
    }
    if (emailSigninBtn) {
        emailSigninBtn.addEventListener('click', signInWithEmail);
    }

    // Enter key handlers
    if (passwordInput) {
        passwordInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') signUpWithEmail();
        });
    }
    if (emailInput) {
        emailInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') signUpWithEmail();
        });
    }
}

function showModal() {
    if (authModal) {
        authModal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }
}

function closeModal() {
    if (authModal) {
        authModal.classList.add('hidden');
        document.body.style.overflow = 'auto';
    }
}

function showLoading() {
    if (loadingSpinner) {
        loadingSpinner.classList.remove('hidden');
    }
}

function hideLoading() {
    if (loadingSpinner) {
        loadingSpinner.classList.add('hidden');
    }
}

async function signInWithGoogle() {
    try {
        showLoading();
        const provider = new window.GoogleAuthProvider();
        const result = await window.signInWithPopup(window.auth, provider);
        console.log('Google sign-in successful:', result.user);
        showNotification('Welcome!', 'success');
    } catch (error) {
        console.error('Google sign-in error:', error);
        let message = 'Google sign-in failed. ';
        if (error.code === 'auth/popup-blocked') {
            message += 'Please allow popups and try again.';
        } else if (error.code === 'auth/unauthorized-domain') {
            message += 'This domain is not authorized.';
        } else {
            message += 'Please try again.';
        }
        showNotification(message, 'error');
    } finally {
        hideLoading();
    }
}

async function signUpWithEmail() {
    const email = emailInput ? emailInput.value.trim() : '';
    const password = passwordInput ? passwordInput.value : '';
    
    console.log('Sign up attempt with:', email);
    
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
        console.log('Creating user with Firebase...');
        const result = await window.createUserWithEmailAndPassword(window.auth, email, password);
        console.log('Email sign-up successful:', result.user);
        showNotification('Account created successfully!', 'success');
    } catch (error) {
        console.error('Email sign-up error:', error);
        let message = 'Sign-up failed. ';
        if (error.code === 'auth/email-already-in-use') {
            message += 'Email already in use. Try signing in instead.';
        } else if (error.code === 'auth/weak-password') {
            message += 'Password is too weak. Please choose a stronger password.';
        } else if (error.code === 'auth/invalid-email') {
            message += 'Invalid email address.';
        } else {
            message += 'Please try again. Error: ' + error.message;
        }
        showNotification(message, 'error');
    } finally {
        hideLoading();
    }
}

async function signInWithEmail() {
    const email = emailInput ? emailInput.value.trim() : '';
    const password = passwordInput ? passwordInput.value : '';
    
    console.log('Sign in attempt with:', email);
    
    if (!email || !password) {
        showNotification('Please enter both email and password.', 'error');
        return;
    }

    try {
        showLoading();
        console.log('Signing in with Firebase...');
        const result = await window.signInWithEmailAndPassword(window.auth, email, password);
        console.log('Email sign-in successful:', result.user);
        showNotification('Welcome back!', 'success');
    } catch (error) {
        console.error('Email sign-in error:', error);
        let message = 'Sign-in failed. ';
        if (error.code === 'auth/user-not-found') {
            message += 'No account found. Try signing up first.';
        } else if (error.code === 'auth/wrong-password') {
            message += 'Incorrect password.';
        } else if (error.code === 'auth/invalid-email') {
            message += 'Invalid email address.';
        } else {
            message += 'Please check your credentials. Error: ' + error.message;
        }
        showNotification(message, 'error');
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
    if (!navAuthSection) return;
    
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
        
        const signOutBtn = document.getElementById('sign-out-btn');
        if (signOutBtn) {
            signOutBtn.addEventListener('click', signOut);
        }
    } else {
        navAuthSection.innerHTML = `
            <button id="sign-in-btn" class="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                Sign In
            </button>
        `;
        
        const signInBtn = document.getElementById('sign-in-btn');
        if (signInBtn) {
            signInBtn.addEventListener('click', showModal);
        }
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