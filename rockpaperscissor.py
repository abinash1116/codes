import random
import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
def game():
    player_score=0
    computer_score=0
    while True:
        while True:
            a=input("Your Choice::Rock , Paper , Scissors ,Quit??").lower() #converts every input to lower case so that the it doesnot invites case sensative error
            if a=="quit": 
                break  #if player input quits then this loop will be closed 
            if a in ["rock","paper","scissors"]: #since we have converted to lowercase you cannot you uppercase element in list else it will throw an error
                break #if the player input any element of this list then this will close the loop
            print("ENTER A VALID INPUT")

        if a=="quit":
            break # And if the player has given input as quit then the loop will be closed and program will not be executed further
        b=random.choice(["rock","paper","scissors"]).lower() #allowing computer to pick random element from the list
        print(f"Computer's Choice::{b}")

        if a==b:
            print("IT'S A DRAW!!")
            speaker.speak("IT'S A DRAW!!")
        elif (a=="rock" and b=="scissors") or (a=="paper" and b=="rock") or (a=="scissors" and b=="paper"):
            print("HURRAYY!!! YOU WON!!")
            speaker.speak("HURRAYY!!! YOU WON!!")
            player_score +=1 #increases the player's score
        elif(a=="rock" and b=="paper") or (a=="paper" and b=="scissors") or (a=="scissors" and b=="rock"):
            print("OPPSSSS!!! YOU LOST PLAY AGAIN!!")
            speaker.speak("OPPSSSS!!! YOU LOST PLAY AGAIN!!")
            computer_score +=1 #increases the computer's score
    print(f"SCORES:\n YOUR SCORE: {player_score}\n COMPUTER'S SCORE: {computer_score}")
    speaker.speak(f"SCORES:\n YOUR SCORE: {player_score}\n COMPUTER'S SCORE: {computer_score}")

    if player_score>computer_score:
        print("YOU ARE A CHAMP")
        speaker.speak("YOU ARE A CHAMP")
    elif computer_score>player_score:
        print("BETTER LUCK NEXT TIME")
        speaker.speak("BETTER LUCK NEXT TIME")
    else:
        print("IT'S A DRAW HEHE")
        speaker.speak("IT'S A DRAW HEHE")

if __name__=="__main__":
    game()

