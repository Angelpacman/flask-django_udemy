from flask import Flask
from flask import request

app = Flask(__name__)

# ahora la linea puede recibir en el navegador algun nombre; /?name=aldo
@app.route('/')
def index(name='Mundo', lastname='!!!'):
    name = request.args.get('name', name)
    lastname = request.args.get('lastname', lastname)
    return "Hola {} {}".format(name, lastname)

# aqui simplemente hemos definido nuestra aplicacion
app.run(debug=True, port=8000, host='0.0.0.0')
