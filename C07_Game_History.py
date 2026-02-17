# Initialise list to hold game history
game_history = []

# get data (base component does this already, code below for testing purposes)
user_score = 0
comp_score = 0

while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break

    user_points = int(input("User points? "))
    comp_points = int(input("Computer points? "))
    winner = input("Who won? ")
    user_score = int(input("User score: "))
    comp_score = int(input("Computer score: "))

    game_results = (f"round {rounds_played} : user points {user_points} | "
                f"computer points {comp_points}, {winner} wins ({user_score} | {comp_score})")

    game_history.append(game_results)

print("game history")

for item in game_history:
    print(item)