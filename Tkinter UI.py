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


def rgb_to_hex(rgb: List[int]) -> str:
    """
    Convert RGB color values to hexadecimal color code.

    Parameters
    ----------
    rgb : List[int]
        List containing [R, G, B] values (0-255)

    Returns
    -------
    str
        Hexadecimal color string (e.g., "#FFAA00")
    """
    return f"#{str(hex(rgb[0]))[2:]}{str(hex(rgb[1]))[2:]}{str(hex(rgb[2]))[2:]}".upper()


# print(rgb_to_hex([238, 232, 145]))  # Example use of the function


# GUI implementation using tkinter
class QuizApp(tk.Tk):
    """
    Main application class for the graphical quiz interface.

    This class manages the entire GUI application including frames,
    quiz logic, timer, and score calculation.
    """

    def __init__(self) -> None:
        """
        Initialize the Quiz Application.

        Sets up the main window, styles, and initial variables.
        """
        super().__init__()
        self.title("IQ Test™")  # Set window title
        self.geometry("400x500")  # Set window size
        self.player = ""  # Initialize player name
        self.current_question = 0  # Track current question index
        self.score = 0  # Initialize score counter
        self.time_left = 60  # Set quiz duration in seconds
        self.timer_running = False  # Flag to track timer status
        self.resizable(False, False)  # Disable window resizing

        # Start with the main menu screen
        self.create_main_menu()

    def create_main_menu(self) -> None:
        """
        Create and display the main menu of the application.

        Contains username entry, start button, scoreboard button, and exit button.
        """
        self.clear_window()  # Clear any existing widgets

        # Create main frame for the menu
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Add main title to the menu
        ttk.Label(self.main_frame, text="Welcome to IQ Test™",
                  font=('Helvetica', 24, 'bold')).pack(pady=20)

        # Embed the username entry field on the main menu
        username_frame = ttk.Frame(self.main_frame)
        username_frame.pack(pady=20)
        ttk.Label(username_frame, text="Enter your username:",
                  font=('Helvetica', 14)).pack(padx=(0, 5))
        self.username_entry = ttk.Entry(username_frame, font=('Helvetica', 14), width=20)
        self.username_entry.pack()

        # Create main menu buttons with custom styles
        ttk.Button(self.main_frame, text="Start Quiz",
                   command=self.start_quiz_flow,
                   style='Accent.TButton', width=25).pack(ipady=10, pady=5)
        ttk.Button(self.main_frame, text="View Scoreboard",
                   command=lambda: self.show_scoreboard(),
                   style='Menu.TButton', width=25).pack(ipady=10, pady=5)
        ttk.Button(self.main_frame, text="Exit", command=self.destroy,
                   style='Exit.TButton', width=25).pack(ipady=10, pady=5)

    def start_quiz_flow(self) -> None:
        """
        Start the quiz process after username is entered.

        Retrieves the player's name and shows the topic selection screen.
        """
        # Retrieve the player's name from the embedded entry field.
        self.player = self.username_entry.get().strip() or "Anonymous"
        self.show_topic_selection()

    def show_topic_selection(self) -> None:
        """
        Display the topic selection screen.

        Shows all available quiz topics as buttons.
        """
        self.clear_window()  # Clear the current window

        # Create frame for topic selection
        self.topic_frame = ttk.Frame(self)
        self.topic_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Add title for the topic selection screen
        ttk.Label(self.topic_frame, text="Select Topic",
                  font=('Helvetica', 20)).pack(pady=20)

        # Create a button for each available topic
        topics = list(quiz_data.keys())
        for i, topic in enumerate(topics, 1):
            ttk.Button(self.topic_frame, text=topic,
                       command=lambda t=topic: self.start_quiz(t),
                       style='Topic.TButton', width=30).pack(pady=10)

        # Add back button to return to main menu
        ttk.Button(self.topic_frame, style="Menu.TButton", text="Back",
                   command=self.create_main_menu).pack(pady=20)

    def start_quiz(self, topic: str) -> None:
        """
        Initialize and start the quiz for the selected topic.

        Sets up the quiz interface including timer, question display, and answer buttons.

        Parameters
        ----------
        topic : str
            The selected quiz topic
        """
        self.defclr = self.cget("background")  # Store default background color
        self.clear_window()  # Clear the window for quiz interface

        # Create main quiz frame
        self.quiz_frame = ttk.Frame(self)
        self.quiz_frame.pack(fill=tk.BOTH, expand=True)

        # Create background label for the quiz
        self.quiz_bg = ttk.Label(self.quiz_frame, width=400)
        self.quiz_bg.pack(fill="both", ipady=100)

        # Create timer display with initial green background
        self.timer_frame = ttk.Label(self.quiz_bg, relief=tk.RAISED, background=rgb_to_hex([102, 255, 82]))
        self.timer_frame.pack(pady=20)

        # Timer label to show remaining time
        self.timer_label = ttk.Label(self.timer_frame,
                                     font=('Helvetica', 14),
                                     foreground='black', background=rgb_to_hex([102, 255, 82]))
        self.timer_label.pack(pady=10, padx=10)

        # Label to display the current question
        self.question_label = ttk.Label(self.quiz_bg,
                                        wraplength=600,
                                        font=('Helvetica', 14, 'bold'))
        self.question_label.pack(pady=20)

        # Create frame and buttons for answer options
        self.option_buttons = []
        self.options_frame = ttk.Label(self.quiz_bg, width=400)
        self.options_frame.pack(pady=20)
        for i in range(4):
            btn = ttk.Button(self.options_frame, style='Option.TButton')
            btn.pack(pady=10)
            btn.config(command=lambda idx=i: self.check_answer(idx + 1))
            self.option_buttons.append(btn)

        # Load the first question and start the timer
        self.load_question(topic)
        self.start_timer()

    def load_question(self, topic: str) -> None:
        """
        Load questions for the selected topic.

        Prepares and shuffles the questions, then shows the first question.

        Parameters
        ----------
        topic : str
            The selected quiz topic
        """
        self.questions = prepare_question_list(topic, "random")
        self.show_question(0)  # Start with the first question (index 0)

    def show_question(self, q_idx: int) -> None:
        """
        Display a question with its options in the quiz interface.

        If the question index is out of range, end the quiz.

        Parameters
        ----------
        q_idx : int
            Index of the question to be displayed
        """
        # Check if we've reached the end of questions
        if q_idx >= len(self.questions):
            self.end_quiz()
            return

        self.current_question = q_idx
        question = self.questions[q_idx]

        # Update the question label with the current question text
        self.question_label.config(justify="center", text=question["question"], wraplength=360)
        # Configure each option button with the corresponding option text
        for i, (btn, option) in enumerate(zip(self.option_buttons, question["options"])):
            btn.config(text=option)

    def check_answer(self, selected_idx: int) -> None:
        """
        Validate the user's answer and provide visual feedback.

        Compares the selected option with the correct answer,
        updates the score if correct, and shows appropriate color feedback.
        Then advances to the next question.

        Parameters
        ----------
        selected_idx : int
            Index of the option selected by the user
        """
        question = self.questions[self.current_question]
        correct = selected_idx == question["answer"]

        # Helper function to change background colors for visual feedback
        def change_colors(color: str) -> None:
            self.quiz_bg.config(background=color)
            self.question_label.config(background=color)
            self.options_frame.config(background=color)

        if correct:
            # Increment score and flash green for correct answer
            self.score += 1
            self.quiz_frame.config()
            change_colors("#99FF99")  # Green background for correct answer
            self.update()
            self.after(250, change_colors("#DCDAD5"))  # Reset to default color after delay
            self.update()
        else:
            # Flash red for incorrect answer
            change_colors("#FF9999")  # Red background for incorrect answer
            self.update()
            self.after(250, change_colors("#DCDAD5"))  # Reset to default color after delay
            self.update()

        # Move to the next question
        self.show_question(self.current_question + 1)

    def start_timer(self) -> None:
        """
        Initialize and start the quiz timer.

        Sets the initial time to 60 seconds and starts the timer countdown.
        """
        self.time_left = 60
        self.timer_running = True

        self.update_timer()

    def update_timer(self) -> None:
        """
        Update the timer display and check for timeout.

        Updates the timer label and changes its color based on remaining time.
        When the timer reaches zero, ends the quiz.
        """
        rgb_to_hex([102, 255, 82])  # This function call appears to have no effect
        if self.time_left > 0 and self.timer_running:
            # Calculate dynamic color based on remaining time
            # The color transitions as time decreases (from green to red)
            self.timer_label.config(
                text=f"Time Left: {self.time_left}s",
                background=rgb_to_hex(
                    [222 - self.time_left * 2, 75 + self.time_left * 3, 22 + self.time_left]
                )
            )
            self.timer_frame.config(
                background=rgb_to_hex(
                    [222 - self.time_left * 2, 75 + self.time_left * 3, 22 + self.time_left]
                )
            )
            # Decrement timer and schedule next update
            self.time_left -= 1
            self.after(1000, self.update_timer)
        else:
            # End quiz if timer ran out and was still running
            if self.timer_running:
                self.end_quiz()
            self.timer_running = False

    def end_quiz(self) -> None:
        """
        Finish the quiz, calculate the final score, and show results.

        Stops the timer, calculates total score including time bonus,
        saves the score, and returns to the main menu.
        """
        # Stop the timer
        self.timer_running = False

        # Calculate final score with weighting and time bonus
        question_weight = 9
        time_bonus = max(0, self.time_left)
        total_score = self.score * question_weight + time_bonus

        # Save player's score
        save(self.player, total_score)

        # Show completion message with final score
        messagebox.showinfo(
            "Quiz Complete!",
            f"Congratulation, You completed the quiz!\nFinal Score: {total_score}\n"
        )
        # Return to main menu
        self.create_main_menu()

    def show_scoreboard(self) -> None:
        """
        Display a formatted scoreboard with player rankings.

        Creates a Treeview widget to show player names and scores
        in a ranked list with alternating row colors.
        """
        # Clear previous window contents
        self.clear_window()

        # Create a frame with padding for better layout
        score_frame = ttk.Frame(self, padding="20")
        score_frame.pack(fill=tk.BOTH, expand=True)

        # Set a theme and configure styles for a clean, modern look
        style = ttk.Style(self)
        style.theme_use("clam")  # Use a theme that works well with custom styling
        # Configure heading style with bold font
        style.configure("Treeview.Heading", font=("Helvetica", 13, "bold"), foreground="#333", padding=5)
        # Configure row style with appropriate height and borders
        style.configure(
            "Treeview",
            font=("Helvetica", 12),
            rowheight=30,
            bordercolor="#ccc",
            borderwidth=1,
            relief="solid"
        )
        # Configure selection highlight color
        style.map("Treeview", background=[("selected", "#347083")])

        # Create the Treeview widget with three columns: Rank, Player, Score
        tree = ttk.Treeview(
            score_frame,
            columns=("Rank", "Player", "Score"),
            show="headings",
            selectmode="none"
        )

        # Configure column headings and alignments
        tree.heading("Rank", text="Rank", anchor=tk.CENTER)
        tree.heading("Player", text="Player", anchor=tk.W)  # Left-align text
        tree.heading("Score", text="Score", anchor=tk.CENTER)

        # Set column widths and alignment
        tree.column("Rank", anchor=tk.CENTER, width=40)  # Narrower Rank column
        tree.column("Player", anchor=tk.W, width=150)  # Player name column
        tree.column("Score", anchor=tk.CENTER, width=80)  # Score column

        # Add a vertical scrollbar linked to the treeview
        scrollbar = ttk.Scrollbar(score_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        # Position scrollbar at specific coordinates
        scrollbar.place(x=350, y=12, height=386)
        # Alternative: scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=60)

        # Read scores from file and insert them with alternating row colors
        try:
            with open("Quiz_score.txt", "r") as f:
                scores = [line.strip().split(": ") for line in f.readlines()]
                for i, (name, score) in enumerate(scores, start=1):
                    # Alternate between odd and even row tags for striping effect
                    tag = "oddrow" if i % 2 == 1 else "evenrow"
                    tree.insert("", tk.END, values=(i, name, int(float(score))), tags=(tag,))
        except FileNotFoundError:
            # Display a message if no scores file exists
            no_socres = ttk.Label(
                score_frame,
                text="No scores yet :(",
                background="white",
                font=("Helvetica", 19)
            )
            no_socres.place(x=100, y=100)

        # Configure tags for alternating row background colors
        tree.tag_configure("oddrow", background="#f9f9f9")  # Light gray for odd rows
        tree.tag_configure("evenrow", background="#ffe5cc")  # Light orange for even rows

        # Add the treeview widget to the frame
        tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Add a button frame for the back button
        button_frame = ttk.Frame(score_frame)
        button_frame.pack(pady=10)
        ttk.Button(
            button_frame,
            style="Menu.TButton",
            text="Back",
            command=self.create_main_menu
        ).pack()

    def clear_window(self) -> None:
        """
        Remove all widgets from the current window.

        Destroys all child widgets to prepare for displaying a new screen.
        """
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = QuizApp()
    app.style = ttk.Style(app)
    app.style.theme_use('clam')

    # Configure custom button styles with specific fonts and colors
    app.style.configure(
        'Accent.TButton',
        font=('Helvetica', 14),
        background='#4CAF50'  # Green accent button
    )
    app.style.configure(
        'Menu.TButton',
        font=('Helvetica', 14),
        background='#FFA726'  # Orange menu button
    )
    app.style.configure(
        'Exit.TButton',
        font=('Helvetica', 14),
        background='#FF7043'  # Red-orange exit button
    )
    app.style.configure(
        'Topic.TButton',
        font=('Helvetica', 16),
        background='#EEE8AA'  # Light yellow topic button
    )
    app.style.configure(
        'Option.TButton',
        font=('Helvetica', 11),
        width=30,
        padding=8  # Standard option button
    )

    style = ttk.Style()

    # Configure dynamic effects for button states (pressed, active)
    # For accent buttons (green)
    style.map(
        'Accent.TButton',
        foreground=[('pressed', 'white'), ('active', 'black')],
        background=[('pressed', '!disabled', '#4CAF50'), ('active', '#388E3C')]
    )
    # For menu buttons (orange)
    style.map(
        'Menu.TButton',
        foreground=[('pressed', 'white'), ('active', 'black')],
        background=[('pressed', '!disabled', '#FFA726'), ('active', '#F57C00')]
    )
    # For exit buttons (red-orange)
    style.map(
        'Exit.TButton',
        foreground=[('pressed', 'white'), ('active', 'black')],
        background=[('pressed', '!disabled', '#FF7043'), ('active', '#D84315')]
    )
    # For topic buttons (light yellow)
    style.map(
        'Topic.TButton',
        foreground=[('pressed', 'black'), ('active', 'black')],
        background=[('pressed', '!disabled', '#EEE8AA'), ('active', '#D4D097')]
    )

    # Start the application
    app.mainloop()
