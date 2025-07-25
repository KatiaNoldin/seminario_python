from flask import Flask
from clientes.clientes import cliente  

app = Flask(__name__)
app.register_blueprint(cliente)  # Registrás el blueprint

@app.route('/', methods=['GET']) 
def inicio():
    return "Servidor Flask funcionando"

if __name__ == '__main__':
    app.run(debug=True, port=5003, host= '0.0.0.0')
