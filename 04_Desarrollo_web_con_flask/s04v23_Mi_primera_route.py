from flask import Flask

app = Flask(__name__)

# esta primera line a indica lo que nuestra pagina va a mostrar en su raiz '/'
@app.route('/')
def index():
    return "hola mundo esta es mi primera app de flask!!!!"

# esta otra linea indca lo que pasa si nos metemos a la pagina '/aldo'
@app.route('/aldo')
def aldo():
    return "hola aldo, que pedo¡¿¡¿?"

# aqui simplemente hemos definido nuestra aplicacion xdxdxddddxd
app.run(debug=True, port=8000, host='0.0.0.0')
