from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def obtener_cliente():
    ci = request.json.get('ci')
    print("CI recibido:", ci)

    if ci == "5829258":
        return jsonify({
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci,
            "nombre": "Katia",
            "apellidos": "Noldin"
        }), 200
    else:
        return jsonify({
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        }), 404