import random
import json
import os

class Scoreboard:
    GAMES_TO_WIN = 5
    def __init__(self):
        self.score = {'player': 0, 'computer': 0}
        self.history = []

    def add_points(self, player, points):
        self.score[player] += points

    def current_score(self):
        print(messages['current_score'].format(
            player=self.score['player'],
            computer=self.score['computer']))

    def reset_score(self):
        self.score['player'] = 0
        self.score['computer'] = 0

    def update_history(self, player_move, computer_move, winner):
        self.history.append((player_move, computer_move, winner))

    def reset_history(self):
        self.history = []

    def query_history(self):
        while True:
            lines = input(messages['history_query'])
            if lines.startswith('a'):
                return len(self.history)
            try:
                lines = int(lines)
            except ValueError:
                print(messages['invalid_help'])
                continue

            if lines > len(self.history):
                return len(self.history)

            return lines

    def display_history(self, lines):
        if not lines:
            print(messages['empty_history'])

        for i in range(lines):
            print(messages['display_history'].format(round=self.history[i]))

class Move:
    def __init__(self):
        self._name = type(self).__name__.lower()

    def display(self, identity):
        if identity == 'human':
            return messages['human_choice'].format(move=self._name)

        return messages['computer_choice'].format(computer=identity,
                                                  move=self._name)

    def __str__(self):
        return self._name

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
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock',
               'r', 'p', 's', 'l', 'sp')
    OPTIONS = ('his', 'history')
    OPPONENT_CHOICES = ('r2d2', 'daneel', 'hal', 'r', 'd', 'h')

    def __init__(self, scoreboard):
        self.move = None
        self.scoreboard = scoreboard

class Computer(Player):
    def __init__(self, scoreboard):
        super().__init__(scoreboard)

    def choose_move(self):
        self.move = random.choice(list(RPSGame.MOVES.values()))

class R2D2(Computer):
    def __init__(self, scoreboard):
        super().__init__(scoreboard)
        self.name = 'R2D2'

    def choose_move(self):
        self.move = Rock()

class HAL(Computer):
    SCISSOR_CHANCE = 60
    def __init__(self, scoreboard):
        super().__init__(scoreboard)
        self.name = 'HAL'

    def choose_move(self):
        if random.choice(range(100)) > self.SCISSOR_CHANCE:
            self.move = Scissors()
        else:
            self.move = random.choice(list(RPSGame.MOVES.values()))


class Daneel(Computer):
    def __init__(self, scoreboard):
        super().__init__(scoreboard)
        self.name = 'Daneel'

    def choose_move(self):
        if self.scoreboard.history:
            self.move = self.scoreboard.history[-1][0]
        else:
            self.move = random.choice(list(RPSGame.MOVES.values()))


class Human(Player):
    def __init__(self, scoreboard):
        super().__init__(scoreboard)

    def choose_move(self):
        while True:
            choice = input(messages['choose_move']).lower()
            if choice in Player.OPTIONS:
                self._identify_option(choice)
                continue
            if choice in Player.CHOICES:
                choice = self._format_choice(choice)
                break

            print(messages['invalid_choice'])

        self.move = RPSGame.MOVES[choice]

    def choose_opponent(self):
        while True:
            opponent = input(messages['choose_opponent']).lower()
            if opponent in Player.OPTIONS:
                self._identify_option(opponent)
                continue

            if opponent in Player.OPPONENT_CHOICES:
                opponent = self._format_opponent(opponent)
                return game.opponents[opponent]
            print(messages['invalid_opponent'])

    def _identify_option(self, option):
        history = ['his', 'history']

        if option in history:
            lines = self.scoreboard.query_history()
            self.scoreboard.display_history(lines)


    def _format_opponent(self, opponent):
        match opponent:
            case 'h':
                return 'hal'
            case 'd':
                return 'daneel'
            case 'r':
                return 'r2d2'

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
        self.scores = Scoreboard()
        self._human = Human(self.scores)
        self._computer = None
        self._opponents = {
            'r2d2': R2D2(self.scores),
            'daneel': Daneel(self.scores),
            'hal': HAL(self.scores)}

    @property
    def opponents(self):
        return self._opponents

    def play(self):
        self._display_welcome_message()
        self.scores.reset_score()
        while True:
            self._computer = self._human.choose_opponent()
            self._display_opponent()
            while True:
                self._human.choose_move()
                self._computer.choose_move()
                self._display_choices()
                winner = self._calculate_winner()
                self._display_winner(winner)
                self._update_score(winner)
                self.scores.update_history(self._human.move,
                                        self._computer.move,
                                        winner)
                self.scores.current_score()
                if self._is_max_game_length():
                    self._display_match_winner()
                    self.scores.reset_score()
                    break
            if not self._play_again():
                self.scores.reset_history()
                break
        self._display_goodbye_message()

    def _display_welcome_message(self):
        self._clear_screen()
        print(messages['welcome'])
        print(messages['game_rules'])
        print(messages['point_system'])
        print(messages['history_intro'])

    def _display_goodbye_message(self):
        print(messages['goodbye'])

    def _display_choices(self):
        print(self._human.move.display('human'))
        print(self._computer.move.display(f'{self._computer.name}'))

    def _display_opponent(self):
        print(messages['opponent_intro'].format(opponent=self._computer.name))
    def _calculate_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        if human_move > computer_move:
            return 'Player wins!'

        if computer_move > human_move:
            return 'Computer wins!'

        return "It's a draw!"

    def _update_score(self, winner):
        match winner:
            case 'Player wins!':
                self.scores.add_points('player', 1)
            case 'Computer wins!':
                self.scores.add_points('computer', 1)
            case "It's a draw!":
                self.scores.add_points('computer', .5)
                self.scores.add_points('player', .5)

    def _display_winner(self, winner):
        match winner:
            case 'Player wins!':
                print(messages['win'])
            case 'Computer wins!':
                print(messages['lose'])
            case "It's a draw!":
                print(messages['tie'])

    def _display_match_winner(self):
        print(messages['match_end'].format(match_winner=self._match_winner()))

    def _clear_screen(self):
        os.system('clear')

    def _play_again(self):
        answer = input(messages['play_again'])
        return answer.lower().startswith('y')

    def _match_winner(self):
        if self.scores.score['player'] >= Scoreboard.GAMES_TO_WIN:
            return messages['win']
        return messages['computer_win'].format(computer=self._computer.name)

    def _is_max_game_length(self):
        return any([num for num in self.scores.score.values()
                    if num >= Scoreboard.GAMES_TO_WIN])

with open('rps_game.json', 'r') as file:
    messages = json.load(file)

game = RPSGame()

game.play()