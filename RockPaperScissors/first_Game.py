# my plan for the rule :
'''
1 = for rock
2 = for paper
3 = for scissor
'''

import random
import os

def game():     #------------------------function

    symbol = ["rock", "paper", "scissor"]
    computer = random.choice(symbol)
    print("----------------------------|")
    print("      Rock Paper Scissor    |")
    print("----------------------------|")
    print(" Press (R) for Rock\n Press (P) for paper\n Press (S) for scissor")
    print("----------------------------|")


    #using switch case 
    you = input("Enter your choice: ")

    match you :
        case 'R':
            you = "rock"

        case 'P':
            you = "paper"

        case 'S':
            you = "scissor"

        case _:
            print("                                                                                         [Wrong input !]")
            exit() # stops the further execution of program

  
    

    print(f"                                    computer = {computer} and you = {you}")
    
    if(computer == you):
        
        print("                                                                                             [Game Draw !]")
        return 0

    elif((computer == "rock" and you == "paper") or \
        (computer == "paper" and you == "scissor") or \
        (computer == "scissor" and you == "rock")):
            print("                                                                                         [You won]")
            return 1 + game()
     
    else:
            print("                                                                                         [you lose]")
            return 0
            

  


'''
-----------------------------------------------------------------------------------------
    adding a high score storing feature to the game (ROCK PAPER & SCISSORS) 
-----------------------------------------------------------------------------------------
'''
#reading previous highscore from the file using exception handling:
previousHighscore_file_name = '/Users/bheshu/Documents/PythonFull/RockPaperScissors/highscore.txt'
if(os.path.exists(previousHighscore_file_name)):
     with open("/Users/bheshu/Documents/PythonFull/RockPaperScissors/highscore.txt", "r") as readFile:
       try:
              previousHighscore = int(readFile.read())
       except ValueError as e:
            print(f"An {e} error is caught !")
else:
     previousHighscore = 0 
            
score = game()          #this will return (score)

if(score > previousHighscore):
    #writing the highscore in the file
    with open("/Users/bheshu/Documents/PythonFull/RockPaperScissors/highscore.txt" , "w") as writefile:
        writefile.write(str(score))



#----------------function boundary----------------------



