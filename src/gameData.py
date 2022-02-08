'''
This file contains all the data for the program such as users online and 
games requested and games running currently with their complete state. 
'''
from typing import List
from .player import Player
from .game import Game
from .gameCandidate import GameCandidate


####################################################
lastPlayerID = 0
activeGameCandidateList = {}
activeGameList = {}
activePlayerDict = {}
activePlayerList:List[Player] = []
####################################################

def getNextGameCandidateNumber() -> int:
    startNumber = 0
    while(startNumber in activeGameCandidateList):
        startNumber+=1
    return startNumber

def getNextGameNumber() ->int :
    startNumber = 0
    while(startNumber in activeGameList) :
        startNumber += 1
    return startNumber

def generatePlayer(name:str) ->int: 
    global lastPlayerID
    genPlayer = Player(name,lastPlayerID)
    activePlayerDict[genPlayer.playerID] = genPlayer
    lastPlayerID += 1
    return genPlayer.playerID


def generateGameCandidate(playerID:int) ->bool : 
    global activePlayerDict
    if playerID in activePlayerDict:
        activeGameCandidateList[getNextGameCandidateNumber()] =  \
             GameCandidate(activePlayerDict[playerID])
        return True
    print("Could not find player in playerPool")
    return False

def generateGame(playerid:int, candidateID:int) ->bool :
    global activePlayerList
    global activeGameCandidateList
    if playerid not in activePlayerList:
        return False

    if candidateID in activeGameCandidateList:
        # This implies we can create a game
        candidate = activeGameCandidateList[candidateID]

        # Remove from candidates
        activeGameCandidateList.pop(candidateID)

        nextGameNumber = getNextGameNumber()
        game_ = Game(candidate.player, activePlayerList[playerid],nextGameNumber)
        activeGameList[nextGameNumber] = game_
        
        return True

    return False