from flask import Blueprint, Flask, jsonify, request

login= Blueprint ('login', __name__)
@login.route('/login', methods=['POST'])

def llamarServicioSet():
    user= request.json.get('user')
    password= request.json.get('password')
    print("user enviado: ", user, "Pass enviados: " , password)
    codRes, menRes, accion, roll = inicializarVariables(user, password)
    salida = {
        "codRes": codRes,
        "menRes": menRes,
        "usuario": user,
        "accion": accion,
        "roll": roll
    }
    return jsonify(salida)
def inicializarVariables(user, password):
    codRes = "SIN_ERROR"
    menRes = "ok"
    accion = "login exitoso"
    roll="admin"
    userLocal= "katiafn"
    passwordLocal= "unida123"
    try:
        if user == userLocal and password == passwordLocal:
           print("Login exitoso")
           accion = "login exitoso"
        else:
            codRes = "ERROR"
            menRes = "Usuario o contraseña incorrectos"
            accion = "login fallido"
            roll = "N/A"
            user = "N/A"
        
    except Exception as e:
        print("Error en el login: ", e)
        codRes = "ERROR"
        menRes = "Error en el login"
        accion = "error en el login"
        roll = "N/A"
        return codRes, menRes, accion, roll,user






    return codRes, menRes, accion, roll

    







   