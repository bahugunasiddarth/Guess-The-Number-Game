from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
answer = random.randint(1, 100)
attempts_left = 10

@app.route('/')
def index():
    global attempts_left
    return render_template('index.html', attempts_left=attempts_left, message="")

@app.route('/guess', methods=['POST'])
def guess():
    global answer, attempts_left

    if attempts_left > 0:
        user_guess = int(request.form['guess'])
        attempts_left -= 1
        
        if user_guess > answer:
            message = "Too high!"
        elif user_guess < answer:
            message = "Too low!"
        else:
            message = f"Correct! The number was {answer}. Restarting the game."
            answer = random.randint(1, 100) 
            attempts_left = 10
            return redirect(url_for('index'))
    else:
        message = f"You've run out of attempts! The number was {answer}. Restarting the game."
        answer = random.randint(1, 100) 
        attempts_left = 10

    return render_template('index.html', attempts_left=attempts_left, message=message)

if __name__ == "__main__":
    app.run(debug=True)
