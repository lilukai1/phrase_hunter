import getpass
import tkinter as tk

word = "default"
solved = False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
letters_tried = []
wrong = 0
pics = ["""
      |------|
      |
      |
      |
      |
    __|________  """,
    """
          |------|
          |      O
          |
          |
          |
        __|________  """,
        """
          |------|
          |      O
          |     /|
          |
          |
        __|________  """,
        """
          |------|
          |      O
          |     /|\\
          |
          |
        __|________  """,
        """
          |------|
          |      O
          |     /|\\
          |      |
          |     /
        __|________  """,
        """
          |------|
          |      O
          |     /|\\
          |      |
          |     / \\
        __|________  """
        ]
win = tk.Tk()

def get_secret_word():
    secret = getpass.getpass("So, whats the secret word?")
    return secret

def the_start(puzzle):
    for letter in puzzle:
        puzzle = f"{filtered_answer(word, alphabet)}"
        #puzzle = puzzle.replace(letter, "_ ")
        #print(puzzle)
    return puzzle


def already_tried():
    print(f"You have already tried: {letters_tried}")


def get_guess():
    guess = entry.get()
    try:
        guess = input("What letter would you like to try?")
    except:
        ValueError("Input not recognized.  Try just a single letter.")
    if guess not in letters_tried:
        letters_tried.append(guess)
        alphabet.remove(guess)
        check_answer(guess)
        if guess not in word:
           wrong += 1
    

    else:
        already_tried()
    return guess


def check_answer(let):
    if let in word:
        pass
    else:
        print(f"Ope, {let} is not in the puzzle!!  ")
        show_puzzle()


def filtered_answer(the_word, the_abcs):
    for letter in the_abcs:
        if letter in the_word:
            the_word = the_word.replace(letter, "_")
    return the_word


def show_puzzle():
    global wrong
    wrong += 1
    pic = pics[wrong]
    print(f"""You have {wrong} wrong answers.  {5 - wrong} to go before hangman!
{pic}
    """)

    return wrong
    
while not wrong >=5:
    # show_puzzle()

    label = tk.Label(text="""Welcome to hangman!! 


                """ + pics[wrong] + """

                Guess this word or DIE!!

                """ + filtered_answer(word, alphabet) + """

                Please enter a letter:

                """
                     )

    entry = tk.Entry()
    # attempt = get_guess(entry)
    # entry_get = entry.get()
    button = tk.Button(win, text="Go ->", command=get_guess)

    # word = get_secret_word()
    # print(the_start(word))
    label.grid(row=0, column=1, padx=10)
    entry.grid(row=2, column=0, padx=10)
    button.grid(row=2, column=2, padx=10)

    #print(f"{filtered_answer(word, alphabet)}")

    if "_" not in filtered_answer(word, alphabet):
        print(f"U win!!! The word was {word}.  You only had {wrong} wrong guesses!")
    elif wrong == 5:
        print(f"Oh no you lost!!  The word was {word}")

    win.mainloop()

