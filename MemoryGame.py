import random
import time

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    print(f"Please enter {difficulty} numbers separated by spaces:")
    while True:
        try:
            user_input = list(map(int, input().split()))
            if len(user_input) == difficulty:
                return user_input
            else:
                print(f"Invalid input. Please enter exactly {difficulty} numbers.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def is_list_equal(sequence, user_sequence):
    return sequence == user_sequence

def play(difficulty):
    sequence = generate_sequence(difficulty)
    print(f"Remember this sequence: {sequence}")
    time.sleep(0.7)
    print("\r\t", end="")  # Clear the screen
    user_sequence = get_list_from_user(difficulty)
    if is_list_equal(sequence, user_sequence):
        print("You won!")
        return True
    else:
        print("You lost.")
        return False
