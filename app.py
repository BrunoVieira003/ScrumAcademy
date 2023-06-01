from flask import Flask, render_template, request
from q import *
import random

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
    return render_template('shskills.html', prox="/materiaisextras", ante="/planningpoker")

@app.route('/materiaisextras')
def materiaisextras():
    return render_template('materiaisextras.html', prox="/", ante="/skills")

@app.route('/audios')
def audios():
    return render_template('audios.html', ante="/")

@app.route('/questoes', methods=['GET', 'POST'])
def questoes():
    global Q      #questoes do aqrquivo q.py
    global alt    #alternativas do aqrquivo q.py
    global gab    #gabarito do aqrquivo q.py

    seed=[]

    newQ = []
    newalt = []
    newgab = []

    score = 0

    if request.method == 'POST':
        resp=[] #respostas
        cor=[] #color das corretas
        seed = request.form['seed']


        seed = seed.strip('][').split(', ')


        for i in seed:    #pega questões anteriores
            i = int(i)
            newQ.append(Q[i])
            newalt.append(alt[i])
            newgab.append(gab[i])

        for i in range(0,len(newQ)):   #Checa cada alternativa e compara com gabarito
            resp.append(request.form[f'q{i}'])
            if request.form[f'q{i}'] == newgab[i]:
                score += 1   
                cor.append('lightgreen') 
            else:
                cor.append('pink')
        scorep = score/len(newQ)*100   #porcentagem de acertos

        return render_template('questoes.html', q = newQ, alt = newalt, x = len(newQ), score = score, scorep = int(scorep), enviado = True, gab = newgab, resp = resp, c=cor, r=resp)

    for i in random.sample(range(0,45), 10):    #pega questões aleatorias
        newQ.append(Q[i])
        newalt.append(alt[i])
        newgab.append(gab[i])
        seed.append(i)
    
    return render_template('questoes.html', q = newQ, alt = newalt, x = len(newQ), enviado = False, gab = newgab, seed = seed)

app.run(debug=True)