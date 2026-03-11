import random
import json

class Scoreboard:
    GAMES_TO_WIN = 5
    def __init__(self):
        self.score = {'player': 0, 'computer': 0}
    
    def add_points(self, player, points):
        self.score[player] += points

    def current_score(self):
        print(messages['current_score'].format(
            player=self.score['player'],
            computer=self.score['computer']))
    
    def _reset(self):
        self.score['player'] = 0
        self.score['computer'] = 0

class Move:
    def __init__(self):
        self._name = type(self).__name__.lower()
    
    def display(self, identity):
        if identity == 'human':
            return messages['human_choice'].format(move=self._name)
        
        return messages['computer_choice'].format(move=self._name)

    def __str__(self):
        return self.name
    
class Rock(Move):
    def __init__(self):
        super().__init__()
        self._wins_against = [Scissors, Lizard]
    
    def __gt__(self, other):
        if not isinstance(other, Move):
            return NotImplemented
        
        return type(other) in self._wins_against

class Paper(Move):
    def __init__(self):
        super().__init__()
        self._wins_against = [Rock, Spock]
    
    def __gt__(self, other):
        if not isinstance(other, Move):
            return NotImplemented
        
        return type(other) in self._wins_against

class Scissors(Move):
    def __init__(self):
        super().__init__()
        self._wins_against = [Paper, Lizard]
    
    def __gt__(self, other):
        if not isinstance(other, Move):
            return NotImplemented
        
        return type(other) in self._wins_against

class Lizard(Move):
    def __init__(self):
        super().__init__()
        self._wins_against = [Paper, Spock]
    
    def __gt__(self, other):
        if not isinstance(other, Move):
            return NotImplemented
        
        return type(other) in self._wins_against

class Spock(Move):
    def __init__(self):
        super().__init__()
        self._wins_against = [Rock, Scissors]
    
    def __gt__(self, other):
        if not isinstance(other, Move):
            return NotImplemented
        
        return type(other) in self._wins_against

class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock', 'r', 'p', 's', 'l', 'sp')
    def __init__(self):
        self.move = None

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(list(RPSGame.MOVES.values()))

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        while True:
            choice = input(messages['choose']).lower()
            if choice in Player.CHOICES:
                choice = self._format_choice(choice)
                break

            print(messages['invalid'])

        self.move = RPSGame.MOVES[choice]

    def _format_choice(self, choice):
        match choice:
            case 'r':
                return 'rock'
            case 's':
                return 'scissors'
            case 'p':
                return 'paper'
            case 'l':
                return 'lizard'
            case 'sp':
                return 'spock'
        return choice

class RPSGame:
    MOVES = {'rock': Rock(),
             'scissors': Scissors(),
             'paper': Paper(),
             'lizard': Lizard(),
             'spock': Spock()}
    
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
                self._display_match_winner()
                if not self._play_again():
                    break
        self._display_goodbye_message()

    def _display_welcome_message(self):
        print(messages['welcome'])
        print(messages['game_rules'])

    def _display_goodbye_message(self):
        print(messages['goodbye'])

    def _display_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        print(human_move.display('human'))
        print(computer_move.display('computer'))

        if human_move > computer_move:
            self.scores.add_points('player', 1)
            print(messages['win'])
        elif computer_move > human_move:
            self.scores.add_points('computer', 1)
            print(messages['lose'])
        else:
            print(messages['tie'])

    def _display_match_winner(self):
        print(messages['match_end'].format(match_winner=self._match_winner()))

    def _human_wins(self, human_move, computer_move):
        return computer_move in self.WINNING_COMBINATIONS[human_move]

    def _computer_wins(self, human_move, computer_move):
        return human_move in self.WINNING_COMBINATIONS[computer_move]

    def _play_again(self):
        answer = input(messages['play_again'])
        return answer.lower().startswith('y')
    
    def _match_winner(self):
        if self.scores.score['player'] == Scoreboard.GAMES_TO_WIN:
            return messages['win']
        return messages['computer_win']
    
    def _is_max_game_length(self):
        return any([num for num in self.scores.score.values() 
                    if num == Scoreboard.GAMES_TO_WIN])

with open('rps_game.json', 'r') as file:
    messages = json.load(file)

RPSGame().play()