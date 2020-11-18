
class Phrase():

    def __init__(self, phrase, *args, **kwargs):        
        self.phrase = phrase.lower()    

    def __str__(self):
        return f"{self.phrase}"

    def display_phrase(self, guesses):
        the_phrase = self.phrase
        for letter in the_phrase:
            if letter not in guesses:
                the_phrase = the_phrase.replace(letter, "_ ")
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

    phrase = Phrase(guessing_phrase)
    print(phrase.display_phrase(), phrase.alphabet, phrase.solved)

    while phrase.solved == False:
        phrase.check_letter()
        # print(phrase.display_phrase(), phrase.alphabet, phrase.solved)
        phrase.check_complete()

