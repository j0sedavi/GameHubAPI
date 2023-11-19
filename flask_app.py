# consultar posições x e y
# enviar posições x e y

from flask import Flask, jsonify, request

app = Flask(__name__)

players = []

@app.route('/players/get/<int:id>',methods=["GET"])
def players_Get(id):
    if id > len(players):
      return "error id not found"
    else:
      return jsonify(players[id])

@app.route('/players/update/<int:id>',methods=["PUT"])
def player_update(id):
    size = len(players) - 1
    if id > size:
      return "error id not found"
    else:
      JsonNew = request.get_json()
      players[id].update(JsonNew)
      return jsonify(JsonNew)
@app.route('/players/add',methods=["PUT"])
def player_add():
  JsonNew = request.get_json()
  players.append(JsonNew)
  return jsonify(JsonNew)
@app.route('/server',methods=['GET'])
def serverinfo():
  info = {
    "playersCount": len(players)
  }
  return jsonify(info)
