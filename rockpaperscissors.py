import random

choices = {
    "rock": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
"paper": '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
"scissors":'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}

userChoice = input("rock? paper? scissors? ")
compChoice = random.choice(list(choices.keys()))

print(f"You choose: userChoice {choices[userChoice]}")
print(f"The computer choose: userChoice {choices[compChoice]}")

if userChoice == "rock" and compChoice == "paper":
    print("Computer Wins!")
elif userChoice == "paper" and compChoice == "paper":
    print("DRAW")
elif userChoice == "scissors" and compChoice == "paper":
    print("You Win!")
elif userChoice == "rock" and compChoice == "rock":
    print("DRAW")
elif userChoice == "paper" and compChoice == "rock":
    print("You Win!")
elif userChoice == "scissors" and compChoice == "rock":
    print("Computer Wins!")
elif userChoice == "rock" and compChoice == "scissors":
    print("You Win!")
elif userChoice == "paper" and compChoice == "scissors":
    print("Computer Wins!")
elif userChoice == "scissors" and compChoice == "scissors":
    print("DRAW")