from crypt import methods
from flask import Flask, request
import src.gameData as gameData
import json

app = Flask(__name__)


@app.route("/",methods=['POST','GET'])
def index():
    if request.method == 'POST':
        gameData.generatePlayer("YOO")
    else:
        gameData.generatePlayer("Humble")
    return "Hallelujah"

@app.route("/login",methods=['POST'])
def login():
    response = {}    
    json_data = request.json
    playerId = gameData.generatePlayer(json_data["name"])
    response["playerId"] = playerId
    response["name"] = json_data["name"]
    return json.dumps(response)



@app.route("/all")
def getListOfAllUsers():
    nameList = []
    for key,player in gameData.activePlayerDict.items():
        nameList.append(player.alias)
    return json.dumps(nameList)



if (__name__ == '__main__'):
    app.run(debug=True)