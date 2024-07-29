from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
app = Flask(__name__)


def getquote(topic):
    # Configure the API key (replace 'YOUR_API_KEY' with your actual key)
    genai.configure(api_key='AIzaSyAwWfqZTf5FonESubc3ECQsBlRakOdBv00')

    # Create a model instance (choose an appropriate model)
    model = genai.GenerativeModel('gemini-1.5-pro')

    # Generate a quote
    topic="give me one new motivational quote on "+ topic
    quote = model.generate_content(topic)
    quotetext=quote.text
    return quotetext


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # Perform any string operation here
        # modified_input = getquote()
        return redirect(url_for('result', modified_input=user_input))
    return render_template('index.html')

@app.route('/quote')
def result():
    user_input = request.args.get('modified_input', '')
    modified_input = getquote(user_input)
    return render_template('quote.html', modified_input=modified_input)

if __name__ == '__main__':
    app.run(debug=True)
