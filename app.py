from flask import Flask, request, render_template, jsonify
from summarizer import summarize_text_with_sentiment

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    article = data['article']
    
    summary, sentiment_label, sentiment_score = summarize_text_with_sentiment(article)
    
    response = {
        'sentiment': sentiment_label,
        'sentiment_score': sentiment_score,
        'summary': summary
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
