#Part B : Game
import random
def guessing_game():
    # Part 1 : guessing game
    lower_bound = 1
    upper_bound = 99
    target_number = random.randint(lower_bound, upper_bound)
    
    print(f"Welcome to the Guessing Game My charos! Guess a number between {lower_bound} and {upper_bound} my friend.")
    
    while True:
        try:
            user_guess = int(input("Guess a number: "))
            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
            elif user_guess < target_number:
                print("Too low! Try again hahah.")
            elif user_guess > target_number:
                print("Too high! Try again hahah.")
            else:
                print(f"Congratulations! You guessed the correct number, Your are genius my friend: {target_number}.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number and give another shot.")

# Part 2 : Rock, paper and scissor game
def rock_paper_scissors_game():
    choices = ["rock", "paper", "scissors"]
    
    print("Welcome And kuzuzangpo To The Rock Paper Scissors Game !")
    
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        if user_choice == "quit":
            print("Thanks for playing charo! Goodbye and have a nice day!")
            break
        elif user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie  bro( -_-)!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win(^__^)!")
        else:
            print("You lose ( - -)!")

def main():
    while True:
        print("\nSelect a number to play a game(2, 4 or 6):")
        print("2. Guess Number Game")
        print("4. Rock Paper Scissors Game")
        print("6. Exit Program")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 2:
                guessing_game()
            elif choice == 4:
                rock_paper_scissors_game()
            elif choice == 6:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()