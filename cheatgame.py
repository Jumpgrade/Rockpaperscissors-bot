import random
moves = ("rock", "paper", "scissors")
type_chart = {
    "rock": "paper",
    "scissors": "rock",
    "paper": "scissors"
}


def game(move):
    if move.lower() in moves:
        computer_move = moves[random.randint(0, 2)]
        print(f"Computer plays {computer_move}. ")
        weakness = type_chart[move.lower()]
        if computer_move == weakness:
            return f"Computer plays {computer_move}, You Lose!"

        elif computer_move == move.lower():
            return f"Computer plays {computer_move}, You Tied."

        else:
            return f"Computer plays {computer_move}, You Win!"
    else:
        print("It's rock, paper, scissors.")
        return "It's rock, paper, scissors."
