#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        # Add more questions as tuples (question, answer)
        ("Largest bone in leg?", "femur"),
        ("What planet is known as the Red Planet?", "Mars"),
        ("What gas do plants absorb from the atmosphere during photosynthesis?", "Carbon dioxide"),
        ("What part of the cell contains genetic material?", "Nucleus"),
        ("What force keeps us anchored to the Earth?", "Gravity"),
        ("What is the boiling point of water at sea level in Celsius?", "100°C"),
        ("What organ pumps blood throughout the body?", "Heart"),
        ("What is the process by which a liquid changes into a gas?", "Evaporation"),
        ("What is the hardest natural substance on Earth?", "Diamond"),
        ("What type of energy is stored in food?", "Chemical energy")
    ],
    "Maths" : [
        ("What is 2+2?", "4"),
        ("What is 5-3?", "2"),
        ("What is 3×4?", "12"),
        ("What is 12÷4?", "3"),
        ("What is the square of 5?", "25"),
        ("What is 10 plus 15?", "25"),
        ("What is 100 minus 25?", "75"),
        ("What is 7 times 2?", "14"),
        ("What is half of 20?", "10"),
        ("What is 9 plus 6?", "15")
    ]
}

hints = {
    "Science": [
        # Pair each question with a corresponding hint.
        "starts with H"
        "starts with F"
        "It's named after the Roman god of war.",
        "It's the same thing you breathe out.",
        "It's the cell’s control center.",
        "It's what makes things fall down.",
        "It's a perfect score in most tests.",
        "It's what beats inside your chest.",
        "It's what happens when puddles disappear in the sun.",
        "It's the toughest thing nature can make.",
        "It's the kind of energy your body gets from snacks."
    ],
    # Repeat for other categories as needed.
    "Math" : [
        "multiple of 2"
        "It's the same as adding two pairs."
        "Take away 3 from 5."
        "Think of 3 groups of 4."
        "How many times does 4 go into 12?"
        "Multiply 5 by itself."
        "Add 10 and then 5 more."
        "Subtract 25 from 100."
        "Double 7."
        "Divide 20 by 2."
        "Add 9 and count 6 more."

        ]
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question
    - Add your code here (str) and its corresponding answer (str).
    """
    #------------------------
    x = random.choice(questions[category])
    return x
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    if player_answer == correct_answer:
        return True
    else:
        return False
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    questions[category].remove(question)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    print(question)
    answer = input()
    return answer
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    i = 0
    for i, (q,_) in enumerate(questions[category]:)
        if question == q:
            return hints[category][i]
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    if not check_answer:
        print(question)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------





