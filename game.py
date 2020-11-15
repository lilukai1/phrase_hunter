import random

from phrase import Phrase


class Game():

    def __init__(self):
        self.phrases = [
            "beautiful is better than ugly",
            "explicit is better than implicit",
            "simple is better than complex",
            "complex is better than complicated",
            "flat is better than nested",
            ]
        self.missed = 0
        self.guesses = [" ",]
        self.active_phrase = None


    ## start(): Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, increments the number of missed by one if the guess is incorrect, calls the game_over method.

    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        incomplete = False

        while self.missed < 5 and incomplete == False:
            self.active_phrase.display_phrase(self.guesses)
            guess = self.get_guess()
            incomplete = self.active_phrase.check_complete(self.guesses)
            print(incomplete)
            if guess:
                self.missed += guess
                lives_left = 5 - self.missed
                print(f"You have missed {self.missed} tries! You only have {lives_left} tries left.")
        self.game_over()
##welcome(): this method prints a friendly welcome message to the user at the start of the game

    def welcome(self):
        welcome = """
    Welcome to Guess That Phrase! 
        (Python Edition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
        print(welcome)

##get_random_phrase(): this method randomly retrieves one of the phrases stored in the phrases list and returns it.

    def get_random_phrase(self):
        choice = random.choice(self.phrases)
        print(choice)
        return Phrase(choice)

## get_guess(): this method gets the guess from a user and records it in the guesses attribute

    def get_guess(self):
        try:
            letter = input("What is your guess? Enter one letter >>  \n")
            letter = letter.lower()
            if letter in self.guesses:
                print(f"You have already tried {letter}!")
            elif letter.isalpha() == False:
                print(f"You must guess an alphabetic character, no spaces, punctuation or numbers.")
            else:
                self.guesses.append(letter)
                return(self.active_phrase.check_letter(letter))
        except:
            print("Your guess must be a single letter.")
## game_over(): this method displays a friendly win or loss message and ends the game.

    def game_over(self):
        if self.missed == 5:
            print(f"You ran out of lives!  The answer was {self.active_phrase}.  Better luck next time!")
        else:
            print(f"Congrats, you won with only {self.missed} wrong guesses!")
    
        while True:
            try:
                try_again = input("Would you like to try again? Y/N\n")
                if try_again.lower() == "y":
                    new_game = Game().start()
                else:
                    print("Thanks, have a great day!")
                    quit()
            except:
                print("I'm sorry, you have to enter y for yes or n for no.")

if __name__ == "__main__":

    game = Game()

    game.start()