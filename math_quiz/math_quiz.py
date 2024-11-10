import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).
    
    Args:
        min_value (int): The minimum value for the random integer.
        max_value (int): The maximum value for the random integer.
    
    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def select_random_operator():
    """
    Select a random arithmetic operator from the list: addition, subtraction, or multiplication.
    
    Returns:
        str: A random operator ('+', '-', '*').
    """
    return random.choice(['+', '-', '*'])


def perform_operation(number_1, number_2, operator):
    """
    Calculate the result of an arithmetic expression based on two numbers and an operator.
    
    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        operator (str): The arithmetic operator ('+', '-', '*').
    
    Returns:
        tuple: A tuple containing the string representation of the expression and its result.
    """
    problem = f"{number_1} {operator} {number_2}"
    if operator == '+': 
        answer = number_1 + number_2
    elif operator == '-': 
        answer = number_1 - number_2
    else: 
        answer = number_1 * number_2

    return problem, answer

def math_quiz():
    """
    Run a math quiz game where users answer randomly generated math problems.
    
    The user will be presented with math problems, and they need to provide the correct answers.
    The score will be displayed at the end of the game.
    """
    # initialize variables
    sum = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = select_random_operator()

        problem, answer = perform_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        while True:
            try:
                user_answer = input("Your answer: ")
                user_answer = int(user_answer)  # Convert input to integer

                if user_answer == answer:
                    print("Correct! You earned a point.")
                    sum += 1
                else:
                    print(f"Wrong answer. The correct answer is {answer}.")
                break  # Exit the loop if input is valid

            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    print(f"\nGame over! Your score is: {sum}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
