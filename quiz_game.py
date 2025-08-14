from termcolor import colored


def ask_question(question_text, options_dict, correct_letter):
    print()
    print(question_text)
    for letter, text in options_dict.items():
        print(f"{letter}. {text}")

    while True:
        answer = input("Your answer (A-D): ").strip().upper()
        if answer in options_dict:
            break
        print("Please enter A, B, C, or D.")

    if answer == correct_letter:
        print(colored("Correct!", "green"))
        return True
    else:
        print(colored("Wrong!", "red"))
        return False


def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
            "answer": "C",
        },
        {
            "question": "Which planet is known as the red planet?",
            "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
            "answer": "B",
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": {"A": "Atlantic", "B": "Indian", "C": "Arctic", "D": "Pacific"},
            "answer": "D",
        },
    ]

    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print()
    print(f"Score: {score}/{len(questions)}")


if __name__ == "__main__":
    main()