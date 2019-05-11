from flask import Flask
from flask import request

app = Flask(__name__)

# ahora la linea puede recibir en el navegador algun nombre; /?name=aldo
@app.route('/')
def index(name='Mundo'):
    name = request.args.get('name', name)
    return "Hola {}".format(name)

# aqui simplemente hemos definido nuestra aplicacion
app.run(debug=True, port=8000, host='0.0.0.0')
