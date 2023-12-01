from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to my fantastic application!"

@app.route('/api')
def api():
    return "Hello World"

@app.route('/api_html')
def html_response():
    return render_template("index.html")

app.run(debug=True)