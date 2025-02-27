from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__) 

                                                                                                                                       
@app.route('/')
def hello_world():
    return """<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>
            <p>Pour accéder à la page exercice liste <a href='./exercice_base1/'>Ici</a></p>
            <p>Pour accéder à la page exercice 2 <a href='./exercice_base2/'>Ici</a></p>
            <p>Pour accéder à la page exercice 3 <a href='./exercice_base3/'>ici</a></p>
            <p>Pour accéder à la page formulaire <a href='./formulaire/'>ici</a></p>
            <p>Pour accéder à la page TP1 <a href='./TP1/'>ici</a></p>
           <p>Pour accéder à la page maison <a href='./maison/'>ici</a></p>
           <p>Pour accéder à la page vallet <a href='./vallet/'>ici</a></p>
          <p>Pour accéder à la page chenille <a href='./chenille/'>ici</a></p> 
           <p>Pour accéder à la page carre <a href='./carre/'>ici</a></p>"""
  
@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route('/carre/')
def carre():
    return render_template('carre.html')
  
@app.route('/chenille/')
def chenille():
    return render_template('chenille.html')

@app.route('/vallet/')
def cards():
    return render_template('vallet.html')

@app.route('/actualite/')
def actualite():
    return render_template('actualite.html')

@app.route('/maison/')
def maison():
    return render_template('Exemple_Base_SVG.html')

@app.route('/act/')
def act():
    return render_template('act.html')
  
@app.route('/exercice_base1/')
def exercices1():
    return render_template('exercice_base1.html')

@app.route('/exercice_base2/')
def exercices2():
    return render_template('Exercices_HTML.html')
  
@app.route('/exercice_base3/')
def exercices3():
    return render_template('exercices_base3.html')

@app.route('/formulaire/')
def formulaire():
    return render_template('formulaire.html')

@app.route('/TP1/')
def tp1():
    return render_template('TP1.html')

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    val_user=int(imput("Entrer un nombre\n"))
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    valeur1=int(imput("Entrer un nombre\n"))
    valeur2=int(imput("Entrer un nombre\n"))
    sommeres = valeur1 + valeur2
    pair = "impair"
    if sommeres % 2 == 0:
        pair = "pair"       
    return "<h2>La somme de vos valeurs est : </h2>" + str(valeur1 + valeur2)

@app.route('/sommeliste/<path:liste>')
def sommeliste(liste):
    L=[int(i) for i in input("Entrer x nombres séparé d'un espace\n").split()]
    somme_nbliste=int(sum(L))
    maxnb=int(max(L))
    return "<h2>La somme de vos valeurs est : </h2>" + str(somme_nbliste)+ "\n" + "<h2>La valeur la plus grande saisie est : </h2>" + str(maxnb)
    
if __name__ == "__main__":
  app.run(debug=True)
