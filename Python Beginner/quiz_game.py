# Primeiro, certifique-se de ter a biblioteca termcolor instalada.
# Se não tiver, abra o terminal e digite: pip install termcolor

from termcolor import cprint

def quiz_game():
    """
    Função principal que executa o Quiz Game de Geografia com 3 questões
    e mostra o placar final.
    """
    score = 0  # Variável para armazenar a pontuação
    total_questions = 3

    print("--- Bem-vindo ao Quiz de Geografia! ---")
    print("Responda às seguintes 3 perguntas.\n")

    # --- Questão 1 ---
    print("Questão 1: What is the capital of France?")
    print("A. Berlin")
    print("B. Madrid")
    print("C. Paris")
    print("D. Rome")

    resposta1 = input("Sua resposta (A, B, C ou D): ")

    if resposta1.upper() == 'C':
        cprint("Correto!", 'green')
        score += 1  # Incrementa o score
    else:
        cprint("Wrong!", 'red')
    
    print("-" * 20)

    # --- Questão 2 ---
    print("\nQuestão 2: Which planet is known as the red planet?")
    print("A. Earth")
    print("B. Mars")
    print("C. Jupiter")
    print("D. Saturn")

    resposta2 = input("Sua resposta (A, B, C ou D): ")

    if resposta2.upper() == 'B':
        cprint("Correto!", 'green')
        score += 1  # Incrementa o score
    else:
        cprint("Wrong!", 'red')

    print("-" * 20)

    # --- Questão 3 ---
    print("\nQuestão 3: What is the largest ocean on Earth?")
    print("A. Atlantic")
    print("B. Indian")
    print("C. Arctic")
    print("D. Pacific")

    resposta3 = input("Sua resposta (A, B, C ou D): ")

    if resposta3.upper() == 'D':
        cprint("Correto!", 'green')
        score += 1  # Incrementa o score
    else:
        cprint("Wrong!", 'red')
    
    # --- Fim do Jogo e Placar Final ---
    print("\n" + "=" * 25)
    cprint("       QUIZ OVER!", 'yellow')
    print("=" * 25)
    # Usando f-string para formatar a mensagem do placar
    print(f"\nSeu score final é: {score} de {total_questions}!")
    print("\nObrigado por jogar.")


# Inicia o jogo
if __name__ == "__main__":
    quiz_game()