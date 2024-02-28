#---------------------------------------
#  User Experience
#    Student C
#---------------------------------------


#---------------------------------------

def choose_difficulty():
    """
    Allows players to choose the difficulty level of the questionsThe user is going to input their choice.

    Parameters: None
    Returns:
    - str: Valid difficulty levels are ('easy', 'medium', 'hard').
    """
    #------------------------
    total_points: 300
    d_level= input("please, choose the difficulty level (EASY, MEDIUM, HARD): ")

    if d_level == "easy":
        points =  total_points * 1.5
    elif d_level == "medium":
        points = total_points * 1.0
    elif d_level == "hard":
        points = total_points * 0.5

    return int(points)


    #------------------------

    #------------------------

#---------------------------------------

def display_leaderboard(leaderboard):
    """
    Displays the leaderboard, showing top scores in descending order.

    Parameters:
    - leaderboard (dict): A dictionary containing player names as keys and their scores as values.

    Returns: None

    The function sorts the leaderboard by scores in descending order and prints the names and scores of the top players. If the leaderboard is empty, it prints a message indicating that there are no scores to display.
    """
    #------------------------
    if not leaderboard:
        print("there are no scores to display")
        return
    decend_board = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

    print("LEADERBOARD")
    for player_name, score in leaderboard.items():
        print(f"(player_name): (score) points")

    #------------------------

    #------------------------

#---------------------------------------

def save_score(player_name, score, file_path='scores.txt'):
    """
    Saves the player's score to a file.

    Parameters:
    - player_name (str): The name of the player.
    - score (int): The score achieved by the player.
    - file_path (str): The file path to save the score.

    Returns: None
    """
    #------------------------
    with open(file_path,"a") as file:
        file.write(f"{player_name}: {score} points\n")
        print("score saved successfully!")
    #------------------------
    
    #------------------------

#---------------------------------------

def load_top_scores(file_path='scores.txt'):
    """
    Loads the top scores from a file into a leaderboard dictionary.

    Parameters:
    - file_path (str): The file path from which to load the scores.

    Returns:
    - dict: The leaderboard dictionary with player names as keys and scores as values.
    """
    #------------------------
    # Add your code here
    #------------------------
    
    #------------------------

#---------------------------------------

def provide_feedback(is_correct):
    """
    Provides feedback to the player after each round.

    Parameters:
    - is_correct (bool): Indicates whether the player's answer was correct.

    Returns: None

    Example:
    - is it correct?   "Well done!"
    - is it incorrect? "Sorry, that's incorrect."
    """
    #------------------------
    if is_correct:
        print("Well done!")
    else:
        print("Sorry, that's incorrect.")
    #------------------------
    
    #------------------------

#---------------------------------------

def fifty_fifty_lifeline(correct_answer, options):
    """
    Provides a 50/50 lifeline by removing two incorrect answers, leaving the correct answer and one other incorrect answer.

    Parameters:
    - correct_answer (str): The correct answer to the current question.
    - options (list): A list containing all possible answers including the correct answer.

    Returns:
    - list: A reduced list of answers containing only the correct answer and one randomly selected incorrect answer.

    This function is designed to be used once per game session by a player who chooses to use the 50/50 lifeline. It randomly selects one incorrect answer to keep along with the correct answer and removes the other options.
    """
    #------------------------
    user_input = input("Do you want to use 50/50 hint? It can only be used once, enter[Y/N]")
    if user_input.upper() == "Y":
        temp = random.randint(1, 9)
        print("Here are two options")
        hint_list = []
        hint_list.append(correct_answer)
        hint_list.append(options[temp])
    return hint_list
    #------------------------
    
    #------------------------

#---------------------------------------

def skip_question(allowed_skips):
    """
    Allows the player to skip a question during the game.

    Parameters:
    - allowed_skips (int): The number of skips available to the player.

    Returns:
    - bool: True if the skip was successful (and a skip was available), False otherwise.

    This function checks if the player has any skips available. If so, it decrements the allowed_skips counter and returns True, indicating the question can be skipped. If no skips are available, it returns False. This function should be called before presenting a new question to the player.
    """
    #------------------------
    if skips < allowed_skips:
        temp = input("Do you want to skip this question? [Y/N]")
        if temp.upper() == "Y":
            skip = skip + 1
            flag = True
        elif temp.upper() == "N":
            flag = False
    return flag 
    #------------------------
    
    #------------------------

#---------------------------------------



