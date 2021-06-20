from flask import Flask, render_template,request,abort,json
import os
import sys
app = Flask(__name__)

datos = open('MSX.json')
msx = json.load(datos)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

@app.route('/juegos')
def juegos():
	return render_template("juegos.html")
@app.route('/listajuegos', methods=["POST"])
def listajuego():
	lista=[]
	form=request.form.get("informacion")
	for a in msx:
		if str(form) == "" or str(a["nombre"]).startswith(form):
			lista.append(a)
	return render_template("listajuegos.html", lista=lista)
@app.route('/juego/<identificador>')
def juego(identificador):
	lista=[]
	indicador=False
	for a in msx:
		if int(a.get("id")) == int(identificador):
			indicador=True
			lista.append(a)
	if indicador == True:
		return render_template("juego.html",lista=lista)
	else:
		abort(404)
port=os.environ["PORT"]
app.run("0.0.0.0",int(port),debug=True)
