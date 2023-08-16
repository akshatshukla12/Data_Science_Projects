from flask import Flask, request, render_template
import util
import matplotlib.pyplot as plt
plt.switch_backend('agg')
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('app.html')

@app.route('/predict_sentiment', methods=['GET', 'POST'])
def predict_sentiment():
    ticker = request.form['ticker']
    df, score = util.get_estimated_sentiments(ticker)
    plt.figure(figsize=(10,8))
    plt.title('Sentiment Analysis of ' + ticker)
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score')
    df.plot(kind='bar')
    plt.tight_layout()
    plt.savefig('./static/image',facecolor='y', transparent=True)
    return render_template('results.html',score=score)

if __name__ == "__main__":
    print("Starting Python Flask Server For Stock Sentiment Prediction...")
    util.load_saved_artifacts()
    app.run()
