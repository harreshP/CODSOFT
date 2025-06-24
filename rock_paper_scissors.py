import random
def get_computer_choice():
  return random.choice(["rock","paper","scissors"])
def get_winner(user,computer):
  if user==computer:
    return "it's a tie!"
  elif (user=="rock" and computer=="scissors")or \
       (user=="scissors" and computer=="paper" )or \
       (user=="paper" and computer=="rock"):
    return"you win!"
  else:
    return "computer wins!"
def play_game():
  user_score=0
  computer_score=0

  while True:
    print("\nchoose rock,paper,or scissors:")
    user_choice=input("your choice:").lower()

    if user_choice not in ["rock","paper","scissors"]:
      print("invalid choice.try again.")
      continue

    computer_choice=get_computer_choice()
    print(f"computer choose:{computer_choice}")

    result=get_winner(user_choice,computer_choice)
    print(result)

    if "you win" in result:
      user_score+=1
    elif "computer wins" in result:
      computer_score+=1

    print(f"score → you:{user_score}|computer:{computer_score}")
    
    play_again=input("do you want to play again?(yes/no):").lower()
    if play_again!="yes":
      print("thanks for playing!")
      break
play_game()
  
    
