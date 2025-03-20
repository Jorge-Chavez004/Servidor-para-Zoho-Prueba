from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

# Clave secreta para firmar y validar el JWT
SECRET_KEY = "BPM-ULIMA"

@app.route('/validar_jwt', methods=['GET'])
def validar_jwt():
    token = request.args.get('token')

    if not token:
        return jsonify({"valido": False, "error": "No se recibió un token"}), 400

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"valido": True, "datos": payload}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"valido": False, "error": "Token expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"valido": False, "error": "Token inválido"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

