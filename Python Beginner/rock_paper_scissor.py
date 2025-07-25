import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"

emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃'}
print()
#Escolha entre pedra, papel e tesoura
options = tuple((emojis.keys()))

def get_user_choice():
    while True:
     player = input("Rock, paper or scissor? (r/p/s) ").lower()
     if player in options:
         return player
     else:
         print("Incorret Option")
         
def display_choices(player, machine):
    print(f"The machine chose: {emojis[machine]}")
    print(f"You chose: {emojis[player]}")     

def determine_winner(player, machine):
 if player == machine:
            print("Draw")
 elif (
    (player == ROCK and machine == SCISSORS) or 
    (player == PAPER and machine == ROCK) or 
    (player == SCISSORS and machine == PAPER)):

    print("You WIN!")           
 else:
    print("You Lose")   
 
def play_game():
                    
    while True:
        player = get_user_choice()
        machine = random.choice(options)
        
        display_choices(player, machine)   

        determine_winner(player, machine)             
        should_continue = input('Continue? (y/n): ').lower()     
        if should_continue == 'n':
            break     
play_game()    