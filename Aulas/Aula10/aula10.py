# Aula 10 - 20-11-2019
#-- Web - Calculadora

nome_pagina = 'Calculadora By Python'

from flask import Flask, render_template, request
from operacoes import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo=nome_pagina)

@app.route('/calcular')
def calcular():
    n1 = int(request.args['n1'])
    n2 = int(request.args['n2'])
    r_soma = soma(n1,n2)
    r_subtracao = sub(n1,n2)
    r_multiplicacao = mult(n1,n2)
    r_divisao_inteira = div(n1,n2)
    r_divisao_fracionada = div_frac(n1,n2)
    r_resto = resto(n1,n2)
    r_raiz = raiz(n1,n2)
    resultados ={'soma':r_soma,'subtracao':r_subtracao,'multiplicacao':r_multiplicacao,'divisao_inteira':r_divisao_inteira,'divisao_fracionada':r_divisao_fracionada,'resto':r_resto,'raiz':r_raiz}

    return render_template(
        'resultado.html'
        ,n1=n1
        ,n2=n2
        ,resultados=resultados
        )

app.run()