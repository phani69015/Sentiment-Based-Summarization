// script.js
$(document).ready(function() {
    $('#article-form').on('submit', function(e) {
        e.preventDefault();
        const article = $('#article').val();
        
        $.ajax({
            type: 'POST',
            url: '/summarize',
            contentType: 'application/json',
            data: JSON.stringify({ article: article }),
            success: function(data) {
                $('#results').html(`
                    <p><strong>Sentiment:</strong> ${data.sentiment}</p>
                    <p><strong>Sentiment Score:</strong> ${data.sentiment_score}</p>
                    <p><strong>Summary:</strong> ${data.summary}</p>
                `);
            }
        });
    });
});
