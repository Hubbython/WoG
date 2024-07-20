import random

def generate_number(difficulty):
    return random.randint(1, difficulty)

def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Enter a number between 1 and {difficulty}: "))
            if 1 <= guess <= difficulty:
                return guess
            else:
                print(f"Invalid input. Please enter a number between 1 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def compare_results(secret_number, guess):
    return secret_number == guess

def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    if compare_results(secret_number, guess):
        print("You won!")
        return True
    else:
        print("You lost.")
        return False
