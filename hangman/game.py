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
    def __init__(self, character, hit=None, miss=None):
        self.character = character
        self.hit = hit
        self.miss = miss

        if self.hit and self.miss:
            raise InvalidGuessAttempt("Can't be both hit and miss")

    def is_hit(self):
        return bool(self.hit)
    
    def is_miss(self):
        return bool(self.miss)
        
    
class GuessWord(object):
    def __init__(self, word):
        if not word:
            raise InvalidWordException()
       
        self.answer = word.lower()
        self.mask_char = "*"
        self.masked = len(self.answer) * self.mask_char
        self.previous_guesses = []
        self.miss_count = 0

    def perform_attempt(self,character):
        self.previous_guesses.append(character.lower())
        if len(character) != 1:
            raise InvalidGuessedLetterException()
        if character.lower() not in self.answer:
            return GuessAttempt(character, miss=True)
            
        self.reveal = "".join([character if character in self.previous_guesses else self.mask_char for character in self.answer.lower()])
        self.masked = self.reveal
        return GuessAttempt(character, hit=True)

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


g = HangmanGame(guess_limit=10)

print(g.select_random_word(['a','b','c','d','e']))
'''