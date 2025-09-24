"use strict";

// Auth state management
var currentUser = null; // DOM elements

var authModal = document.getElementById('auth-modal');
var closeAuthModal = document.getElementById('close-auth-modal');
var googleSigninBtn = document.getElementById('google-signin');
var emailSigninBtn = document.getElementById('email-signin');
var emailInput = document.getElementById('email-input');
var navAuthSection = document.getElementById('nav-auth-section');
var loadingSpinner = document.getElementById('loading-spinner'); // Initialize auth state

document.addEventListener('DOMContentLoaded', function () {
  // Listen for auth state changes
  window.onAuthStateChanged(window.auth, function (user) {
    if (user) {
      handleAuthSuccess(user);
    } else {
      handleAuthSignOut();
    }
  }); // Set up event listeners

  setupEventListeners();
}); // Email Sign-up and Sign-in

document.getElementById('email-signup').addEventListener('click', signUpWithEmail);
document.getElementById('email-signin').addEventListener('click', signInWithEmail);

function setupEventListeners() {
  // Modal controls
  closeAuthModal.addEventListener('click', closeModal);
  authModal.addEventListener('click', function (e) {
    if (e.target === authModal) closeModal();
  }); // Google Sign-in

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

function signInWithGoogle() {
  var provider, result;
  return regeneratorRuntime.async(function signInWithGoogle$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          _context.prev = 0;
          showLoading();
          provider = new window.GoogleAuthProvider();
          _context.next = 5;
          return regeneratorRuntime.awrap(window.signInWithPopup(window.auth, provider));

        case 5:
          result = _context.sent;
          console.log('Google sign-in successful:', result.user);
          _context.next = 13;
          break;

        case 9:
          _context.prev = 9;
          _context.t0 = _context["catch"](0);
          console.error('Google sign-in error:', _context.t0);
          showNotification('Sign-in failed. Please try again.', 'error');

        case 13:
          _context.prev = 13;
          hideLoading();
          return _context.finish(13);

        case 16:
        case "end":
          return _context.stop();
      }
    }
  }, null, null, [[0, 9, 13, 16]]);
}

function sendEmailLink() {
  var email, actionCodeSettings;
  return regeneratorRuntime.async(function sendEmailLink$(_context2) {
    while (1) {
      switch (_context2.prev = _context2.next) {
        case 0:
          email = emailInput.value.trim();

          if (email) {
            _context2.next = 4;
            break;
          }

          showNotification('Please enter your email address.', 'error');
          return _context2.abrupt("return");

        case 4:
          try {
            showLoading();
            actionCodeSettings = {
              url: window.location.origin + '/dashboard',
              handleCodeInApp: true
            }; // Save email for later use

            localStorage.setItem('emailForSignIn', email);
            showNotification('Magic link sent! Check your email.', 'success');
            closeModal();
          } catch (error) {
            console.error('Email link error:', error);
            showNotification('Failed to send magic link. Please try again.', 'error');
          } finally {
            hideLoading();
          }

        case 5:
        case "end":
          return _context2.stop();
      }
    }
  });
}

function handleEmailLinkSignIn() {
  var email, result;
  return regeneratorRuntime.async(function handleEmailLinkSignIn$(_context3) {
    while (1) {
      switch (_context3.prev = _context3.next) {
        case 0:
          _context3.prev = 0;
          showLoading();
          email = localStorage.getItem('emailForSignIn');

          if (!email) {
            email = window.prompt('Please provide your email for confirmation');
          }

          _context3.next = 6;
          return regeneratorRuntime.awrap(window.signInWithEmailLink(window.auth, email, window.location.href));

        case 6:
          result = _context3.sent;
          localStorage.removeItem('emailForSignIn');
          console.log('Email link sign-in successful:', result.user);
          _context3.next = 15;
          break;

        case 11:
          _context3.prev = 11;
          _context3.t0 = _context3["catch"](0);
          console.error('Email link sign-in error:', _context3.t0);
          showNotification('Sign-in failed. Please try again.', 'error');

        case 15:
          _context3.prev = 15;
          hideLoading();
          return _context3.finish(15);

        case 18:
        case "end":
          return _context3.stop();
      }
    }
  }, null, null, [[0, 11, 15, 18]]);
}

function handleAuthSuccess(user) {
  var response;
  return regeneratorRuntime.async(function handleAuthSuccess$(_context4) {
    while (1) {
      switch (_context4.prev = _context4.next) {
        case 0:
          currentUser = user;
          closeModal(); // Send user data to Flask backend

          _context4.prev = 2;
          _context4.next = 5;
          return regeneratorRuntime.awrap(fetch('/api/auth/login', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              user: {
                uid: user.uid,
                email: user.email,
                displayName: user.displayName,
                photoURL: user.photoURL
              }
            })
          }));

        case 5:
          response = _context4.sent;

          if (response.ok) {
            updateNavAuth(user);
            showNotification("Welcome, ".concat(user.displayName || user.email, "!"), 'success'); // Redirect to dashboard if on home page

            if (window.location.pathname === '/') {
              window.location.href = '/dashboard';
            }
          }

          _context4.next = 12;
          break;

        case 9:
          _context4.prev = 9;
          _context4.t0 = _context4["catch"](2);
          console.error('Login API error:', _context4.t0);

        case 12:
        case "end":
          return _context4.stop();
      }
    }
  }, null, null, [[2, 9]]);
}

function handleAuthSignOut() {
  currentUser = null;
  updateNavAuth(null); // Clear Flask session

  fetch('/api/auth/logout', {
    method: 'POST'
  }); // Redirect to home if on protected page

  if (window.location.pathname.startsWith('/dashboard') || window.location.pathname.startsWith('/games')) {
    window.location.href = '/';
  }
}

function updateNavAuth(user) {
  if (user) {
    navAuthSection.innerHTML = "\n            <div class=\"flex items-center space-x-4\">\n                <img src=\"".concat(user.photoURL || '/static/img/default-avatar.png', "\" \n                     alt=\"Profile\" class=\"w-8 h-8 rounded-full\">\n                <span class=\"hidden sm:inline text-gray-700\">").concat(user.displayName || user.email, "</span>\n                <button id=\"sign-out-btn\" class=\"text-gray-500 hover:text-gray-700\">\n                    Sign Out\n                </button>\n            </div>\n        ");
    document.getElementById('sign-out-btn').addEventListener('click', signOut);
  } else {
    navAuthSection.innerHTML = "\n            <button id=\"sign-in-btn\" class=\"bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700\">\n                Sign In\n            </button>\n        ";
    document.getElementById('sign-in-btn').addEventListener('click', showModal);
  }
}

function signOut() {
  return regeneratorRuntime.async(function signOut$(_context5) {
    while (1) {
      switch (_context5.prev = _context5.next) {
        case 0:
          _context5.prev = 0;
          _context5.next = 3;
          return regeneratorRuntime.awrap(window.signOut(window.auth));

        case 3:
          showNotification('Signed out successfully!', 'success');
          _context5.next = 9;
          break;

        case 6:
          _context5.prev = 6;
          _context5.t0 = _context5["catch"](0);
          console.error('Sign out error:', _context5.t0);

        case 9:
        case "end":
          return _context5.stop();
      }
    }
  }, null, null, [[0, 6]]);
}

function showNotification(message) {
  var type = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 'info';
  var notification = document.createElement('div');
  notification.className = "fixed top-4 right-4 z-50 px-4 py-2 rounded-md text-white ".concat(type === 'success' ? 'bg-green-500' : type === 'error' ? 'bg-red-500' : 'bg-blue-500');
  notification.textContent = message;
  document.body.appendChild(notification);
  setTimeout(function () {
    notification.remove();
  }, 4000);
} // Utility functions for games


function requireAuth(callback) {
  if (!currentUser) {
    showNotification('Please sign in to continue.', 'error');
    showModal();
    return false;
  }

  callback();
  return true;
}

function saveGameData(endpoint, data) {
  var response;
  return regeneratorRuntime.async(function saveGameData$(_context6) {
    while (1) {
      switch (_context6.prev = _context6.next) {
        case 0:
          if (currentUser) {
            _context6.next = 2;
            break;
          }

          return _context6.abrupt("return", false);

        case 2:
          _context6.prev = 2;
          _context6.next = 5;
          return regeneratorRuntime.awrap(fetch(endpoint, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
          }));

        case 5:
          response = _context6.sent;
          return _context6.abrupt("return", response.ok);

        case 9:
          _context6.prev = 9;
          _context6.t0 = _context6["catch"](2);
          console.error('Save game data error:', _context6.t0);
          return _context6.abrupt("return", false);

        case 13:
        case "end":
          return _context6.stop();
      }
    }
  }, null, null, [[2, 9]]);
}