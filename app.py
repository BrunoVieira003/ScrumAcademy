from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', href="/introducao")

@app.route('/introducao')
def introducao():
    return render_template('introducao.html', href="/importancia")

@app.route('/importancia')
def imp():
    return render_template('importancia.html', href="/sprint")

@app.route('/sprint')
def sprint():
    return render_template('sprint.html', href="/SprintBacklog")

@app.route('/SprintBacklog')
def sprintbacklog():
    return render_template('SprintBacklog.html', href="/mvp")

@app.route('/mvp')
def mvp():
    return render_template('mvp.html', href="/productincrement")

@app.route('/productincrement')
def PI():
    return render_template('productincrement.html', href="/po")

@app.route('/po')
def po():
    return render_template('po.html', href="/sm")

@app.route('/sm')
def sm():
    return render_template('sm.html', href="/equipe")

@app.route('/equipe')
def equipe():
    return render_template('equipe.html', href="/productbacklog")

@app.route('/productbacklog')
def pbacklog():
    return render_template('productbacklog.html', href="/dor-dod")

@app.route('/dor-dod')
def dor_dod():
    return render_template('dor-dod.html', href="/burndown")

@app.route('/burndown')
def burndown():
    return render_template('burndown.html', href="/planningpoker")

@app.route('/planningpoker')
def PP():
    return render_template('planningpoker.html', href="/pacer")

@app.route('/pacer')
def pacer():
    return render_template('pacer.html', href="/skills")

@app.route('/skills')
def skills():
    return render_template('shskills.html', href="/quemsomos")

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html', href="/")

app.run(debug=True)