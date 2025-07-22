from flask import Blueprint, Flask, jsonify, request

logout= Blueprint ('logout_blueprint', __name__)
@logout.route('/logout', methods=['POST'])
def llamarServicioSet():
    user = request.json.get('user')
    password = request.json.get('password')
    print("user enviado: ", user, "Pass enviado", password)
