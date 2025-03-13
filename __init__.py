from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__) 

                                                                                                                                       
@app.route('/')
def hello_world():
    return """<h2>Bonjour tout le monde !</h2>
           <p>Pour accéder à la page etoiles <a href='./etoiles/'>ici</a></p>
           <p>Pour accéder à la page image <a href='./images/'>ici</a></p>
  <p>Pour accéder à la page jeu <a href='./jeu_des/'>ici</a></p>
  <p>Pour accéder à la page roulette russe <a href='./roulette_russe/'>ici</a></p>"""

@app.route('/etoiles/')
def etoiles():
    return render_template('Carre_Etoiles.html')

@app.route('/jeu_des/')
def jeu_des():
    return render_template('Jeu_Des_Base.html')

@app.route('/images/')
def images():
    return render_template('images.html')
  
@app.route('/roulette_russe/')
def roulette_russe():
    return render_template('Barillet_Vide.html')
    
if __name__ == "__main__":
  app.run(debug=True)
