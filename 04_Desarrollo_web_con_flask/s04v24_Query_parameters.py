from flask import Flask
from flask import request

app = Flask(__name__)

# esta primera line a indica lo que nuestra pagina va a mostrar en su raiz '/'
@app.route('/')
def index(name='Mundo'):
    name = request.args.get('name', name)
    return "Hola {}".format(name)

# aqui simplemente hemos definido nuestra aplicacion xdxdxddddxd
app.run(debug=True, port=8000, host='0.0.0.0')
