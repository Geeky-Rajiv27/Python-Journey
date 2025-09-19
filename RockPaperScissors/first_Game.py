# my plan for the rule :
'''
1 = for rock
2 = for paper
3 = for scissor
'''

import random
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

elif((computer == "rock" and you == "paper") or \
      (computer == "paper" and you == "scissor") or \
      (computer == "scissor" and you == "rock")):
        print("                                                                                         [You won]")
     
else:
        print("                                                                                         [you lose]")