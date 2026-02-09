want_instructions = input("Would you like to see the instructions? "). lower()

#check if user says yes/no
if want_instructions == "yes" or want_instructions == "y":
    print("you said yes")

elif want_instructions == "no" or want_instructions == "n":
    print("you said no")
else:
    print("please type yes or no")