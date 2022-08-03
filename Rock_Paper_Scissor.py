import random

choices={ "Rock" : 1, "Paper" : 2, "Scissor":3}
def user_input():
  return int(input("""
  Please enter your choice 
  Rock : 1
  Paper : 2
  Scissor : 3
  """))

def Computer_turn():
  return random.randint(1,3)

def game(score:int):
  user=user_input()
  print("User : ",user)
  computer= Computer_turn()
  print("Computer : ",computer)
  if((user == choices["Rock"] and computer == choices["Scissor"]) or
    (user == choices["Paper"] and computer == choices["Rock"])or
    (user == choices["Scissor"] and computer == choices["Paper"])):
      score += 1
  elif (( computer== choices["Rock"] and user == choices["Scissor"]) or
    (computer == choices["Paper"] and user == choices["Rock"])or
    (computer == choices["Scissor"] and user == choices["Paper"])):
    score -= 1
  return score


#----------------------------
if __name__=="__main__":

  player1=game(3);
  player2=game(3);

  if(player1 > player2): 
    print("Player1 Won with score",player1)
  elif(player2 > player1):
    print("Player2 Won with score",player2)
  else:
    print("Drawn")
