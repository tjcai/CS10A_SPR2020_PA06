import random

def play_hangman():
    one_more_time = True

    while one_more_time:
        guessed_letters = []
        guess_left = 6
        word_list = "python property happy lovely".split()
        word = random.choice(word_list)
        word_li = list(word)
        done = False

        raw = []
        for a in range(len(word_li)):
            raw.append('-')

        while not done:

            print("-----------")
            print(raw)
            print(guess_left, "chances left")
            guess = input("pick a letter: ")

            if guess in guessed_letters:
                """Repeated guessing"""
                guess_left -= 1
                print("You've already guessed this letter. Try a new one.")

            elif guess not in word_li:
                """Wrong guess"""
                guess_left -= 1
                guessed_letters.append(guess)
                print("This letter is not in the word. Please try a new one")

            elif guess in word_li:
                """Correct Guess"""
                s = num_place(word_li,guess)
                if len(s) == 1:
                    """Only one correct letter in the random word"""
                    raw[s[0]] = guess
                else:
                    """More than one correct letter in the random word"""
                    for m in s:
                        raw[m] = guess
                guess_left = guess_left
                guessed_letters.append(guess)

            if raw == word_li:
                """Correct Guess."""
                print(raw)
                print("Congratualation! You won!")
                done = True
            elif guess_left == 0:
                """No more chances."""
                print(raw)
                print("Sorry, you have used up all the chances.")
                print("The word is: ",word)
                done = True

        """Ask whether to play another game."""
        one_more_time = input("Do you want to play again? [Y]es or [N]o")
        if one_more_time.upper() == "Y":
            one_more_time = True
        else:
            one_more_time = False

def num_place(word_list,letter):
    """This function is used to determine the position of the letter guessed in the word randomly chosen."""
    a = len(word_list)
    n = []
    for m in range(a):
        if word_list[m] == letter:
            n.append(m)
    return n

play_hangman()
