// blogs/static/blogs/js/load_posts.js
$(document).ready(function() {
    $.ajax({
        url: LOAD_BLOGS_URL,  // Use the URL passed from the template
        method: "GET",
        success: function(response) {
            try {
                // Parse the JSON response
                let posts = response;  // No need to parse, as the response is already an object

                // Clear any existing content in the posts container
                $('#posts').html('');

                // Loop through each post and create HTML for it
                posts.forEach(function(post) {
                    // Format the date
                    const createdAt = new Date(post.date_created);
                    const formattedDate = createdAt.toLocaleString();  // Format as a readable string

                    // Create the HTML for the post
                    const postHtml = `
                        <div class="post">
                            <h2>${post.title}</h2>
                            <p>${post.content}</p>
                            <p><strong>Author:</strong> ${post.author}</p>
                            <p><strong>Posted on:</strong> ${formattedDate}</p>
                            <hr>
                        </div>
                    `;

                    // Append the post HTML to the posts container
                    $('#posts').append(postHtml);
                });
            } catch (error) {
                console.error("Error processing posts:", error);
            }
        },
        error: function(xhr, status, error) {
            console.error("Error loading posts:", error);  // Log any errors
        }
    });
});


