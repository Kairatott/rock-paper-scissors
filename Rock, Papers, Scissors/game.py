import random

computer = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
x = input("Select your pick: ")
y = computer[random.randint(0,2)]

for i in range(3):
  print(".\n")

print(f"Your pick is {x}.")
print(f"Computer pick is {y}.\n")

if x.lower() == y:
  print("Tie!")
elif x.lower() == "rock" and y == "paper":
  print("Computer wins!")
elif x.lower() == "rock" and y == "scissors":
  print("You win!")
elif x.lower() == "paper" and y == "rock":
  print("You win!")
elif x.lower() == "paper" and y == "scissors":
  print("Computer wins!")
elif x.lower() == "scissors" and y == "rock":
  print("Computer wins!")
elif x.lower() == "scissors" and y == "paper":
  print("You win!")
else:
  print("Error occurred.")