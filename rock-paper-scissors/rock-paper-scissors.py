import random

choices = ["rock", "paper", "scissors"]
player_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print(f"Computer chose: {computer_choice}")

if player_choice in choices:
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid choice")
