import random

def roll():
    min_val = 1
    max_value = 6
    roll = random.randint(min_val, max_value)
    return roll

while True:
    players = input("Enter number of players(1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Must be between 1-4 players")
    else:
        print("INVALID - Try Again")

print(players)
max_score = 100
players_score = [0 for i in range(players)]

while max(players_score) < max_score:
    for i in range(players):
        print("\nPlayer number", i + 1, "turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (yes/no)? ")

            if should_roll.lower() == "no":
                break

            value = roll()

            if value == 1:
                print("You rolled 1! You are done.")
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        players_score[i] += current_score
        print("Your total score is:", players_score[i])

        if players_score[i] >= max_score:
            break
    if players_score[i] >= max_score:
        break

