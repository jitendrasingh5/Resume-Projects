from getpass import getpass as input
import os
import time
print()


s1 =0
s2 =0
while True:
  t = "R ⛰️, P 📃, S ✂️"
  print(f"{t:^38}")
  print()

  p1 = input("Player 1 : "). capitalize()
  p2 = input("Player 2 : ").capitalize()
  print()
  
  if p1 == "R":
    if p2 == "R":
      print("Rock vs Rock, it's a tie.")
    elif p2 == "P":
      print("Paper covers Rock, Player 2 wins")
      s2 += 1
    elif p2 == "S":
      print("Rock crushes Scissor, Player 1 wins")
      s1 += 1
    else:
      print("Invalid input")
  elif p1 == "P":
    if p2 == "R":
      print("Paper covers Rock, Player 1 wins")
      s1 += 1
    elif p2 == "P":
      print("Paper vs Paper, it's a tie.")
    elif p2 == "S":
      print("Scissor cuts Paper, Player 2 wins")
      s2 += 1
    else:
      print("Invalid input")
  elif p1 == "S":
    if p2 == "R":
      print("Rock crushes Scissor, Player 2 wins")
      s2 += 1
    elif p2 == "P":
      print("Scissor cuts Paper, Player 1 wins")
      s1 += 1
    elif p2 == "S":
      print("Scissor vs Scissor, it's a tie.")
    else:
      print("Invalid input")
  else:
    print("Invalid input")
    
  print()
  print(f"Player 1 score : {s1}")
  print(f"Player 2 score : {s2}")
  print()
  

  if s1 == 3:
    print("Player 1 won the game")
    print()
    replay =input("Play Again? : ").upper()
    if replay.upper() == "YES":
      s1 = 0
      s2 = 0
      time.sleep(3)
      os.system("clear")
      continue
    else:
      print("Thanks for playing")
      break
  elif s2 == 3:
    print("Player 2 won the game")
    print()
    replay =input("Play Again? : ").upper()
    if replay.upper() == "YES":
      s1 = 0
      s2 = 0
      time.sleep(3)
      os.system("clear")
      continue
    else:
      print("Thanks for playing")
      break

    
    

      

      
      


      






  time.sleep(2)
  os.system("clear")
  