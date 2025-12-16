/**
 * Brain Games - Leaderboards System
 * Displays global rankings by game type with various filters
 */

const LeaderboardManager = {
  GAMES: {
    memory: 'Memory Training',
    problem_solving: 'Problem Solving',
    tbi_memory: 'TBI Memory'
  },
  
  TIMEFRAMES: {
    alltime: { label: 'All Time', days: null },
    month: { label: 'This Month', days: 30 },
    week: { label: 'This Week', days: 7 }
  },

  /**
   * Initialize leaderboard page
   */
  init() {
    this.setupEventListeners();
    this.loadLeaderboard('memory', 'alltime');
  },

  /**
   * Setup UI event listeners
   */
  setupEventListeners() {
    // Game type buttons
    document.querySelectorAll('[data-game-type]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const gameType = e.target.dataset.gameType;
        const timeframe = this.getCurrentTimeframe();
        this.loadLeaderboard(gameType, timeframe);
        this.updateActiveTab(gameType);
      });
    });

    // Timeframe buttons
    document.querySelectorAll('[data-timeframe]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const timeframe = e.target.dataset.timeframe;
        const gameType = this.getCurrentGameType();
        this.loadLeaderboard(gameType, timeframe);
        this.updateActiveTimeframeTab(timeframe);
      });
    });
  },

  /**
   * Get current selected game type
   */
  getCurrentGameType() {
    const active = document.querySelector('[data-game-type].active');
    return active ? active.dataset.gameType : 'memory';
  },

  /**
   * Get current selected timeframe
   */
  getCurrentTimeframe() {
    const active = document.querySelector('[data-timeframe].active');
    return active ? active.dataset.timeframe : 'alltime';
  },

  /**
   * Update active game type tab
   */
  updateActiveTab(gameType) {
    document.querySelectorAll('[data-game-type]').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.gameType === gameType);
    });
  },

  /**
   * Update active timeframe tab
   */
  updateActiveTimeframeTab(timeframe) {
    document.querySelectorAll('[data-timeframe]').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.timeframe === timeframe);
    });
  },

  /**
   * Load leaderboard data from Firestore
   */
  async loadLeaderboard(gameType, timeframe) {
    this.showLoading(true);

    try {
      const db = firebase.firestore();
      const user = firebase.auth().currentUser;
      let userRank = null;
      let userScore = null;

      // Build query based on game type
      let query = db.collection('game_sessions')
        .where('gameType', '==', gameType)
        .orderBy('score', 'desc')
        .limit(100); // Get top 100 to find user

      // Apply timeframe filter
      if (this.TIMEFRAMES[timeframe].days) {
        const daysAgo = new Date();
        daysAgo.setDate(daysAgo.getDate() - this.TIMEFRAMES[timeframe].days);
        query = query.where('timestamp', '>=', daysAgo);
      }

      // Get top scores
      const snapshot = await query.get();
      const topScores = [];
      let rank = 1;

      snapshot.forEach((doc) => {
        const data = doc.data();
        // Group by user and get their best score
        if (!topScores.find(s => s.userId === data.userId)) {
          topScores.push({
            userId: data.userId,
            score: data.score,
            difficulty: data.difficulty,
            timestamp: data.timestamp,
            rank: rank++
          });
        }

        // Check if it's current user
        if (user && data.userId === user.uid) {
          userScore = data.score;
        }
      });

      // Get top 10 with user details
      const top10 = topScores.slice(0, 10);
      const leaderboardWithUsers = await this.enrichWithUserData(top10);

      // Find user's rank and percentile
      if (user) {
        userRank = topScores.findIndex(s => s.userId === user.uid) + 1;
      }

      // Render leaderboard
      this.render(leaderboardWithUsers, userRank, userScore, gameType, timeframe);

    } catch (error) {
      console.error('Leaderboard error:', error);
      this.showError('Failed to load leaderboard');
    } finally {
      this.showLoading(false);
    }
  },

  /**
   * Enrich leaderboard data with user information
   */
  async enrichWithUserData(entries) {
    const db = firebase.firestore();
    const enriched = [];

    for (const entry of entries) {
      try {
        const userDoc = await db.collection('users').doc(entry.userId).get();
        const userData = userDoc.data() || {};

        enriched.push({
          ...entry,
          displayName: userData.displayName || 'Anonymous',
          avatar: userData.avatar || this.getDefaultAvatar()
        });
      } catch (error) {
        enriched.push({
          ...entry,
          displayName: 'Anonymous',
          avatar: this.getDefaultAvatar()
        });
      }
    }

    return enriched;
  },

  /**
   * Get default avatar URL
   */
  getDefaultAvatar() {
    return 'data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 fill=%22%23ccc%22 viewBox=%220 0 24 24%22%3E%3Cpath d=%22M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z%22/%3E%3C/svg%3E';
  },

  /**
   * Render leaderboard HTML
   */
  render(entries, userRank, userScore, gameType, timeframe) {
    const container = document.getElementById('leaderboard-table');
    if (!container) return;

    // Build medals/badges
    const medals = ['🥇', '🥈', '🥉'];

    let html = `
      <div class="leaderboard-container">
        <!-- Title -->
        <div class="leaderboard-header dark:bg-gray-800 bg-gray-50 px-6 py-4 border-b dark:border-gray-700">
          <h2 class="text-2xl font-bold dark:text-white">${this.GAMES[gameType]} Leaderboard</h2>
          <p class="text-sm text-gray-600 dark:text-gray-400 mt-1">${this.TIMEFRAMES[timeframe].label}</p>
        </div>

        <!-- User Rank Card (if logged in) -->
        ${userRank ? `
          <div class="user-rank-card dark:bg-blue-900 bg-blue-50 border-l-4 border-blue-500 px-6 py-4 my-6 rounded">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm text-gray-600 dark:text-gray-300">Your Rank</p>
                <p class="text-2xl font-bold dark:text-white">
                  #${userRank} 
                  <span class="text-sm text-gray-500 dark:text-gray-400">
                    (Top ${Math.round((userRank / 100) * 100)}%)
                  </span>
                </p>
              </div>
              <div class="text-right">
                <p class="text-sm text-gray-600 dark:text-gray-300">Your Score</p>
                <p class="text-2xl font-bold dark:text-white">${userScore}</p>
              </div>
            </div>
          </div>
        ` : ''}

        <!-- Rankings Table -->
        <table class="w-full">
          <thead class="dark:bg-gray-800 bg-gray-50 border-b dark:border-gray-700">
            <tr>
              <th class="text-left px-6 py-3 text-sm font-semibold dark:text-gray-300 text-gray-700">Rank</th>
              <th class="text-left px-6 py-3 text-sm font-semibold dark:text-gray-300 text-gray-700">Player</th>
              <th class="text-left px-6 py-3 text-sm font-semibold dark:text-gray-300 text-gray-700">Score</th>
              <th class="text-left px-6 py-3 text-sm font-semibold dark:text-gray-300 text-gray-700">Difficulty</th>
              <th class="text-left px-6 py-3 text-sm font-semibold dark:text-gray-300 text-gray-700">Date</th>
            </tr>
          </thead>
          <tbody>
            ${entries.map((entry, idx) => {
              const medal = medals[idx] || `#${idx + 1}`;
              const date = entry.timestamp?.toDate?.() || new Date(entry.timestamp);
              const formattedDate = date.toLocaleDateString('en-US', { 
                month: 'short', 
                day: 'numeric' 
              });

              return `
                <tr class="border-b dark:border-gray-700 hover:dark:bg-gray-800 hover:bg-gray-50 transition">
                  <td class="px-6 py-4 text-lg font-bold dark:text-white">${medal}</td>
                  <td class="px-6 py-4">
                    <div class="flex items-center gap-3">
                      <img src="${entry.avatar}" alt="${entry.displayName}" 
                           class="w-10 h-10 rounded-full object-cover">
                      <div>
                        <p class="font-semibold dark:text-white">${entry.displayName}</p>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 font-bold text-lg dark:text-green-400 text-green-600">${entry.score}</td>
                  <td class="px-6 py-4 text-sm">
                    <span class="px-2 py-1 rounded-full dark:bg-gray-700 bg-gray-200 dark:text-gray-300 text-gray-700 capitalize">
                      ${entry.difficulty}
                    </span>
                  </td>
                  <td class="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">${formattedDate}</td>
                </tr>
              `;
            }).join('')}
          </tbody>
        </table>

        ${entries.length === 0 ? `
          <div class="text-center py-12">
            <p class="text-gray-500 dark:text-gray-400">No scores yet for this timeframe</p>
          </div>
        ` : ''}
      </div>
    `;

    container.innerHTML = html;
  },

  /**
   * Show loading state
   */
  showLoading(isLoading) {
    const table = document.getElementById('leaderboard-table');
    if (isLoading) {
      if (table) {
        table.innerHTML = `
          <div class="text-center py-12">
            <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
            <p class="mt-4 text-gray-600 dark:text-gray-400">Loading leaderboard...</p>
          </div>
        `;
      }
    }
  },

  /**
   * Show error message
   */
  showError(message) {
    const table = document.getElementById('leaderboard-table');
    if (table) {
      table.innerHTML = `
        <div class="text-center py-12 text-red-600 dark:text-red-400">
          <p>${message}</p>
        </div>
      `;
    }
  }
};

// Initialize when page loads
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('leaderboard-table')) {
      LeaderboardManager.init();
    }
  });
} else {
  if (document.getElementById('leaderboard-table')) {
    LeaderboardManager.init();
  }
}

// Expose to global scope
window.LeaderboardManager = LeaderboardManager;
