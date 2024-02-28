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
        ("one difference between DNA and RNA",'DNA is doube stranded'),
        ("total number of bones in human body","206"),
        ('what tissue connects muscles to the bones','tendon'),
        ("what is the earth's only natural satellite",'moon'),
        ('what part of the body helps you to move','muscles'),
        ("two holes of nose are called",'nostrils'),
        ('legs have feet and arms have?','hands'),
        ("what part of the plat conducts photosynthesis",'leaf'),
        ("what is the boiling part of water",'100')

    ],"History":[("who is the founder of pakistan,'Quaid e azam"),
                 ("who was the first prime minitser of pakitsn",'liaqat ali khan'),
                 ("who was the first governor of pakistan,'Quaid e azam"),
                 ("who built taj mehal",'shah jahan'),
                 ("when did world war 2 start","1939"),
                 ("who discovered the continent America",'Coloumbus'),
                 ("when did Bangladesh came into existence","1971"),
                 ("pakistan became an indepenedent nation on",'1947'),
                 ("when was the 1st constitution adopted",'1956'),
                 ("who was the first female prime minitser of pakistan"'"benazir bhutto ')
                                                     ]
}

hints = {
    "Science": [('2H2+O2-----?'),
                ('Structural diference'),
                ('more than 200 and less than 210'),
                ('either tendon or ligament'),
                ('the planatery object that apperars at night'),
                ("either bone or muscle"),
                ('either nostrils or mouth'),
                ("hands or tongue"),
                ("leaf or roots"),
                ("between 90-120")
        # Pair each question with a corresponding hint.
    ],"History":[("first governor general"),
                 ("liaqat ali khan or nawaz shareef"),
                 ("founder of paksitan"),
                 ("shah jahan or aurengzeb"),
                 ("between 1920 and 1940"),
                 ("coloumbus or einstein"),
                 ("between 1968 and 1975"),
                 ("beween 1940 and 1950"),
                 ("between 1950 and 1960"),
                 ("daughter of bhutto")]
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question():
    global temp,user_answer,answer
    category = input("Choose S for Science or H for History: ")
    temp = random.randint(1, 9)
    if category.upper() == "S":
        question, answer = questions["Science"][temp - 1]
    elif category.upper() == "H":
        question, answer = questions["History"][temp - 1]
    else:
        print("Invalid category choice.")
        return

    print(question)
    user_answer = input("Please enter your answer: ")
    print("Correct!" if user_answer.lower() == answer.lower() else f"Wrong! The correct answer is {answer}.")


    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #------------------------
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
    # Add your code here
    #------------------------
    print("Correct!" if user_answer.lower() == answer.lower() else f"Wrong! The correct answer is {answer}.")
    #------------------------

#---------------------------------------

def remove_question(category, temp):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    del questions[category][temp-1]
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
    # Add your code here
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
    # Add your code here
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
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------




