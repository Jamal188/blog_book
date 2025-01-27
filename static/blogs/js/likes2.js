document.addEventListener('DOMContentLoaded', function() {
    // Update CSRF token after every HTMX swap
    document.body.addEventListener('htmx:afterSwap', function(e) {
        const newToken = e.detail.target.querySelector('[name=csrfmiddlewaretoken]')?.value;
        if (newToken) {
            // Update all CSRF tokens globally
            document.querySelectorAll('[name=csrfmiddlewaretoken]').forEach(input => {
                input.value = newToken;
            });
            // Update HTMX headers
            htmx.config.defaultHeaders['X-CSRFToken'] = newToken;
        }
    });

    // Ensure CSRF token is sent in headers for every request
    document.body.addEventListener('htmx:configRequest', (event) => {
        event.detail.headers['X-CSRFToken'] = document.querySelector('[name=csrfmiddlewaretoken]').value;
    });
});

