from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

# ahora la linea puede recibir en el navegador algun nombre; /?name=aldo
@app.route('/')
@app.route('/<name>')

def index(name='Mundo'):
    name = request.args.get('name', name)
    return "Hola {}".format(name)

# en estas lineas hemos puesto distintos route con el fin de acertar al tipo de
# variable de entrada a la url
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')

def add(num1, num2):
    #return '{} + {} = {}'.format(num1, num2,num1 + num2)
    return render_template("add.html", a=num1, b=num2)

# aqui simplemente hemos definido nuestra aplicacion
app.run(debug=True, port=8000, host='0.0.0.0')
