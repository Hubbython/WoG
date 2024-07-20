from flask import Flask, render_template, request, session
from Live import welcome
from GuessGame import generate_number, compare_results
from MemoryGame import generate_sequence, is_list_equal
from CurrencyRouletteGame import get_money_interval
from Score import add_score

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome_user():
    name = request.form['name']
    session['name'] = name
    welcome_message = welcome(name)
    return render_template('welcome.html', welcome_message=welcome_message)

@app.route('/load_game')
def load_game_route():
    return render_template('load_game.html')

@app.route('/play_game', methods=['POST'])
def play_game():
    game_choice = int(request.form['game_choice'])
    difficulty = int(request.form['difficulty'])
    session['difficulty'] = difficulty

    if game_choice == 1:
        sequence = generate_sequence(difficulty)
        session['sequence'] = sequence
        return render_template('memory_game.html', sequence=sequence)
    elif game_choice == 2:
        secret_number = generate_number(difficulty)
        session['secret_number'] = secret_number
        return render_template('guess_game.html')
    elif game_choice == 3:
        interval, amount = get_money_interval(difficulty)
        session['interval'] = interval
        session['amount'] = amount
        return render_template('currency_roulette_game.html', amount=amount)

@app.route('/memory_game_result', methods=['POST'])
def memory_game_result():
    sequence = session['sequence']
    try:
        user_sequence = list(map(int, request.form['user_sequence'].split()))
    except ValueError:
        error_message = 'Invalid input! Please enter a sequence of integers.'
        return render_template('memory_game.html', sequence=sequence, error_message=error_message)

    result = is_list_equal(sequence, user_sequence)
    if result:
        add_score(session['difficulty'])  # Update score if the user wins
    return render_template('result.html', result=result)

@app.route('/guess_game_result', methods=['POST'])
def guess_game_result():
    user_guess = int(request.form['user_guess'])
    secret_number = session['secret_number']
    result = compare_results(secret_number, user_guess)
    if result:
        add_score(session['difficulty'])  # Update score if the user wins
    return render_template('result.html', result=result)

@app.route('/currency_roulette_game_result', methods=['POST'])
def currency_roulette_game_result():
    user_guess = float(request.form['user_guess'])
    interval = session['interval']
    result = interval[0] <= user_guess <= interval[1]
    if result:
        add_score(session['difficulty'])  # Update score if the user wins
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
