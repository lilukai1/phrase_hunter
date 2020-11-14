import random

from phrase import Phrase

PHRASES = [
    "bobs",
    "tims",
    "bill",
    "four",
    "five",
]

class Game():
    self.phrase = 
    missed = 0
    self.letters_tried = []
    letters_tried = []

    def __init__(self):
        self.missed = 0
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.active_phrase = random.choice(PHRASES)

    def welcome(self):
        

The class should also have these methods:

start(): Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, increments the number of missed by one if the guess is incorrect, calls the game_over method.
get_random_phrase(): this method randomly retrieves one of the phrases stored in the phrases list and returns it.
welcome(): this method prints a friendly welcome message to the user at the start of the game
get_guess(): this method gets the guess from a user and records it in the guesses attribute
game_over(): this method displays a friendly win or loss message and ends the game.

if __name__ == "__main__":