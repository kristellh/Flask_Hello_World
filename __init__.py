from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__) 

                                                                                                                                       
@app.route('/')
def hello_world():
    return """<h2>Bonjour tout le monde !</h2>
           <p>Pour accéder à la page etoiles <a href='./etoiles/'>ici</a></p>"""
  

 

@app.route('/etoiles/')
def etoiles():
    return render_template('Carre_Etoiles.html')



    
if __name__ == "__main__":
  app.run(debug=True)
