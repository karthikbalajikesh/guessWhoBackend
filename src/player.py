'''
This file contains classes and methods for all details pertaining to one player. 
'''
class Player: 

    def __init__(self,name:str, id:int) -> None:
        self.playerID = id
        self.gameID = -1
        self.alias = name
        self.whomToGuess = -1 # this is the person this player will be guessing
        self.opponentGuess = -1 # this is the id of the person the opponent would be guessing.
        print("Created player with name :  ",name) 

    '''
    Function to set who the opponent Guesses
    '''
    def setOpponentGuesss(self,oppId :int) ->bool:

        if self.opponentGuess == -1 :
            self.opponentGuess = oppId
            return True
        return False


    '''
    Function to set whom the player is going to guess
    '''
    def setWhomToGuess(self, guessId:int) ->bool :

        if self.whomToGuess == -1 :
            self.whomToGuess = guessId
            return True
        return False


    '''
    Function that returns True if there is a right guess and false otherwise
    '''
    def guess(self, guessId:int) ->bool:

        if(guessId == self.whomToGuess):
            print("Player {name}  has guessed right")
            return True
        return False


    '''
    Function that assigns a game ID
    '''
    def assignGameId(self, id:int) ->bool:
        if(self.gameID == -1 ):
            self.gameID = id
            return True

        return False