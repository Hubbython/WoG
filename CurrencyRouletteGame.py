import random
import requests

def get_money_interval(difficulty):
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    rate = response.json()["rates"]["ILS"]
    random_amount = random.randint(1, 100)
    interval = (random_amount * rate - (5 - difficulty), random_amount * rate + (5 - difficulty))
    return interval, random_amount

def get_guess_from_user(amount):
    while True:
        try:
            guess = float(input(f"Guess the value of {amount} USD in ILS: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play(difficulty):
    interval, amount = get_money_interval(difficulty)
    guess = get_guess_from_user(amount)
    if interval[0] <= guess <= interval[1]:
        print("You won!")
        return True
    else:
        print("You lost.")
        return False
