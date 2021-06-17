from flask import Flask, render_template,request,abort,json
import os
import sys
app = Flask(__name__)
datos = open('msx.json')
msx = json.load(datos)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("index.html")

@app.route('/juegos')
def juegos():
	return render_template("juegos.html")
port=os.environ["PORT"]
app.run("0.0.0.0",int(port),debug=True)
