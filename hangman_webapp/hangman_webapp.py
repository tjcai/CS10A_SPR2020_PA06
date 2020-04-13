"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
         'word':"interesting",
		 'word_so_far':"-----------",
		 'done':False}

@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/start')
def play():
	global state
	state['word']=hangman_app.generate_random_word()
	state['guesses'] = []
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return play()

	elif request.method == 'POST':
		letter = request.form['guess']
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
            counter = -1
            for i in word:
                counter += 1
                if guess == i:
                    raw[counter] = i
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
        # check if letter has already been guessed
		# and generate a response to guess again
		# else check if letter is in word
		# then see if the word is complete
		# if letter not in word, then tell them
		state['guesses'] += [letter]
		return render_template('play.html',state=state)




if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
