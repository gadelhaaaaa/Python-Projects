import random

#Gere um numero entre 1 e 100
secret_number = random.randint(1, 100)

while True:
 try:
    guess = int(input("Guess the number betwwen 1 and 100: "))
    if guess < 1 or guess > 100:
        print("Invalid, try again")    
    elif guess > secret_number:    
        print("Too High!")
    elif guess < secret_number:
        print("Too Low!")   
    else:
        print("Congratulations! You guessed the number.")  
        break
 except ValueError:  
     print("Pleaser, enter a valid number")
  