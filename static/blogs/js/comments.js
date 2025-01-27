document.addEventListener('DOMContentLoaded', function() {
    // Toggle comments visibility
    document.body.addEventListener('click', function(e) {
        if (e.target.matches('[data-toggle-comments]')) {
            const btn = e.target;
            const container = document.querySelector(btn.dataset.target);
            
            if (container.style.display === 'none' || !container.style.display) {
                container.style.display = 'block';
                btn.textContent = 'Hide Comments';
                // Load comments if not already loaded
                if (!container.hasChildNodes()) {
                    htmx.trigger(btn, 'click');
                }
            } else {
                container.style.display = 'none';
                btn.textContent = 'Show Comments';
            }
        }
    });
});
