
class Phrase():

    def __init__(self, phrase, *args, **kwargs):        
        self.phrase = phrase.lower()    

    def __str__(self):
        return f"{self.phrase}"

    def display_phrase(self, guesses):
        # the_phrase = self.phrase
        the_phrase = ""
        for letter in self.phrase:
            if letter in guesses:
                r_letter = f"{letter} "
                the_phrase += f"{letter} "
            elif letter not in guesses:
                the_phrase += "_ "
        print(the_phrase)        
        return the_phrase


    def check_letter(self, letter): 
        if letter in self.phrase:
            print(f"{letter} is in the puzzle!")
            return 0
        else:
            print(f"Ope, {letter} is not in the puzzle!")
            return 1
        
    
    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
        

if __name__ == "__main__":
    
    guessing_phrase = input("What is the phrase to guess?")
    guesses = ["a","b","c","d"]
    phrase = Phrase(guessing_phrase)
    while True:
        print(phrase.display_phrase(guesses))
        guess = input("Whats your guess?")
        guesses.append(guess)
        phrase.check_letter(guess)
        phrase.check_complete(guesses)

