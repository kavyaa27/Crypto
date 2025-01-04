import random

def start_game():
    print("Welcome to the Unexpected Guessing Game!")
    print("I will think of a number, and you have to guess it.")
    print("The catch: The range of numbers might change unexpectedly!")
    
    # Define the initial range
    min_num = 1
    max_num = 10
    secret_number = random.randint(min_num, max_num)

    while True:
        try:
            guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
            if guess < min_num or guess > max_num:
                print(f"Your guess is out of range! Please guess between {min_num} and {max_num}.")
            elif guess < secret_number:
                print("Too low! But watch out, the range might change!")
            elif guess > secret_number:
                print("Too high! But I might change the range soon!")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                break

            # Randomly change the range to keep it unpredictable
            if random.random() < 0.3:  # 30% chance to change the range
                min_num = random.randint(1, 50)
                max_num = random.randint(min_num + 1, 100)
                secret_number = random.randint(min_num, max_num)
                print(f"Surprise! The range has changed to {min_num} to {max_num}.")

        except ValueError:
            print("Oops! Please enter a valid number.")

# Start the game
start_game()
