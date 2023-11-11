import random

def get_random_number(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)
def random_operation():
    return random.choice(['+', '-', '*'])
def create_question(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a  

def math_quiz():
    s = 0
    t_q = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = get_random_number(1, 10); n2 = get_random_number(1, 5); o = random_operation()

        PROBLEM, ANSWER = create_question(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
