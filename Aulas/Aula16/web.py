from flask import Flask, render_template, redirect, request
from faixa import *

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_templates("inicio.html", nome='Lista de Faixas')

@app.route('/lista')
def listar_faixas():
    return render_templates("lista.html", nome='Lista de Faixas', lista=ler_faixa())

@app.route('/salvar')
def salvar():
    request.args['musica']
    request.args['album']
    request.args['artista']
    faixa = criar_faixa(musica,album,artista)
    salvar_faixa(faixa)
    return redirect('/lista')

app.run()
