alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']
letters_tried = []
wrong = 0

class Phrase():

    def __init__(self, guessing_phrase):
        self.guessing_phrase = guessing_phrase
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.letters_tried = []
        self.solved = False
        self.wrong = 0
    

    def __str__(self):
        return f"{guessing_phrase}"

    def display_phrase(self):
        self.the_phrase = self.guessing_phrase
        for letter in self.alphabet:
            if letter in self.the_phrase:
                self.the_phrase = self.the_phrase.replace(letter, "_")
        return self.the_phrase

    def check_letter(self):
        try:
            letter = input("What is your guess? Enter one letter >>  \n")
        except:
            print("Your guess must be a single letter.")
        if letter in self.letters_tried:
            print(f"You have already tried {letter}!")
        else:
            self.alphabet.remove(letter)
            self.letters_tried.append(letter)        
            if letter in self.guessing_phrase:
                print(f"{letter} is in the puzzle!")
            else:
                print(f"Ope, {letter} is not in the puzzle!")
        print(self.alphabet)
    
    def check_complete(self):
        if "_" not in self.display_phrase():
            print("You won the game!!")
            self.solved = True
        

if __name__ == "__main__":
    
    guessing_phrase = input("What is the phrase to guess?")

    phrase = Phrase(guessing_phrase)
    print(phrase.display_phrase(), phrase.alphabet, phrase.letters_tried, phrase.solved)

    while phrase.solved == False:
        phrase.check_letter()
        print(phrase.display_phrase(), phrase.alphabet, phrase.letters_tried, phrase.solved)
        phrase.check_complete()

