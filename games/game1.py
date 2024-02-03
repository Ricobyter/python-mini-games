import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value) 

    return roll

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
        else:
            print("Invalid number.Enter a number between 2 and 4")
    
    else:
        print("Invalid entry. Enter a valid number")

max_score = 50

player_scores = [0 for _ in range(len(players))]

while max(player_scores) < max_score:
    should_roll  = input("would you like to rolll (y): ")
    if should_roll.lower() != "y":
        break

    value = roll()




