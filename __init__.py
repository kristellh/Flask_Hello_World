from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__) 

                                                                                                                                       
@app.route('/')
def hello_world():
    return """<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>
            <p>Pour accéder à la page contact <a href='./contact/'>Ici</a></p>
            <p>Pour accéder à la page cnam <a href='./cnam/'>Ici</a></p>
            <p>Pour accéder à la page cv <a href='./cv/'>Ici</a></p>
            <p>Pour accéder à la page exercice liste <a href='./exercice_base1/'>Ici</a></p>
            <p>Pour accéder à la page exercice 2 <a href='./exercice_base2/'>Ici</a></p>
            <p>Pour accéder à la page exercice 3 <a href='./exercice_base3/'>ici</a></p>"""
  
@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route('/exercice_base1/')
def exercices1():
    return render_template('exercice_base1.html')

@app.route('/exercice_base2/')
def exercices2():
    return render_template('Exercices_HTML.html')
  
@app.route('/exercice_base3/')
def exercices3():
    return render_template('exercices_base3.html')
  
@app.route("/cnam/")
def MaPremierepage():
    return render_template("cnam.html")
  
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")
  
@app.route("/cv/")
def MonCv():
    return render_template("cv.html")

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
