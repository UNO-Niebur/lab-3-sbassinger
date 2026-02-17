#RPS.py
#Name:Scott Bassinger
#Date:02/16/2026
#Assignment:Lab3-RPS
import random
import time

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  playAgain = "Y"
  while playAgain == "Y":
    print("Let's play Rock, Paper, Scissors! ")
    time.sleep(1)
    #Randomly choose the computer between 'R', 'P', or 'S'
    computerChoice = random.choice(["R", "P", "S"])
    #Prompt the user for their RPS selection
    userChoice = input("Choose your weapon! (R, P, S) ")
    if userChoice not in ["R", "P", "S"]:
      print("Sorry, the only acceptable values are R, P, or S!")

    else:
      time.sleep(1)
      #Determine winner and state what happened to the user
      if userChoice == computerChoice:
        print("It's a tie! You and the computer both chose", computerChoice)
        ties += 1
      elif userChoice == "R" and computerChoice == "S":
        print("The computer chose", computerChoice, "You win!")
        wins += 1
      elif userChoice == "P" and computerChoice == "R":
        print("The computer chose", computerChoice, "You win!")
        wins += 1
      elif userChoice == "S" and computerChoice == "P":
        print("The computer chose", computerChoice, "You win!")
        wins += 1
      else:
          print("The computer chose", computerChoice, "You lost!")
          losses += 1

      time.sleep(1.5)
      #In the end, print the stats
      print("Wins \t Ties \t Losses")
      print("---- \t ---- \t ------")
      print(wins, "\t", ties , "\t", losses)
      #Ask the user if they would like to play again.
      playAgain = input("Would you like to play again?(Y/N)")
      time.sleep(0.5)

if __name__ == '__main__':
  main()
