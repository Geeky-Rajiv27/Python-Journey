import random

computer_number = random.randint(1, 100)
guess_no = 0
Guess = 0
while(Guess != computer_number):
   
   
    Guess = int(input("Enter your guess : "))


    if(Guess > computer_number):
        print("Little bit smaller 🫨")
        print("Your guess is not correct\n")
        guess_no += 1
        
    else:
        print("Little bit greater 🫨")
        print("Your guess is not correct\n")
        guess_no += 1

print("Congratulation - 💐, Your guess is correct\n")
print(f"Total no of guesses you used : {guess_no}")


