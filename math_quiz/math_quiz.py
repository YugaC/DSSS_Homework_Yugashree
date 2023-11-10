import random


def random_integer_generate(min, max):
    """
    Generation of a random integer between the minimum and maximum integer value
    """
    return random.randint(min, max)


def random_operator_generate():
    """
    Generation of a random mathematical operator: +,-,*
    """
    
    return random.choice(['+', '-', '*'])


def calc(num1, num2, operator):
    """
    Perform calculation of 2 numbers with an operator
    """
    
    p = f"{num1} {operator} {num2}"
    if operator == '+': result = num1 + num2
    elif operator == '-': result = num1 - num2
    else: result = num1 * num2
    return p, result

def math_quiz():
    score = 0
    total_question = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_question):
        num1 = random_integer_generate(1, 10); 
        num2 = random_integer_generate(1, 5); 
        operator = random_operator_generate()

        PROBLEM, ANSWER = calc(num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")
        
        try:
            useranswer = int(input("Your answer: "))
        
        except ValueError:
            print("Invalid input. Please enter a valid integer")
            continue
            
        
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_question}")

if __name__ == "__main__":
    math_quiz()
