from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Aqui vai a página home'

app.run(debug=True)