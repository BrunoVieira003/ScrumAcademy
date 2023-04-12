from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/sprint')
def sprint():
    return render_template('sprint.html')

@app.route('/importancia')
def imp():
    return render_template('importancia.html')

app.run(debug=True)