import random

def guessing_game():

    secret_number = random.randint(1, 100)

  
    attempts = 0
    max_attempts = 10
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print(f"Guess the number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            guessed_correctly = True
            break
        else:

            if guess < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")

    if guessed_correctly:
        print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
    else:
        print(f"Sorry, you have reached the maximum number of attempts. The correct number was {secret_number}.")

guessing_game()

