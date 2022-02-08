from crypt import methods
from flask import Flask, request
import src.gameData as gameData
import json

success = 200
internalError = 500

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

@app.route("/game/new",methods=['POST'])
def startNewGame():
    response = {}
    json_data = request.json

    if "playerId" not in json_data:
        response["success"] = False
        return json.dumps(response),internalError
    playerID = int(json_data["playerId"])

    if gameData.generateGameCandidate(playerID):
        response["success"]  = True
        return json.dumps(response), success
    else :
        response["success"] = False
        return json.dumps(response), internalError


@app.route("/users")
def getListOfAllUsers():
    nameList = []
    for key,player in gameData.activePlayerDict.items():
        nameList.append(player.alias)
    return json.dumps(nameList)

@app.route("/game/available",methods=["GET"])
def getListOfGameCandidates():
    response = []
    response.append(["playerName","playerId", "gameID"])
    candidateList = gameData.activeGameCandidateList
    for (candidateID, candidate) in candidateList.items():
        response.append([candidate.player.alias,candidate.player.playerID, candidateID])
    print(candidateList)
    return json.dumps(response),success

@app.route("/game/join",methods=["POST"])
def joinGame():
    response = {}
    json_data = request.json

    if "playerId" not in json_data:
        response["success"] = False
        return json.dumps(response), internalError

    if "gameId" not in json_data:
        response["success"] = False
        return json.dumps(response), internalError

    playerId = int(json_data["playerId"])
    gameId = int(json_data["gameId"])

    if(gameData.generateGame(playerId, gameId)):
        response["success"] = True
        return json.dumps(response),success
    else:
        response["success"] = False
        return json.dumps(response),internalError

        

if (__name__ == '__main__'):
    app.run(debug=True)