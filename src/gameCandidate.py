from .player import Player


'''
A game candidate is created when a new user comes in and wants to create a new game to the server. 

When another user joins in and checks list of existing games, a list of open gameCandidates open Up. 

Currently a game candidate would work if the player just started a connection and went away. Will handle handshakes
and other fault checks later on
'''

class GameCandidate :
    def __init__(self,player:Player) -> None:
        self.player = player
        # generate a unique psiphon based on the time
        self.gamePsiphon = ""
        