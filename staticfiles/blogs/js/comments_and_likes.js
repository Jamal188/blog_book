
// scripts.js

// Event listener for HTMX 'afterSwap' event
document.addEventListener('htmx:afterSwap', function(event) {
    if (event.detail.target.id === 'like-list') {
        // Show the like list after loading
        document.getElementById('like-list').style.display = 'block';
        // Hide the "Show Likes" button
        document.getElementById('show-likes-btn').style.display = 'none';
    }
});

// Store the initial state of the like list (empty)
const initialLikes = document.getElementById('like-list').innerHTML;

// Function to restore the initial state of the like list
function restoreInitialLikes() {
    document.getElementById('like-list').innerHTML = initialLikes;
    document.getElementById('like-list').style.display = 'none'; // Hide the like list
    document.getElementById('show-likes-btn').style.display = 'inline-block'; // Show "Show Likes"
    document.getElementById('hide-likes-btn').style.display = 'none'; // Hide "Hide Likes"
}

// HTMX event listener to toggle buttons
document.addEventListener('htmx:afterSwap', function(event) {
    if (event.detail.target.id === 'like-list') {
        // Show the like list and toggle buttons
        document.getElementById('like-list').style.display = 'block'; // Show the like list
        document.getElementById('show-likes-btn').style.display = 'none'; // Hide "Show Likes"
        document.getElementById('hide-likes-btn').style.display = 'inline-block'; // Show "Hide Likes"
    }
});

// comments.js

// Store the initial comments in a variable
const initialComments = document.getElementById('comments').innerHTML;

// Function to restore the initial comments
function restoreInitialComments() {
    document.getElementById('comments').innerHTML = initialComments;
    document.getElementById('show-comments-btn').style.display = 'inline-block';
    document.getElementById('hide-comments-btn').style.display = 'none';
}

// HTMX event listener to toggle buttons
document.addEventListener('htmx:afterSwap', function(event) {
    if (event.detail.target.id === 'comments') {
        // Show "Hide Comments" button and hide "Show All Comments" button
        document.getElementById('show-comments-btn').style.display = 'none';
        document.getElementById('hide-comments-btn').style.display = 'inline-block';
    }
});
