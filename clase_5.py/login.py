from flask import Blueprint, Flask, jsonify, request

login= Blueprint ('login', __name__)
@login.route('/login', methods=['POST'])
def llamarServicioSet():
    user= request.json.get('user')
    password= request.json.get('password')
   
   
   
   
   
    print("user enviado: ", user, "Pass enviado", password)
    codRes, menRes, accion= inicializarVariables(user, password)
    salida={
        'codRes': codRes,
        'menRes': menRes,
        'accion': accion,
        'usuario': user
    }
    return jsonify(salida)
def inicializarVariables(user, password):
    codRes= 0
    menRes= "OK"
    accion="Login exitoso"
    rol= "Admin"
    userlocal="katiaf"
    passwordlocal="Unida123"
    try:
        if user != userlocal or password != passwordlocal:
           print("Login exitoso")
           accion= "Login exitoso"
        else:
            codRes= "error"
            menRes= "Login Fallido"
            accion="Login Fallido"
            rol="N/A"
    except Exception as e:
        print("Error en el login: ", e)
        codRes= "error"
        menRes= "Error en el login"
        accion="Error en el login"
        rol="N/A"
    return codRes, menRes, accion

    
    return codRes, menRes, accion