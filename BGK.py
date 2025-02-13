import random

def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors : ")
    computer_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choices)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

def cek_win(player, computer):
    print(f"You Choice { player }, Computer Choice {computer}")
    if player == computer:
        return "It's a Tie"
    elif player == "Rock":
        if computer == "Scissors":
            return "You Win!"
        else:
            return "You Lose!"
    elif player == "Paper":
        if computer == "Rock":
            return "You Win!"
        else:
            return "You Lose!"
    elif player == "Scissors":
        if computer == "Paper":
            return "You Win!"
        else:
            return "You Lose!"

while True:
    choices = get_choices()
    result = cek_win(choices["player"], choices["computer"])
    print(result)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break
    


