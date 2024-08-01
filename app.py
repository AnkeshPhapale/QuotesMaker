from flask import Flask, render_template, request, redirect, url_for, session
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a real secret key

def getquote(topic):
    genai.configure(api_key='AIzaSyAwWfqZTf5FonESubc3ECQsBlRakOdBv00')
    model = genai.GenerativeModel('gemini-1.5-pro')
    topic = "give me one new motivational quote on " + topic
    quote = model.generate_content(topic)
    return quote.text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        session['user_input'] = user_input
        return redirect(url_for('quote'))
    return render_template('index.html')

@app.route('/quote', methods=['GET'])
def quote():
    user_input = session.get('user_input', '')
    modified_input = getquote(user_input)
    return render_template('quote.html', modified_input=modified_input)

if __name__ == '__main__':
    app.run(debug=True)
