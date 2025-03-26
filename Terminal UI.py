import random
import time
import threading
from typing import Dict, List, Union, Optional, Any

import tkinter as tk
from tkinter import ttk, messagebox

# Dictionary containing all quiz questions organized by subject
# Structure: {topic: [list of question dictionaries]}
# Each question dictionary has: question text, options list, and answer index
quiz_data: Dict[str, List[Dict[str, Union[str, List[str], int]]]] = {
    "Mathematics": [
        {"question": "What is 7 + 8?", "options": ["15", "12", "16", "14"], "answer": 1},
        {"question": "What is the square root of 64?", "options": ["6", "7", "8", "9"], "answer": 3},
        {"question": "What is 12 * 12?", "options": ["124", "144", "134", "154"], "answer": 2},
        {"question": "What is 50 divided by 5?", "options": ["5", "10", "15", "20"], "answer": 2},
        {"question": "What is the value of pi to two decimal places?", "options": ["3.12", "3.14", "3.16", "3.18"],
         "answer": 2},
        {"question": "What is 9 squared?", "options": ["81", "72", "90", "99"], "answer": 1},
        {"question": "What is 100 divided by 4?", "options": ["20", "25", "30", "40"], "answer": 2},
        {"question": "What is 5 factorial (5!)?", "options": ["60", "100", "120", "150"], "answer": 3},
        {"question": "What is the cube root of 27?", "options": ["2", "3", "4", "5"], "answer": 2},
        {"question": "Solve for x: 2x + 3 = 7", "options": ["1", "3", "4", "2"], "answer": 4}
    ],
    "Physics": [
        {"question": "What is the SI unit of force?",
         "options": ["Watt", "Joule", "Newton", "Pascal"],
         "answer": 3},
        {"question": "Which law of motion states that for every action, there is an equal and opposite reaction?",
         "options": ["Newton's First Law", "Newton's Second Law", "Newton's Third Law",
                     "Law of Conservation of Momentum"],
         "answer": 3},
        {"question": "What is the formula for calculating kinetic energy?",
         "options": ["KE = mgh", "KE = ½mv²", "KE = Fd", "KE = mv"],
         "answer": 2},
        {"question": "Which phenomenon explains why the sky appears blue?",
         "options": ["Reflection", "Refraction", "Rayleigh scattering", "Diffraction"],
         "answer": 3},
        {"question": "What happens to the wavelength of light when it passes from air into water?",
         "options": ["It increases", "It decreases", "It stays the same", "It becomes zero"],
         "answer": 2},
        {"question": "Which particle has a positive charge?",
         "options": ["Electron", "Proton", "Neutron", "Photon"],
         "answer": 2},
        {
            "question": "According to Einstein's theory of relativity, what happens to time as an object approaches the speed of light?",
            "options": ["Time passes faster", "Time passes slower", "Time remains unchanged", "Time stops completely"],
            "answer": 2},
        {
            "question": "What is the relationship between frequency (f) and wavelength (λ) of a wave if v is the velocity?",
            "options": ["v = f/λ", "v = f·λ", "v = f+λ", "v = f-λ"],
            "answer": 2},
        {"question": "Which law states that energy cannot be created or destroyed, only transformed?",
         "options": ["Newton's First Law", "Law of Conservation of Momentum", "Law of Conservation of Energy",
                     "Coulomb's Law"],
         "answer": 3},
        {"question": "What is the acceleration due to gravity on Earth's surface (approximate value)?",
         "options": ["5.60 m/s²", "9.81 m/s²", "12.23 m/s²", "15.05 m/s²"],
         "answer": 2}
    ],
    "History": [
        {"question": "Who was the first president of the United States?",
         "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
         "answer": 1},
        {"question": "In what year did World War II end?", "options": ["1943", "1944", "1945", "1946"],
         "answer": 3},
        {"question": "Which ancient civilization built the pyramids?",
         "options": ["Greeks", "Romans", "Egyptians", "Mayans"], "answer": 3},
        {"question": "Who discovered America?",
         "options": ["Christopher Columbus", "Leif Erikson", "Marco Polo", "James Cook"],
         "answer": 1},
        {"question": "Which country was the first to land a man on the Moon?",
         "options": ["USSR", "China", "USA", "UK"], "answer": 3},
        {"question": "Who was the first emperor of Rome?", "options": ["Julius Caesar", "Augustus", "Nero", "Caligula"],
         "answer": 2},
        {"question": "In what year did the Titanic sink?", "options": ["1910", "1915", "1920", "1912"],
         "answer": 4},
        {"question": "Who wrote the Declaration of Independence?",
         "options": ["Benjamin Franklin", "John Adams", "George Washington", "Thomas Jefferson"],
         "answer": 4},
        {"question": "Which war was fought between the North and South regions of the United States?",
         "options": ["Revolutionary War", "Civil War", "World War I", "Vietnam War"], "answer": 2},
        {"question": "Who was the British Prime Minister during World War II?",
         "options": ["Winston Churchill", "Neville Chamberlain", "Margaret Thatcher", "Tony Blair"],
         "answer": 1}
    ],
    "Geography": [
        {"question": "What is the capital of France?", "options": ["London", "Berlin", "Madrid", "Paris"],
         "answer": 4},
        {"question": "Which continent is the largest by land area?",
         "options": ["Africa", "North America", "Asia", "Europe"], "answer": 3},
        {"question": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
         "answer": 4},
        {"question": "What is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
         "answer": 2},
        {"question": "Which country has the most population?", "options": ["USA", "India", "China", "Russia"],
         "answer": 3},
        {"question": "What is the tallest mountain in the world?",
         "options": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"], "answer": 3},
        {"question": "Which desert is the largest in the world?",
         "options": ["Antarctic", "Sahara", "Gobi", "Kalahari"], "answer": 1},
        {"question": "Which country has the most islands in the world?",
         "options": ["Canada", "Sweden", "Indonesia", "Philippines"], "answer": 2},
        {"question": "What is the smallest country in the world by land area?",
         "options": ["Monaco", "San Marino", "Vatican City", "Liechtenstein"], "answer": 3},
        {"question": "What is the capital of Brazil?",
         "options": ["Rio de Janeiro", "Sao Paulo", "Brasilia", "Salvador"], "answer": 3}
    ],
    "Biology": [
        {"question": "Which organelle is responsible for photosynthesis in plant cells?",
         "options": ["Mitochondria", "Nucleus", "Chloroplast", "Ribosome"],
         "answer": 3},
        {"question": "DNA replication occurs during which phase of the cell cycle?",
         "options": ["G1 phase", "S phase", "G2 phase", "M phase"],
         "answer": 2},
        {"question": "Which of the following is NOT a component of the central dogma of molecular biology?",
         "options": ["DNA", "RNA", "Proteins", "Lipids"],
         "answer": 4},
        {"question": "What is the main function of hemoglobin in blood?",
         "options": ["Clotting", "Oxygen transport", "Carbon dioxide removal", "pH regulation"],
         "answer": 2},
        {
            "question": "Which kingdom contains organisms that are multicellular and have cell walls but cannot photosynthesize?",
            "options": ["Protista", "Fungi", "Plantae", "Animalia"],
            "answer": 2},
        {"question": "Which part of the brain is primarily responsible for balance and coordination?",
         "options": ["Cerebrum", "Cerebellum", "Medulla oblongata", "Thalamus"],
         "answer": 2},
        {"question": "What is the primary role of enzymes in biological reactions?",
         "options": ["Energy source", "Reaction catalyst", "Transport molecule", "Storage compound"],
         "answer": 2},
        {"question": "Which process converts glucose to pyruvate in cellular respiration?",
         "options": ["Glycolysis", "Krebs cycle", "Electron transport chain", "Fermentation"],
         "answer": 1},
        {"question": "Mendel's principle of independent assortment applies to genes that are:",
         "options": ["On the same chromosome and close together", "On the same chromosome but far apart",
                     "On different chromosomes", "All of the above"],
         "answer": 3},
        {"question": "Which of the following is an example of negative feedback in the human body?",
         "options": ["Blood clotting", "Labor contractions during childbirth", "Thermoregulation", "Digestion"],
         "answer": 3}
    ]
}


def view_scoreboard(last_position: Optional[int] = None) -> None:
    """
    Display the scoreboard with player rankings and scores.

    This function reads the score file and prints a formatted leaderboard.
    If last_position is provided, only shows scores before last position.

    Parameters
    ----------
    last_position : int, optional
        Number of top scores to display. If None, displays all scores

    Returns
    -------
    None
    """
    try:
        with open("Quiz_score.txt", "r") as file:
            print("╔═══════════════════════════╗\n"
                  "║        LEADERBOARD        ║\n"
                  "╠═══════════════════╦═══════╣\n"
                  "║      Player       ║ Score ║\n"
                  "╠═══════════════════╬═══════╣")
            if last_position is None:
                lines = file.readlines()
                for i in range(1, len(lines) + 1):
                    player = f'{i}. {lines[i - 1].split(":")[0]}'
                    score = str(int(float(lines[i - 1].split(" ")[1][:-1])))
                    # Transforms float score from the file
                    # to int to fit the score into leaderboard and avoid ties between players
                    print(f"║ {player.ljust(17)} ║ {score.ljust(5)} ║")
            else:
                for i in range(1, last_position + 1):
                    line = file.readline()
                    player = f'{i}. {line.split(":")[0]}'
                    score = str(int(float(line.split(" ")[1][:-1])))
                    print(f"║ {player.ljust(17)} ║ {score.ljust(5)} ║")
                print("╚═══════════════════╩═══════╝\n")
    except FileNotFoundError:
        print("There is no scoreboard yet :(")
    time.sleep(2)  # Pause to allow the user to read the scoreboard


def show_commands() -> None:
    """
    Display the command menu for console interface.

    Prints a formatted box with available commands and their descriptions.
    Used in the command-line version of the quiz.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    commands = {
        "start": "Begin the quiz",
        "view": "View full scoreboard",
        "stop": "Exit the program",
        "help": "Show command menu"
    }

    # Menu design with box-drawing characters
    print("╔═══════════════════════════════════╗\n"
          "║           COMMAND MENU            ║\n"
          "╠════════════╦══════════════════════╣\n"
          "║  Command   ║      Description     ║\n"
          "╠════════════╬══════════════════════╣")
    for command, description in commands.items():
        print(f"║ {command.ljust(10)} ║ {description.ljust(20)} ║")
    print("╚════════════╩══════════════════════╝")


def confirm_action(prompt: str) -> bool:
    """
    Request user confirmation for an action.

    Continuously prompts the user until they provide a valid response.

    Parameters
    ----------
    prompt : str
        The confirmation message to display to the user

    Returns
    -------
    bool
        True if user confirms (enters 'y'), False otherwise
    """
    while True:
        confirmation = input(prompt).lower()
        if confirmation == "y" or confirmation == "n":
            return confirmation == "y"
        print("Please enter \"y\" or \"n\". Where y = yes; n = no: ")


def save(username: str, user_score: float) -> int:
    """
    Save the user's score to the scoreboard file.

    Reads the existing scoreboard, adds the new score, sorts scores in descending order,
    writes the updated scoreboard back to file.

    Parametrs
    ----------
    username : str
        Player's username to save with the score
    user_score : float
        Player's score to be saved

    Returns
    -------
    int
        The player's position/rank in the scoreboard after saving
    """
    try:
        with open("Quiz_score.txt", "r") as file:
            scoreboard = {}
            lines = file.readlines()
            for line in lines:
                name, score = line.replace(":", "").split()
                scoreboard[name] = score
            scoreboard[username] = user_score
            # Sort scoreboard by score in descending order
            scoreboard = dict(sorted(scoreboard.items(), key=lambda x: float(x[1]), reverse=True))
    except FileNotFoundError:
        # Handles the first launch of the program
        scoreboard = dict()
        scoreboard[username] = user_score
    with open("Quiz_score.txt", "w") as file:
        for name, score in scoreboard.items():
            file.write(f"{name}: {score}\n")
    print("Saved the current score to the \"Quiz_score.txt\"! Returning to main menu.")
    return list(scoreboard.keys()).index(username) + 1  # Return the player's position (1-based index)


def prepare_question_list(topic: str, shuffle_mode: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Prepare a list of questions for a quiz on a specific topic.

    Parameters
    ----------
    topic : str
        The category of questions to retrieve (must be a key in quiz_data)
    shuffle_mode : str, optional
        If "random", shuffles the questions; if None, maintains original order

    Returns
    -------
    List[Dict[str, Any]]
        List of question dictionaries for the selected topic
    """
    # Prepares questions with proper shuffling and validation.
    global quiz_data
    question_list = []
    if shuffle_mode == "random":
        question_list = quiz_data[topic]
        random.shuffle(question_list)
    elif shuffle_mode is None:
        question_list = quiz_data[topic]
    return question_list


def show_question(question: Dict[str, Any]) -> None:
    """
    Display a question and its answer options to the console.

    Parameters
    ----------
    question : Dict[str, Any]
        Dictionary containing question text and options

    Returns
    -------
    None
    """
    print(question["question"])
    opt_number = 1
    for option in question["options"]:
        print(f"{opt_number}. {option}")
        opt_number += 1


def get_answer(question: Dict[str, Any]) -> Union[bool, None]:
    """
    Get the user's answer to a question.

    Continuously prompts until a valid answer is provided.

    Parameters
    ----------
    question : Dict[str, Any]
        Dictionary containing the question data including the correct answer

    Returns
    -------
    bool or None
        True if the answer is correct, False if incorrect, None if skipped
    """
    while True:
        user_input = input("Your answer: ")
        if user_input not in ["1", "2", "3", "4", ""]:
            print(
                "Please select a number from 1 to 4 corresponding to your answer\n"
                "or press \"Enter\" to skip the question.")
            continue
        break
    if user_input == "":
        return False
    else:
        return int(user_input) == question["answer"]


# Global variables for timer functionality
time_ran_out = False
timer_event = threading.Event()


def choose_topic() -> str:
    """
    Prompt the user to select a quiz topic.

    Displays available topics and validates user selection.

    Parameters
    ----------
    None

    Returns
    -------
    str
        The selected topic name
    """
    while True:
        print("╔════════════════╗\n"
              "║     TOPICS     ║\n"
              "╠════════════════╣\n"
              "║ 1. Mathematics ║\n"
              "║ 2. Physics     ║\n"
              "║ 3. History     ║\n"
              "║ 4. Geography   ║\n"
              "║ 5. Biology     ║\n"
              "╚════════════════╝")
        topic = input("Please choose a topic of the test:\n")
        if topic not in ["1", "2", "3", "4", "5"]:
            print(
                "Please select a number from 1 to 5 corresponding to your answer.")
            continue
        break
    return list(quiz_data.keys())[int(topic) - 1]


def timer(duration: int = 2) -> None:
    """
    Run a countdown timer for the quiz.

    This function runs in a separate thread to track time during the quiz.

    Parameters
    ----------
    duration : int, optional
        The duration of the timer in seconds (default is 60)

    Returns
    -------
    None
    """
    start_time = time.time()
    while (time.time() - start_time) < duration and not timer_event.is_set():
        time.sleep(0.1)  # Check frequently but don't consume too much CPU
    if not timer_event.is_set():
        print("Time ran out!")
    timer_event.set()  # Signal that the timer has finished


def test(player: str) -> None:
    """
    Execute the quiz test for a player in console mode.

    Handles the entire quiz flow including topic selection,
    question presentation, scoring, and saving results.

    Parameters
    ----------
    player : str
        The username of the player taking the test

    Returns
    -------
    None
    """
    global time_ran_out, timer_event
    final_time = -1
    print("You will have 1 minute to answer 10 test questions.")
    if confirm_action("Do you want to start the test?(y/n)"):
        timer_thread = threading.Thread(target=timer, args=(2,))
        topic = choose_topic()
        print("Let's begin! You have 1 minute.")
        timer_event.clear()  # Reset the timer event
        start_time = time.time()
        timer_thread.start()
        print(start_time)
        questions = prepare_question_list(topic, "random")
        questions_answered_correclty = 0
        for current_question in questions:
            show_question(current_question)
            result = get_answer(current_question)
            if time_ran_out:
                final_time = time.time() - start_time
                break
            print("Correct!\n" if result else "Incorrect :(\n")
            if result:
                questions_answered_correclty += 1
        if final_time == -1:
            final_time = time.time() - start_time

        # Calculate the final score based on correct answers and time bonus
        question_weight = 9
        time_bonus = max(0, 50 - final_time)
        score = questions_answered_correclty * question_weight + time_bonus

        print(
            f"Congratulations! You completed the test.\nYour final score is {score}")
        position = save(player, score)
        print(f"Your position in the leader board is № {position}")
        timer_event.set()  # Signal the timer to stop if still running
        timer_thread.join()  # Wait for the timer thread to finish


def main() -> None:
    """
    Main function for the console-based quiz application.

    Handles user interactions for the command-line interface version.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    print("This is a specialized quiz to estimate your IQ level.")
    player = input("Please enter your nickname: ")
    print(f"Thank you, {player}!\n\nHere is our top 5 of scoreboard so far:")
    view_scoreboard(5)

    while True:
        show_commands()
        user_input = input("Please enter a command:\n").lower()
        if user_input == "start":
            test(player)
        elif user_input == "view":
            view_scoreboard()
        elif user_input == "stop":
            break


main()  # Commented out to allow the GUI version to run instead