import random

def game():
    player_score = 0
    computer_score = 0
    while True:
        while True:
            a = input("Your Choice: Rock, Paper, Scissors, or Quit? ").lower() #converts every input to lower case to minimize case sensative error
            if a =="quit":
                break #if player input quits then this loop will be closed 
            if a in ["rock", "paper", "scissors"]:
                break #if the player input any element of this list then this will close the loop
            print("ENTER A VALID INPUT")

        if a == "quit":
            break # And if the player has given input as quit then the loop will be closed and program will not be executed further

        
        b = random.choice(["rock", "paper", "scissors"]).lower()  #allowing computer to pick random element from the list
        print(f"Computer's Choice: {b}")

        if a==b:
            print("IT'S A DRAW!TRY AGAIN")
        elif (a=="rock" and b=="scissors") or (a=="paper" and b=="rock") or (a=="scissors" and b=="paper"):
            print("HURRAYY!!! YOU WON!!")
            player_score +=1
        elif(a=="rock" and b=="paper") or (a=="paper" and b=="scissors") or (a=="scissors" and b=="rock"):
            print("OPPSSSS!!! YOU LOST PLAY AGAIN!!")
            computer_score +=1


    print(f"SCORES:\n YOUR SCORE:{player_score}\n COMPUTER'S SCORE{computer_score}")

    if player_score>computer_score:
        print("YOU ARE A CHAMP")
    elif computer_score>player_score:
        print("BETTER LUCK NEXT TIME")
    else:
        print("IT'S A DRAW HEHE")

if __name__=="__main__":
    game()
