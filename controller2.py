from PyQt5.QtWidgets import *
from Project2 import *
import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    player_wins = 0
    computer_wins = 0

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Rockbutton.clicked.connect(lambda: self.rockpush())
        self.Paperbutton.clicked.connect(lambda: self.paperpush())
        self.Scissorsbutton.clicked.connect(lambda: self.scissorpush())
        self.Lizardbutton.clicked.connect(lambda: self.lizardpush())
        self.Spockbutton.clicked.connect(lambda: self.spockpush())
        self.Reset_button.clicked.connect(lambda: self.resetbutton())
        self.Player_wins.setText(f'Player wins: {self.player_wins}')
        self.Computer_wins.setText(f'Computer wins: {self.computer_wins}')
        self.Message_box.setText('The rules are simple:\n'
                                 'Scissors cut paper, paper covers rock, rock crushes lizard,\n'
                                 'lizard poisons Spock, Spock smashes scissors, scissors decapitate lizard,\n'
                                 'lizard eats paper, paper disproves Spock, Spock vaporizes rock,\n'
                                 'and as it always has, rock crushes scissors.')

    def rockpush(self) -> None:
        """
        Function to select the player's choice as rock and generate a random computer choice, then determine the
        outcome and update the scores.
        :return: None
        """
        computer_choice = random.randint(1, 5)
        if computer_choice == 3:
            Controller.player_wins += 1
            self.Message_box.setText('Rock crushes scissors, player wins.')
        elif computer_choice == 4:
            Controller.player_wins += 1
            self.Message_box.setText('Rock crushes lizard, player wins.')
        elif computer_choice == 2:
            Controller.computer_wins += 1
            self.Message_box.setText('Rock is covered by paper, computer wins.')
        elif computer_choice == 5:
            Controller.computer_wins += 1
            self.Message_box.setText('Rock is vaporized by Spock, computer wins.')
        elif computer_choice == 1:
            self.Message_box.setText('Draw, both chose Rock')
        self.update_scores()

    def paperpush(self) -> None:
        """
        Function to select the player's choice as paper and generate a random computer choice, then determine the
        outcome and update the scores.
        :return: None
        """
        computer_choice = random.randint(1, 5)
        if computer_choice == 1:
            Controller.player_wins += 1
            self.Message_box.setText('Paper covers rock, player wins.')
        elif computer_choice == 2:
            Controller.player_wins += 1
            self.Message_box.setText('Paper disproves Spock, player wins.')
        elif computer_choice == 3:
            Controller.computer_wins += 1
            self.Message_box.setText('Paper is cut by scissors, computer wins.')
        elif computer_choice == 4:
            Controller.computer_wins += 1
            self.Message_box.setText('Paper is eaten by lizard, computer wins.')
        elif computer_choice == 2:
            self.Message_box.setText('Draw, both chose Paper')
        self.update_scores()

    def scissorpush(self) -> None:
        """
        Function to select the player's choice as scissors and generate a random computer choice, then determine the
        outcome and update the scores.
        :return: None
        """
        computer_choice = random.randint(1, 5)
        if computer_choice == 2:
            Controller.player_wins += 1
            self.Message_box.setText('Scissors cut paper, player wins.')
        elif computer_choice == 4:
            Controller.player_wins += 1
            self.Message_box.setText('Scissors decapitate lizard, player wins.')
        elif computer_choice == 1:
            Controller.computer_wins += 1
            self.Message_box.setText('Scissors are smashed by rock, computer wins.')
        elif computer_choice == 5:
            Controller.computer_wins += 1
            self.Message_box.setText('Scissors are smashed by Spock, computer wins.')
        elif computer_choice == 3:
            self.Message_box.setText('Draw, both chose Scissors')
        self.update_scores()

    def lizardpush(self) -> None:
        """
        Function to select the player's choice as lizard and generate a random computer choice, then determine the
        outcome and update the scores.
        :return: None
        """
        computer_choice = random.randint(1, 5)
        if computer_choice == 2:
            Controller.player_wins += 1
            self.Message_box.setText('Lizard eats paper, player wins.')
        elif computer_choice == 5:
            Controller.player_wins += 1
            self.Message_box.setText('Lizard poisons Spock, player wins.')
        elif computer_choice == 1:
            Controller.computer_wins += 1
            self.Message_box.setText('Lizard is smashed by rock, computer wins.')
        elif computer_choice == 3:
            Controller.computer_wins += 1
            self.Message_box.setText('Lizard is decapitated by scissors, computer wins.')
        elif computer_choice == 4:
            self.Message_box.setText('Draw, both chose Lizard')
        self.update_scores()

    def spockpush(self) -> None:
        """
        Function to select the player's choice as spock and generate a random computer choice, then determine the
        outcome and update the scores.
        :return: None
        """
        computer_choice = random.randint(1, 5)
        if computer_choice == 1:
            Controller.player_wins += 1
            self.Message_box.setText('Spock vaporizes rock, player wins.')
        elif computer_choice == 3:
            Controller.player_wins += 1
            self.Message_box.setText('Spock smashes scissors, player wins.')
        elif computer_choice == 2:
            Controller.computer_wins += 1
            self.Message_box.setText('Spock is disproven by paper, computer wins.')
        elif computer_choice == 4:
            Controller.computer_wins += 1
            self.Message_box.setText('Spock is poisoned by lizard, computer wins.')
        elif computer_choice == 5:
            self.Message_box.setText('Draw, both chose Spock')
        self.update_scores()

    def resetbutton(self) -> None:
        """
        Function to reset the scores and the message box message.
        :return: None
        """
        Controller.computer_wins = 0
        Controller.player_wins = 0
        self.update_scores()
        self.Message_box.setText('The rules are simple:\n'
                                 'Scissors cut paper, paper covers rock, rock crushes lizard,\n'
                                 'lizard poisons Spock, Spock smashes scissors, scissors decapitate lizard,\n'
                                 'lizard eats paper, paper disproves Spock, Spock vaporizes rock,\n'
                                 'and as it always has, rock crushes scissors.')

    def update_scores(self) -> None:
        """
        Function to update the scores displayed on the GUI.
        :return: None
        """
        self.Player_wins.setText(f'Player wins: {self.player_wins}')
        self.Computer_wins.setText(f'Computer wins: {self.computer_wins}')