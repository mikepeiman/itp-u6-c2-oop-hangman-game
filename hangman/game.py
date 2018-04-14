import random
from .exceptions import *

# class InvalidListOfWordsException(Exception):
#     pass


# class InvalidWordException(Exception):
#     pass


# class GameWonException(Exception):
#     pass


# class GameLostException(Exception):
#     pass


# class GameFinishedException(Exception):
#     pass


# class InvalidGuessedLetterException(Exception):
#     pass


# class InvalidGuessAttempt(Exception):
#     pass


class GuessAttempt(object):
    def __init__(self, guess_char, hit=None, miss=None):
        self.guess = guess_char
        self.hit = hit
        self.miss = miss
        self.miss_counter = 0

        if self.hit and self.miss:
            raise InvalidGuessAttempt

    
    def is_hit(self):
        if self.hit and not self.miss:
            return True
        if self.hit and self.miss:
            raise InvalidGuessAttempt
        else:
            return False
    
    def is_miss(self):
        if self.miss and not self.hit:
            self.miss_counter += 1
            return True
        if self.miss and self.hit:
            raise InvalidGuessAttempt
        else:
            return False
        
    
class GuessWord(object):
    def __init__(self):
        pass

class HangmanGame(object):
    def __init__(self):
        pass
  
'''
>we need to create an answer word to guess, from either user input or default list
>we need to mask that word as the answer
>we need to set number of guesses allowed, from default or user input
>we need to match the character of user guess against the answer word, and generate either a hit or a miss, as well as decrement guess counter
>if a hit, we need to reveal that letter at all locations in the answer word
>throughout, we need to check end game conditions: win if the answer has been solved, or lose if guess count limit has been hit


g = HangmanGame(number_of_guesses=10)

print(g.select_random_word(['a','b','c','d','e']))
'''