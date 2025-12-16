/**
 * Brain Games - Avatar Upload System
 * Handles user profile picture uploads to Firebase Storage
 */

const AvatarManager = {
  STORAGE_PATH: 'avatars',
  MAX_FILE_SIZE: 5 * 1024 * 1024, // 5MB
  ALLOWED_TYPES: ['image/jpeg', 'image/png', 'image/webp', 'image/gif'],

  /**
   * Initialize avatar upload listeners
   */
  init() {
    const input = document.getElementById('avatar-input');
    const dropZone = document.getElementById('avatar-drop-zone');
    
    if (input) {
      input.addEventListener('change', (e) => this.handleFileSelect(e));
    }
    
    if (dropZone) {
      dropZone.addEventListener('dragover', (e) => this.handleDragOver(e));
      dropZone.addEventListener('dragleave', (e) => this.handleDragLeave(e));
      dropZone.addEventListener('drop', (e) => this.handleDrop(e));
    }
  },

  /**
   * Handle file input change
   */
  handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
      this.uploadAvatar(file);
    }
  },

  /**
   * Handle drag over
   */
  handleDragOver(event) {
    event.preventDefault();
    event.stopPropagation();
    event.currentTarget.classList.add('drag-over');
  },

  /**
   * Handle drag leave
   */
  handleDragLeave(event) {
    event.preventDefault();
    event.stopPropagation();
    event.currentTarget.classList.remove('drag-over');
  },

  /**
   * Handle drop
   */
  handleDrop(event) {
    event.preventDefault();
    event.stopPropagation();
    event.currentTarget.classList.remove('drag-over');
    
    const file = event.dataTransfer.files[0];
    if (file) {
      this.uploadAvatar(file);
    }
  },

  /**
   * Validate and upload avatar
   */
  async uploadAvatar(file) {
    // Validation
    if (!this.ALLOWED_TYPES.includes(file.type)) {
      this.showError('Please upload an image (JPG, PNG, WebP, or GIF)');
      return;
    }

    if (file.size > this.MAX_FILE_SIZE) {
      this.showError('Image must be smaller than 5MB');
      return;
    }

    const user = firebase.auth().currentUser;
    if (!user) {
      this.showError('You must be logged in to upload an avatar');
      return;
    }

    this.showLoading(true);

    try {
      // Compress image before upload (optional but recommended)
      const compressedFile = await this.compressImage(file);

      // Upload to Firebase Storage
      const storage = firebase.storage();
      const filename = `${user.uid}-${Date.now()}`;
      const ref = storage.ref(`${this.STORAGE_PATH}/${filename}`);
      
      const snapshot = await ref.put(compressedFile, {
        customMetadata: {
          userId: user.uid
        }
      });

      // Get download URL
      const downloadURL = await snapshot.ref.getDownloadURL();

      // Update Firestore user document
      const db = firebase.firestore();
      await db.collection('users').doc(user.uid).update({
        avatar: downloadURL,
        avatarLastUpdated: firebase.firestore.FieldValue.serverTimestamp()
      });

      // Update UI
      this.updateAvatarDisplay(downloadURL);
      this.showSuccess('Avatar updated successfully!');

    } catch (error) {
      console.error('Avatar upload error:', error);
      this.showError(`Upload failed: ${error.message}`);
    } finally {
      this.showLoading(false);
    }
  },

  /**
   * Compress image using canvas
   */
  async compressImage(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = (event) => {
        const img = new Image();
        img.src = event.target.result;
        img.onload = () => {
          const canvas = document.createElement('canvas');
          let { width, height } = img;

          // Keep aspect ratio, max 800px
          const maxSize = 800;
          if (width > height && width > maxSize) {
            height *= maxSize / width;
            width = maxSize;
          } else if (height > maxSize) {
            width *= maxSize / height;
            height = maxSize;
          }

          canvas.width = width;
          canvas.height = height;

          const ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0, width, height);

          canvas.toBlob(
            (blob) => resolve(blob),
            'image/jpeg',
            0.85 // 85% quality
          );
        };
        img.onerror = () => reject(new Error('Failed to load image'));
      };
      reader.onerror = () => reject(new Error('Failed to read file'));
    });
  },

  /**
   * Update avatar display in UI
   */
  updateAvatarDisplay(url) {
    // Update avatar in navbar
    const navbarAvatar = document.getElementById('navbar-avatar');
    if (navbarAvatar) {
      navbarAvatar.src = url;
    }

    // Update avatar in profile
    const profileAvatar = document.getElementById('profile-avatar');
    if (profileAvatar) {
      profileAvatar.src = url;
    }

    // Update preview if on upload page
    const preview = document.getElementById('avatar-preview');
    if (preview) {
      preview.src = url;
      preview.style.display = 'block';
    }
  },

  /**
   * Show loading state
   */
  showLoading(isLoading) {
    const button = document.getElementById('avatar-upload-btn');
    const spinner = document.getElementById('avatar-spinner');

    if (isLoading) {
      if (button) button.disabled = true;
      if (spinner) spinner.style.display = 'inline-block';
    } else {
      if (button) button.disabled = false;
      if (spinner) spinner.style.display = 'none';
    }
  },

  /**
   * Show success message
   */
  showSuccess(message) {
    this.showNotification(message, 'success');
  },

  /**
   * Show error message
   */
  showError(message) {
    this.showNotification(message, 'error');
  },

  /**
   * Show notification toast
   */
  showNotification(message, type = 'info') {
    // Create toast element
    const toast = document.createElement('div');
    toast.className = `fixed bottom-4 right-4 px-4 py-3 rounded-lg text-white z-50 animate-slide-in ${
      type === 'success' ? 'bg-green-500' :
      type === 'error' ? 'bg-red-500' :
      'bg-blue-500'
    }`;
    toast.textContent = message;

    document.body.appendChild(toast);

    // Auto-remove after 4 seconds
    setTimeout(() => {
      toast.style.animation = 'fade-out 0.3s ease-out';
      setTimeout(() => toast.remove(), 300);
    }, 4000);
  }
};

// Initialize when page loads
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => AvatarManager.init());
} else {
  AvatarManager.init();
}

// Expose to global scope
window.triggerAvatarUpload = () => {
  document.getElementById('avatar-input').click();
};
