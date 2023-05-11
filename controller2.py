from PyQt5.QtWidgets import *
from Project2 import *
import random, csv, os



QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    player_wins = 0
    player_grandtotal = 0
    computer_wins = 0
    computer_grandtotal = 0
    computer_choice = 0
    windividual = ''
    if os.path.isfile('./scoresheet.csv'):
        pass
    else:
        with open('scoresheet.csv', 'w') as scoresheet:
            score_sheet = csv.writer(scoresheet, delimiter='\t')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.home_page)

    def play(self):
        self.stackedWidget.setCurrentWidget(self.game_page)
        self.resetgame()

    def results(self):
        self.stackedWidget.setCurrentWidget(self.resultpage)

    def home(self):
        self.stackedWidget.setCurrentWidget(self.home_page)

    def computer_rand(self):
        self.computer_choice = random.randint(1, 5)
        if self.computer_choice == 1:
            self.Computerimage.setIcon(QtGui.QIcon("Rock.jpg"))
        elif self.computer_choice == 2:
            self.Computerimage.setIcon(QtGui.QIcon("Paper.jpg"))
        elif self.computer_choice == 3:
            self.Computerimage.setIcon(QtGui.QIcon("Scissors.jpg"))
        elif self.computer_choice == 4:
            self.Computerimage.setIcon(QtGui.QIcon("Lizard.jpg"))
        elif self.computer_choice == 5:
            self.Computerimage.setIcon(QtGui.QIcon("Spock.jpg"))


    def rockpush(self) -> None:
        """
        Function to select the player's choice as rock and generate a random computer choice, then determine the
        outcome and update the scores.
        :return: None
        """
        self.computer_rand()
        if self.computer_choice == 3:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Rock crushes scissors, player wins.')
        elif self.computer_choice == 4:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Rock crushes lizard, player wins.')
        elif self.computer_choice == 2:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Rock is covered by paper, computer wins.')
        elif self.computer_choice == 5:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Rock is vaporized by Spock, computer wins.')
        elif self.computer_choice == 1:
            self.Message_box.setPlainText('Draw, both chose Rock')
        self.update_scores()

    def paperpush(self) -> None:
        """
        Function to select the player's choice as paper and generate a random computer choice, then determine the
        outcome and update the scores.
        :return: None
        """
        self.computer_rand()
        if self.computer_choice == 1:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Paper covers rock, player wins.')
        elif self.computer_choice == 2:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Paper disproves Spock, player wins.')
        elif self.computer_choice == 3:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Paper is cut by scissors, computer wins.')
        elif self.computer_choice == 4:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Paper is eaten by lizard, computer wins.')
        elif self.computer_choice == 2:
            self.Message_box.setPlainText('Draw, both chose Paper')
        self.update_scores()

    def scissorpush(self) -> None:
        """
        Function to select the player's choice as scissors and generate a random computer choice, then determine the
        outcome and update the scores.
        :return: None
        """
        self.computer_rand()
        if self.computer_choice == 2:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Scissors cut paper, player wins.')
        elif self.computer_choice == 4:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Scissors decapitate lizard, player wins.')
        elif self.computer_choice == 1:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Scissors are smashed by rock, computer wins.')
        elif self.computer_choice == 5:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Scissors are smashed by Spock, computer wins.')
        elif self.computer_choice == 3:
            self.Message_box.setPlainText('Draw, both chose Scissors')
        self.update_scores()

    def lizardpush(self) -> None:
        """
        Function to select the player's choice as lizard and generate a random computer choice, then determine the
        outcome and update the scores.
        :return: None
        """
        self.computer_rand()
        if self.computer_choice == 2:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Lizard eats paper, player wins.')
        elif self.computer_choice == 5:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Lizard poisons Spock, player wins.')
        elif self.computer_choice == 1:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Lizard is smashed by rock, computer wins.')
        elif self.computer_choice == 3:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Lizard is decapitated by scissors, computer wins.')
        elif self.computer_choice == 4:
            self.Message_box.setPlainText('Draw, both chose Lizard')
        self.update_scores()

    def spockpush(self) -> None:
        """
        Function to select the player's choice as spock and generate a random computer choice, then determine the
        outcome and update the scores.
        :return: None
        """
        self.computer_rand()
        if self.computer_choice == 1:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Spock vaporizes rock, player wins.')
        elif self.computer_choice == 3:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Spock smashes scissors, player wins.')
        elif self.computer_choice == 2:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Spock is disproven by paper, computer wins.')
        elif self.computer_choice == 4:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Spock is poisoned by lizard, computer wins.')
        elif self.computer_choice == 5:
            self.Message_box.setPlainText('Draw, both chose Spock')
        self.update_scores()

    def resetgame(self) -> None:
        """
        Function to reset the scores and the message box message.
        :return: None
        """
        Controller.computer_wins = 0
        Controller.player_wins = 0
        self.update_scores()
        self.Message_box.setPlainText('The rules are simple:\n'
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
        self.win_check()

    def win_check(self):
        if self.player_wins >= 3:
            self.player_grandtotal += 1
            self.resultbox.setText("Player Wins")
            self.windividual = 'Player'
            self.results()
            self.update_text()
        elif self.computer_wins >= 3:
            self.computer_grandtotal += 1
            self.resultbox.setText("Computer Wins")
            self.windividual = 'Computer'
            self.results()
            self.update_text()
        self.Message_box2.setPlainText(self.Message_box.toPlainText())

    def update_text(self):
        with open('scoresheet.csv', 'a', newline='') as scoresheet:
            score_list = csv.writer(scoresheet, delimiter='\t')
            field = [self.player_wins, self.computer_wins, self.windividual, self.player_grandtotal, self.computer_grandtotal]
            score_list.writerow(field)

    def previousscores(self):
        self.stackedWidget.setCurrentWidget(self.score_page)
        with open('scoresheet.csv', 'r') as scoresheet:
            self.score_box.setText('Player rounds won\t Computer rounds won\tWinner\tPlayer total wins\tComputer total wins\t')
            for row in scoresheet:
                self.score_box.setText(self.score_box.text() + row)


    def reset_data(self):
        self.score_box.setText('Player rounds won\t Computer rounds won\tWinner\tPlayer total wins\tComputer total wins\t')
        with open('scoresheet.csv', 'w') as scoresheet:
            score_sheet = csv.writer(scoresheet)
            fields = ['Player rounds won', 'Computer rounds won', 'Winner', 'Player total wins', 'Computer total wins']
            score_sheet.writerow(fields)

