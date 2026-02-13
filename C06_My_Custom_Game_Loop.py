#At the start of he game, the computer and user score are both zero

user_score = 0
comp_score = 0

game_goal = int(input("What's the Game Goal? "))     #Should be a function call!

#Play multiple rounds until a winner is found

    #Start of the round loop
    #For testing purposes, ask the user what the points for the user and computer were
while True:
    user_points = int(input("What was user points? "))
    comp_points = int(input("What was Comp points? "))

    #Outside rounds loop - update score with round points, only add points to the score of the winner
    if comp_points < user_points:
        winner = "User"

    if user_points < comp_points:
        winner = "Comp"

    if winner == "User":
        user_score = user_score + user_points

    if winner == "Comp":
        comp_score = comp_score + comp_points

    #Show overall scores (Add this to rounds loop)

    print(f"\nWinner is {winner}")
    print(f"\nScores are: User, {user_score} | Comp, {comp_score}")


    #End of entire game, output final results
    if user_score >= game_goal:
        game_winner = "user"
        break
    elif comp_score >= game_goal:
        game_winner = "Comp"
        break

print(f"\nGame winner is... {game_winner}!!")



