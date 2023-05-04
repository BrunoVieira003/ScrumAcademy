from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', prox="/introducao")

@app.route('/introducao')
def introducao():
    return render_template('introducao.html', prox="/sprint", ante="/")

@app.route('/sprint')
def sprint():
    return render_template('sprint.html', prox="/sprintbacklog", ante="/introducao")

@app.route('/sprintbacklog')
def sprintbacklog():
    return render_template('SprintBacklog.html', prox="/mvp", ante="/sprint")

@app.route('/mvp')
def mvp():
    return render_template('mvp.html', prox="/po", ante="/sprintbacklog")


@app.route('/po')
def po():
    return render_template('po.html', prox="/sm", ante="/mvp")

@app.route('/sm')
def sm():
    return render_template('sm.html', prox="/equipe", ante="/po")

@app.route('/equipe')
def equipe():
    return render_template('equipe.html', prox="/productbacklog", ante="/sm")

@app.route('/productbacklog')
def pbacklog():
    return render_template('productbacklog.html', prox="/dor-dod", ante="/equipe")

@app.route('/dor-dod')
def dor_dod():
    return render_template('dor-dod.html', prox="/burndown", ante="/productbacklog")

@app.route('/burndown')
def burndown():
    return render_template('burndown.html', prox="/planningpoker", ante="/dor-dod")

@app.route('/planningpoker')
def PP():
    return render_template('planningpoker.html', prox="/skills", ante="/burndown")

@app.route('/skills')
def skills():
    return render_template('shskills.html', prox="/quemsomos", ante="/planningpoker")

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html', prox="/")

app.run(debug=True)