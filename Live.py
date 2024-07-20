def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 0.7 seconds and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    while True:
        try:
            game_choice = int(input("Enter the number of the game you want to play: "))
            if game_choice < 1 or game_choice > 3:
                print("Invalid choice. Please choose a number between 1 and 3.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if difficulty < 1 or difficulty > 5:
                print("Invalid choice. Please choose a number between 1 and 5.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if game_choice == 1:
        from MemoryGame import play
    elif game_choice == 2:
        from GuessGame import play
    elif game_choice == 3:
        from CurrencyRouletteGame import play

    play(difficulty)
