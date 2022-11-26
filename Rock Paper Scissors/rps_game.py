import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        exit = True

    print("Your input is", user_input)
    print("Computer input is", computer_input)
    if user_input == "rock":
        if computer_input == "rock":
            print("It's a tie")
        elif computer_input == "paper":
            print("Computer wins")
            computer_points += 1
        elif computer_input == "scissors":
            print("You win!")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "paper":
            print("It's a tie")
        elif computer_input == "rock":
            print("You win!")
            user_points += 1
        elif computer_input == "scissors":
            print("Computer wins")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "scissors":
            print("It's a tie")
        elif computer_input == "paper":
            print("You win!")
            user_points += 1
        elif computer_input == "rock":
            print("Computer wins")
            computer_points += 1

    elif user_input != "rock" or user_input != "paper" or user_input != "scissors" or user_input != "exit":
        print("Invalid Input!")

print("Your Score:", user_points)
print("Computer Score:", computer_points)

if user_points > computer_points:
    print("Congratulations!! You have scored more points than the computer.")
elif user_points < computer_points:
    print("Better luck next time! You have scored less points than the computer.")
else:
    print("Weird tie at the end!!")

print("Come back next time to have fun!!")
