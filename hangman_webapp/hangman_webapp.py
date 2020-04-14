
from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
        'word':"interesting",
        'word_so_far':"-",
        'done':False,
        "chances":6,
        "response":" "}

@app.route('/')
@app.route('/main')
def main():
    return render_template('hangman.html')

@app.route('/start')
def play():
    global state

    state['word']=str(hangman_app.generate_random_word())

    state['guesses'] = []
    l = len(state['word'])
    b = '-'*l
    state['word_so_far'] = b
    return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
    """ plays hangman game """
    global state
    if request.method == 'GET':
        return play()

    elif request.method == 'POST':

        while not state['done']:
            letter = request.form['guess']
            if letter in state['guesses']:
                state['response'] = "You have guessed this letter. Try a knew one."
                state['chances'] -= 1
            elif letter in state['word']:
                s = []
                for n in state['word_so_far']:
                    s += [n]
                counter = -1
                for i in state['word']:
                    counter += 1
                    if i == letter:
                        s[counter] = i
                state['word_so_far'] = "".join(s)
                state['chances'] = state['chances']
                state['response'] = "This is a correct letter!"
                state['guesses'] += [letter]
            elif letter not in state ['word']:
                state['response'] = "You have guessed wrong. Try another letter."
                state['chances'] -= 1
                state['guesses'] += [letter]

            if state['word_so_far'] == state['word']:
                state['response'] = "You have guessed the word! The word is: %s" % state['word']
                state['done'] = True
            elif state['chances'] == 0:
                state['response'] = "You have used up your chances. The word is: %s" % state['word']
                state['done'] = True

            return render_template('play.html',state=state)


@app.route('/about')
def profile():
    return "<h2> This game is made by team Hotpot. (Thanks Zeline for the help!)</h2>"




if __name__ == '__main__':
    app.run('0.0.0.0',port=3000,debug = True)
