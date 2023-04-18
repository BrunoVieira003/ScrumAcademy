from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/introducao')
def introducao():
    return render_template('introducao.html')

@app.route('/sprint')
def sprint():
    return render_template('sprint.html')

@app.route('/po')
def po():
    return render_template('po.html')

@app.route('/importancia')
def imp():
    return render_template('importancia.html')

@app.route('/productbacklog')
def pbacklog():
    return render_template('productbacklog.html')

@app.route('/sm')
def sm():
    return render_template('sm.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

@app.route('/dor-dod')
def dor_dod():
    return render_template('dor-dod.html')

@app.route('/SprintBacklog')
def sprintbacklog():
    return render_template('SprintBacklog.html')

@app.route('/productincrement')
def PI():
    return render_template('productincrement.html')

@app.route('/planningpoker')
def PP():
    return render_template('planningpoker.html')

@app.route('/pacer')
def pacer():
    return render_template('pacer.html')

@app.route('/burndown')
def burndown():
    return render_template('burndown.html')

@app.route('/mvp')
def mvp():
    return render_template('mvp.html')

@app.route('/skills')
def skills():
    return render_template('shskills.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

app.run(debug=True)