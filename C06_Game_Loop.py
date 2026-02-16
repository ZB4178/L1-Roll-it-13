#At the start of he game, the computer and user score are both zero
user_score = 0
comp_score = 0

game_goal = int(input("What's the Game Goal? "))     #Should be a function call!

#Play multiple rounds until a winner is found
while comp_score < game_goal and user_score < game_goal:

    #Start of the round loop
    #For testing purposes, ask the user what the points for the user and computer were
    comp_points = int(input("Enter the computer points at the end of the round: "))
    user_points = int(input("Enter the user points at the end of the round: "))

    #Outside rounds loop - update score with round points, only add points to the score of the winner
    comp_score += comp_points
    user_score += user_points

    #Show overall scores (Add this to rounds loop)
    print("*** Game Update ***") # Replace with call to statement generator
    print(f"User Score: {user_score} | Computer Score: {comp_score}")

#End of entire game, output final results
print()
if user_score > comp_score:
    print("The user won") # Replace this with Statement generator call
else:
    print("The Computer Won")
