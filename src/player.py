'''
This file contains classes and methods for all details pertaining to one player. 
'''

class Player:
    def __init__(self) -> None:
        self.alias = ""
        self.whomToGuess = -1 # this is the person this player will be guessing
        self.opponentGuess = -1 # this is the id of the person the opponent would be guessing.
        print("Player Created") 

    '''
    Function to set player name. This would by server when a user logs in. 
    '''
    def setPlayerName(self,playerName :str) ->bool:

        if self.alias == "":
            self.alias = playerName
            return True
        return False

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