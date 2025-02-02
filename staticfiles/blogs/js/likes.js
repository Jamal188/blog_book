document.addEventListener('DOMContentLoaded', function() {
    // Update like button state and CSRF token
    document.body.addEventListener('htmx:afterSwap', function(e) {
        const target = e.detail.target;
        
        // Update like button style
        if (target.matches('.like-btn')) {
            if (target.getAttribute('data-liked') === 'true') {
                target.classList.add('liked');
            } else {
                target.classList.remove('liked');
            }
        }

        // Extract new CSRF token from the swapped content
        const newCsrfToken = target.querySelector('[name=csrfmiddlewaretoken]')?.value;
        if (newCsrfToken) {
            // Update all CSRF tokens in forms
            document.querySelectorAll('[name=csrfmiddlewaretoken]').forEach(input => {
                input.value = newCsrfToken;
            });
            // Update meta tag (if used)
            const metaCsrf = document.querySelector('meta[name="csrf-token"]');
            if (metaCsrf) {
                metaCsrf.content = newCsrfToken;
            }
        }
    });
    // Refresh the page after any like button interaction
    document.body.addEventListener('htmx:afterRequest', function(e) {
        if (e.detail.elt.classList.contains('like-btn')) {
            window.location.reload();
        }
    });

});

