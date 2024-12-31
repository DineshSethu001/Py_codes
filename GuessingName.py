import random

def play_game():
    print("Hai! Shall we play a number guessing game?")
    cx = input("Enter your opinion here (yes/no): ").strip().lower()

    if cx == "yes":
        print("Okay! Let me start the game. You need to find the number that I guessed.")
        GuessedNumber = random.randint(1, 20)  # Random number between 1 and 20

        for guessesTaken in range(1, 6):
            try:
                Player_number = int(input(f"Attempt {guessesTaken}: Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if Player_number > GuessedNumber:
                print("You are too high!")
            elif Player_number < GuessedNumber:
                print("You are too low!")
            else:
                print(f"Yes, you are correct! You found the number in {guessesTaken} attempt(s).")
                break
        else:
            print(f"Sorry, you've used all attempts. The correct number was {GuessedNumber}.")

        replay()
    else:
        print("Okay, I think you're not in the mood to play. See you next time! :)")

def replay():
    print("Shall we play once more?")
    playerWish = input("Enter your wish here (yes/no): ").strip().lower()
    if playerWish == "yes":
        play_game()
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
play_game()
