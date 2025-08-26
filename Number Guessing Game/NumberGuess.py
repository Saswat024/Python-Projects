import random

computerNumber = random.randint(1, 100)
userNumber = int(input("Guess a Number between 1 and 100 inclusive (You have 10 attempts left): "))
attempts = 10
won = False

while(attempts != 0):
    if computerNumber == userNumber:
        print("Congratulations! You have successfully guessed the number.")
        print(f"Remaining tries: {attempts}")
        won = True
        break
    
    attempts -= 1
    
    if userNumber > computerNumber and attempts > 0:
        print(f"Too High. Try again. (Remaining tries: {attempts})")
        
    elif userNumber < computerNumber and attempts > 0: 
        print(f"Too Low. Try again. (Remaining tries: {attempts})")
        
    if attempts > 0:
        userNumber = int(input("Guess again: "))
    

print(f"OOPS!! You have ran out of attempts. The number was {computerNumber}") if not won else ""
