from flask import Flask
from src.player import Player

playerList = []

app = Flask(__name__)

@app.route("/")
def index():
    playerList.append(Player())
    return "Player Created"


if (__name__ == '__main__'):
    app.run(debug=False)