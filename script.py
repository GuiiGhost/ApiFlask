from flask import Flask, jsonify
import users

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def getUser():
    dados = users.users
    return jsonify(dados['user'])


if __name__ == '__main__':
    app.run(debug=True)