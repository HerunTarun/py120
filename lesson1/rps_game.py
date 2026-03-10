import random

class Scoreboard:
    GAMES_TO_WIN = 5
    def __init__(self):
        self.score = {'player': 0, 'computer': 0}

    @property
    def values(self):
        return self.score.values()
    
    def add_points(self, player, points):
        self.score[player] += points

    def current_score(self):
        print(f'The score is {self.score['player']} : {self.score['computer']}')
    
    def _reset(self):
        self.score['player'] = 0
        self.score['computer'] = 0


class Player:
    CHOICES = ('rock', 'paper', 'scissors')
    def __init__(self):
        self.move = None

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Pick rock, paper, or scissors: '
        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                break

            print('Invalid choice')

        self.move = choice

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self.scores = Scoreboard()

    def play(self):
        self._display_welcome_message()
        self.scores._reset()
        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            self.scores.current_score()
            if self._is_max_game_length():
                self.scores._reset()
                if not self._play_again():
                    break
        self._display_goodbye_message()

    def _display_welcome_message(self):
        print('Welcome to Rock, Paper, Scissors')
        print('First one to 5 points wins. Good luck!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock, Paper, Scissors. Goodbye!')

    def _display_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'You chose {self._human.move}')
        print(f'The computer chose {self._computer.move}')

        if self._human_wins(human_move, computer_move):
            self.scores.add_points('player', 1)
            print('You win!')
        elif self._computer_wins(human_move, computer_move):
            self.scores.add_points('computer', 1)
            print('You lose!')
        else:
            print("It's a tie!")

    def _human_wins(self, human_move, computer_move):
        return ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper'))

    def _computer_wins(self, human_move, computer_move):
        return ((human_move == 'rock' and computer_move == 'paper') or
              (human_move == 'paper' and computer_move == 'scissors') or
              (human_move == 'scissors' and computer_move == 'rock'))

    def _play_again(self):
        answer = input('Would you like to play again? (y/n): ')
        return answer.lower().startswith('y')
    
    def _is_max_game_length(self):
        return any([num for num in self.scores.values if num == 5])


RPSGame().play()