# Rock Paper Scissors Game 

import random
print("!!ROCK PAPER SCISSORS GAME !!")

user_score = 0
computer_score = 0

while True:

    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")
        user_score += 1

    elif user_choice in choices:
        print("Computer Wins!")
        computer_score += 1

    else:
        print("Invalid Input!")

    print("\nCurrent Scores")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play = input("\nDo you want to continue? (yes/no): ").lower()
    if play == "no":
        print("\nFinal Scores")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        print("Thanks for Playing!")
        break