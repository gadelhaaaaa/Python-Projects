import random

emojis = { 'r': '🪨', 's': '✂️', 'p': '📃'}
#Escolha entre pedra, papel e tesoura
options = ("r", "p", "s")

while True:
    player = input("Rock, paper or scissor? (r/p/s) ").lower()
    if player not in options:
        print("Incorret Option")
        continue

#Faça o computador escolher uma opcao  
    else:
        machine = random.choice(options)
    
        print(f"The machine chose: {emojis[machine]}")
        print(f"You chose: {emojis[player]}")
    
    #Se o computador escolher a mesma opcao do jogador
        if player == machine:
            print("Draw")
 #Se o jogador escolher entre pedra e o computador tessoura
 #Se o jogador escolher entre papel e o computador pedra
 #Se o jogador escolher entre tesoura e o computador papel   
        elif (
            (player == "r" and machine == "s") or 
            (player == "p" and machine == "r") or 
            (player == "s" and machine == "p")):

#Print Voce Venceu
             print("You WIN!")    
#Caso Contrario
#Print Voce perder        
        else:
            print("You Lose")      
    should_continue = input('Continue? (y/n): ').lower()     
    if should_continue == 'n':
        break     
    