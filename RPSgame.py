import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')
    def __init__(self):
        self._move = None

class Computer():
    def __init__(self):
        self._move = None

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human:
    def __init__(self):
        self._move = None

    def choose(self):
        prompt = 'Pick rock, paper, or scissors: '
        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                break

            print(f'Invalid choice')

        self.move = choice

class Move:
    def __init__(self):
        pass

class Rule:
    def __init__(self):
        pass

    def compare(self, move1, move2):
        pass

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def play(self):
        self._display_welcome_message()
        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break
        self._display_goodbye_message()

    def _display_welcome_message(self):
        print('Welcome to Rock, Paper, Scissors')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock, Paper, Scissors. Goodbye!')

    def _display_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'You chose {self._human.move}')
        print(f'The computer chose {self._computer.move}')

        if ((human_move == 'rock' and computer_move == 'scissors') or 
            (human_move == 'paper' and computer_move == 'rock') or 
            (human_move == 'scissors' and computer_move == 'paper')):
            print('You win!')
        elif ((human_move == 'rock' and computer_move == 'paper') or 
              (human_move == 'paper' and computer_move == 'scissors') or 
              (human_move == 'scissors' and computer_move == 'rock')):
            print('You lose!')
        else:
            print("It's a tie!")

    def _play_again(self):
        answer = input('Would you like to play again? (y/n): ')
        return answer.lower().startswith('y')


RPSGame().play()