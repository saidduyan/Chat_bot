import random

def calculate_max_attempts(min_range, max_range):
    range_size = max_range - min_range + 1
    max_attempts = range_size.bit_length() - 1
    return max_attempts

def guessing_game():
    print("Welcome to the Guessing Number Game!")

    # Get the range from the player
    min_range = int(input("Enter the minimum number of the range: "))
    max_range = int(input("Enter the maximum number of the range: "))

    # Calculate the maximum number of attempts based on the range
    max_attempts = calculate_max_attempts(min_range, max_range)

    # Generate a random number within the specified range
    secret_number = random.randint(min_range, max_range)

    print(f"I've thought of a number between {min_range} and {max_range}. Try to guess it!")

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess: "))

        if guess < secret_number:
            print("Higher!")
        elif guess > secret_number:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()
