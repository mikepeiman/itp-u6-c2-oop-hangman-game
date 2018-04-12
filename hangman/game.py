import random
from hangman.exceptions import *


class GuessAttempt(object):
    def __init__(self):
        pass
    
    @classmethod
    def is_hit(self):
        print("It's a hit!")
        self.hit_count += 1
        return self.hit_count
    
    @classmethod
    def is_miss(self):
        print("It's a miss!")
        self.miss_count += 1
        return self.miss_count

class GuessWord(object):
    def __init__(self, answer_word, guess_limit, remaining_misses):
        self.answer = answer_word.upper()
        self.masked = len(self.answer)*"*"
        self.mask_char = "*"
        self.reveal = self.masked
        self.attempt_list = []
        self.miss_count = 0
        self.hit_count = 0
        self.remaining_misses = remaining_misses
        self.guess_limit = guess_limit
        print("GuessWord self.answer = ", self.answer)
        print("Guess limit = ", self.guess_limit)

    def perform_attempt(self,attempt=None):
        while self.miss_count < self.guess_limit:
            input_string = "Guess limit: {} | Misses: {} | Attempts: {}".format(self.guess_limit, self.miss_count, self.attempt_list)
            input_string += "\nYour secret word: {}".format(self.reveal)
            input_string += "\nMake a guess: "
            self.attempt = input(input_string).upper()
                
            if len(self.attempt) != 1:
                raise InvalidGuessAttempt('Error on input, please enter a single letter')
            
            self.attempt_list.append(self.attempt)
            self.reveal = "".join([char if char in self.attempt_list else self.mask_char for char in self.answer.upper()])
            self.masked = self.reveal
            if self.attempt not in self.answer.upper():
                print("self.attempt = ", self.attempt, " not in self.answer ", self.answer)
                self.miss_count += 1
                if self.miss_count == self.guess_limit:
                    print("Game over! Guess limit exceeded.")
                    return
                GuessAttempt.is_miss()
            else:
                self.hit_count += 1
                GuessAttempt.is_hit()
            if self.mask_char not in self.masked:
                print("You win!!!!!!!!! You missed with {} of {} guesses, and hit with {} guesses.".format(self.miss_count, self.guess_limit, self.hit_count))
                return
                    
    
    # def mask_answer_word(self):
    #     for char in self.answer:
    #         self.masked += "*"
    #     return self.masked

class HangmanGame(object):
    WORD_LIST = ['rmotr', 'python', 'awesome']
    def __init__(self,word_list=[''],guess_limit=5):
        self.word_list = word_list
        self.guess_limit = guess_limit

        if len(self.word_list) < 1:
            self.word_list = self.WORD_LIST
        self.answer_word = random.choice(self.word_list)
        self.miss_count = GuessWord.miss_count
        self.remaining_misses = self.guess_limit - self.miss_count
        self.word = GuessWord(self.answer_word, self.guess_limit, self.remaining_misses)
    
    # def set_word_list(self,word_list):
    #     if len(self.word_list) < 1:
    #         self.word_list = self.WORD_LIST
    #     # print(str(self.word_list) + " guess limit: " + str(self.guess_limit))
    #     return self.word_list
    
    # def set_word(self,word_list):
    #     self.word_list = word_list
    #     answer_word = random.choice(self.word_list)
    #     print(answer_word)
    #     return answer_word
    # self.word = GuessWord(set_word(self.word_list))


  
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