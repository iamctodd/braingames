"use strict";

// Auth state management
var currentUser = null; // DOM elements

var authModal = document.getElementById('auth-modal');
var closeAuthModal = document.getElementById('close-auth-modal');
var googleSigninBtn = document.getElementById('google-signin');
var emailSignupBtn = document.getElementById('email-signup');
var emailSigninBtn = document.getElementById('email-signin');
var emailInput = document.getElementById('email-input');
var passwordInput = document.getElementById('password-input');
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
});

function setupEventListeners() {
  // Modal controls
  if (closeAuthModal) {
    closeAuthModal.addEventListener('click', closeModal);
  }

  if (authModal) {
    authModal.addEventListener('click', function (e) {
      if (e.target === authModal) closeModal();
    });
  } // Authentication buttons


  if (googleSigninBtn) {
    googleSigninBtn.addEventListener('click', signInWithGoogle);
  }

  if (emailSignupBtn) {
    emailSignupBtn.addEventListener('click', signUpWithEmail);
  }

  if (emailSigninBtn) {
    emailSigninBtn.addEventListener('click', signInWithEmail);
  } // Enter key handlers


  if (passwordInput) {
    passwordInput.addEventListener('keypress', function (e) {
      if (e.key === 'Enter') signUpWithEmail();
    });
  }

  if (emailInput) {
    emailInput.addEventListener('keypress', function (e) {
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

function signInWithGoogle() {
  var provider, result, message;
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
          showNotification('Welcome!', 'success');
          _context.next = 16;
          break;

        case 10:
          _context.prev = 10;
          _context.t0 = _context["catch"](0);
          console.error('Google sign-in error:', _context.t0);
          message = 'Google sign-in failed. ';

          if (_context.t0.code === 'auth/popup-blocked') {
            message += 'Please allow popups and try again.';
          } else if (_context.t0.code === 'auth/unauthorized-domain') {
            message += 'This domain is not authorized.';
          } else {
            message += 'Please try again.';
          }

          showNotification(message, 'error');

        case 16:
          _context.prev = 16;
          hideLoading();
          return _context.finish(16);

        case 19:
        case "end":
          return _context.stop();
      }
    }
  }, null, null, [[0, 10, 16, 19]]);
}

function signUpWithEmail() {
  var email, password, result, message;
  return regeneratorRuntime.async(function signUpWithEmail$(_context2) {
    while (1) {
      switch (_context2.prev = _context2.next) {
        case 0:
          email = emailInput ? emailInput.value.trim() : '';
          password = passwordInput ? passwordInput.value : '';
          console.log('Sign up attempt with:', email);

          if (!(!email || !password)) {
            _context2.next = 6;
            break;
          }

          showNotification('Please enter both email and password.', 'error');
          return _context2.abrupt("return");

        case 6:
          if (!(password.length < 6)) {
            _context2.next = 9;
            break;
          }

          showNotification('Password must be at least 6 characters.', 'error');
          return _context2.abrupt("return");

        case 9:
          _context2.prev = 9;
          showLoading();
          console.log('Creating user with Firebase...');
          _context2.next = 14;
          return regeneratorRuntime.awrap(window.createUserWithEmailAndPassword(window.auth, email, password));

        case 14:
          result = _context2.sent;
          console.log('Email sign-up successful:', result.user);
          showNotification('Account created successfully!', 'success');
          _context2.next = 25;
          break;

        case 19:
          _context2.prev = 19;
          _context2.t0 = _context2["catch"](9);
          console.error('Email sign-up error:', _context2.t0);
          message = 'Sign-up failed. ';

          if (_context2.t0.code === 'auth/email-already-in-use') {
            message += 'Email already in use. Try signing in instead.';
          } else if (_context2.t0.code === 'auth/weak-password') {
            message += 'Password is too weak. Please choose a stronger password.';
          } else if (_context2.t0.code === 'auth/invalid-email') {
            message += 'Invalid email address.';
          } else {
            message += 'Please try again. Error: ' + _context2.t0.message;
          }

          showNotification(message, 'error');

        case 25:
          _context2.prev = 25;
          hideLoading();
          return _context2.finish(25);

        case 28:
        case "end":
          return _context2.stop();
      }
    }
  }, null, null, [[9, 19, 25, 28]]);
}

function signInWithEmail() {
  var email, password, result, message;
  return regeneratorRuntime.async(function signInWithEmail$(_context3) {
    while (1) {
      switch (_context3.prev = _context3.next) {
        case 0:
          email = emailInput ? emailInput.value.trim() : '';
          password = passwordInput ? passwordInput.value : '';
          console.log('Sign in attempt with:', email);

          if (!(!email || !password)) {
            _context3.next = 6;
            break;
          }

          showNotification('Please enter both email and password.', 'error');
          return _context3.abrupt("return");

        case 6:
          _context3.prev = 6;
          showLoading();
          console.log('Signing in with Firebase...');
          _context3.next = 11;
          return regeneratorRuntime.awrap(window.signInWithEmailAndPassword(window.auth, email, password));

        case 11:
          result = _context3.sent;
          console.log('Email sign-in successful:', result.user);
          showNotification('Welcome back!', 'success');
          _context3.next = 22;
          break;

        case 16:
          _context3.prev = 16;
          _context3.t0 = _context3["catch"](6);
          console.error('Email sign-in error:', _context3.t0);
          message = 'Sign-in failed. ';

          if (_context3.t0.code === 'auth/user-not-found') {
            message += 'No account found. Try signing up first.';
          } else if (_context3.t0.code === 'auth/wrong-password') {
            message += 'Incorrect password.';
          } else if (_context3.t0.code === 'auth/invalid-email') {
            message += 'Invalid email address.';
          } else {
            message += 'Please check your credentials. Error: ' + _context3.t0.message;
          }

          showNotification(message, 'error');

        case 22:
          _context3.prev = 22;
          hideLoading();
          return _context3.finish(22);

        case 25:
        case "end":
          return _context3.stop();
      }
    }
  }, null, null, [[6, 16, 22, 25]]);
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
  if (!navAuthSection) return;

  if (user) {
    navAuthSection.innerHTML = "\n            <div class=\"flex items-center space-x-4\">\n                <img src=\"".concat(user.photoURL || '/static/img/default-avatar.png', "\" \n                     alt=\"Profile\" class=\"w-8 h-8 rounded-full\">\n                <span class=\"hidden sm:inline text-gray-700\">").concat(user.displayName || user.email, "</span>\n                <button id=\"sign-out-btn\" class=\"text-gray-500 hover:text-gray-700\">\n                    Sign Out\n                </button>\n            </div>\n        ");
    var signOutBtn = document.getElementById('sign-out-btn');

    if (signOutBtn) {
      signOutBtn.addEventListener('click', signOut);
    }
  } else {
    navAuthSection.innerHTML = "\n            <button id=\"sign-in-btn\" class=\"bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700\">\n                Sign In\n            </button>\n        ";
    var signInBtn = document.getElementById('sign-in-btn');

    if (signInBtn) {
      signInBtn.addEventListener('click', showModal);
    }
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