
#---------------------------------------
#  Game Mechanics
#    Student A (team lead)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    # Add your code here
    print("Welcome to Grade 8 Plays")
    #------------------------
    #------------------------
#---------------------------------------

def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    for i in range(len(categories)):
        print(i,".", categories[i])
    temp = int(input("Enter a given integer to select a category:"))
    category = categories[temp]
    return category
    #------------------------
    #------------------------

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.
    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.
    Returns: None
    """
    #------------------------
    print("current score: ", score)
    print("round number: ", round_number)
    #------------------------
    #------------------------

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    print("Game Over")
    print("Your final score: ", final_score)
    #------------------------
    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------
    for i in range(0,5):
        chosen_category = choose_category(categories)
        question, correct_answer = display_question_and_accept_answer(question)
        correct = validate_answer(player_answer, correct_answer)
        score = update_score(score, correct)
        display_score(score, round_number)
        next_round(round_number)
        remove_question(chosen_category, question)
#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    if player_answer == correct_answer:
        correct = True
    else:
        correct = False
    return correct
    #------------------------
    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    #------------------------
    if correct:
        score += 10
    return score
    #------------------------
    #------------------------

#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    #------------------------
    round_number += 1
    #------------------------
    #------------------------

#---------------------------------------

def check_game_over(incorrect_answers, final_score):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    #------------------------
    if incorrect_answers >= 3:
        game_over_message(final_score)
        return True
    elif incorrect_answers < 3:
        return False
    #------------------------
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    #------------------------
    list = ["Restart","Exit"]
    for i in range(len(list)):
        print(i, list[i])
    temp = int(input("Enter: "))
    if temp == 0:
        main()
    elif temp ==1:
        print("Thanks for playing!")
        break
    #------------------------
    #------------------------

#---------------------------------------
