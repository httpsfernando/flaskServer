from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

estado = False

@app.route('/')
def inicial():
    
    return render_template("interface.html")



@app.route('/acao', methods=['POST'])
def acao():
    global estado
    estado = not estado  # lógica do servidor

    return jsonify({
        'ativa': estado
    })

@app.route('/led', methods=['POST'])
def estado():
    dados = request.get_json()

    estadoled = dados.get('led')

    if estadoled == 'on':

        return jsonify({
            'estadoled': True
        })


if __name__ == "__main__":
    app.run(host="10.0.0.232", port=80, debug=True)