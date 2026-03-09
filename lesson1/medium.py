# exercise 1
class CircularBuffer:
    def __init__(self, buffer_size):
        self._buffer_size = buffer_size
        self._buffer = []
        
    @property
    def buffer_size(self):
        return self._buffer_size
    
    def put(self, obj):
        self._buffer.append(obj)
        if len(self._buffer) > self._buffer_size:
            self._buffer.pop(0)
        
    def get(self):
        if not self._buffer:
            return None
        return self._buffer.pop(0)

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True
# better version
class CircularBuffer:
    def __init__(self, buffer_size):
        self._buffer_size = buffer_size
        self._buffer = [None for i in range(buffer_size)]
        self._next = 0
        self._oldest = 0
        
    @property
    def buffer_size(self):
        return self._buffer_size
    
    def put(self, obj):
        if self._buffer[self._next] is not None:
            self._oldest = (self._next + 1) % self.buffer_size
        
        self._buffer[self._next] = obj
        self._next = (self._next + 1) % self.buffer_size
            
    def get(self):
        value = self._buffer[self._oldest]
        self._buffer[self._oldest] = None
        if value is not None:
            self._oldest = (self._oldest + 1) % self.buffer_size
        return value
        

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get())             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True

# exercise 2
import random

class GuessingGame:
    NUMBER_OF_GUESSES = 7
    def __init__(self):
        self._guess = None
        self._guesses = NUMBER_OF_GUESSES
        self._number = None
    
    def play(self):
        self._number = random.randint(1, 100)
        self._guesses = 7
        while True:
            self._display_remaining_guesses()
            self._guess = self._enter_guess()
            guess_result = self._is_correct_guess(self._guess)
            if guess_result:
                self._display_win()
                break
            self._display_incorrect_guess_message(self._guess)    
            self._guesses -= 1
            if self._guesses == 0:
                self._display_loss()
                break
            
    def _reset(self):
        self._guesses = NUMBER_OF_GUESSES
    def _enter_guess(self):
        guess  = input('Enter a number between 1 and 100:')
        
        while True:
            try:
                num = int(guess)
            except ValueError:
                guess = self._display_retry_after_invalid()
                continue
            
            if not self._is_valid_guess(num):
                guess = self._display_retry_after_invalid()
                continue
            return num
    
    def _display_remaining_guesses(self):
        print(f'You have {self._guesses} guesses remaining.')
    
    def _is_valid_guess(self, num):
        if not isinstance(num, int):
            return False
        if num < 1 or num > 100:
            return False
        return True
    
    def _is_correct_guess(self, guess):
        if guess == self._number:
            return True
        return False
    
    def _display_win(self):
        print("That's the number!")
        print()
        print('You won!')
    
    def _display_incorrect_guess_message(self, guess):
        if guess < self._number:
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')
    
    def _display_retry_after_invalid(self):
        return input('Invalid guess. Enter a number between 1 and 100:')
    
    def _display_loss(self):
        print('You have no more guesses. You lost!')
        
        
game = GuessingGame()
game.play()
 # better solution
import random

class GuessingGame:
    NUMBER_OF_GUESSES = 7
    def __init__(self):
        self._guesses = NUMBER_OF_GUESSES
        self._number = None
    
    def play(self):
        self._number = random.randint(1, 100)
        self._guesses = 7
        while True:
            self._display_remaining_guesses()
            guess = self._enter_guess()
            guess_result = self._is_correct_guess(guess)
            if guess_result:
                self._display_win()
                break
            self._display_incorrect_guess_message(guess)    
            self._guesses -= 1
            if self._guesses == 0:
                self._display_loss()
                break
            
    def _reset(self):
        self._guesses = NUMBER_OF_GUESSES
    def _enter_guess(self):
        while True:
            guess  = input('Enter a number between 1 and 100:')
            try:
                num = int(guess)
            except ValueError:
                guess = self._display_retry_after_invalid()
                continue
            
            if not self._is_valid_guess(num):
                guess = self._display_retry_after_invalid()
                continue
                
            return num
    
    def _display_remaining_guesses(self):
        print(f'You have {self._guesses} guesses remaining.')
    
    def _is_valid_guess(self, num):
        if not isinstance(num, int):
            return False
        if num < 1 or num > 100:
            return False
        return True
    
    def _is_correct_guess(self, guess):
        if guess == self._number:
            return True
        return False
    
    def _display_win(self):
        print("That's the number!")
        print()
        print('You won!')
    
    def _display_incorrect_guess_message(self, guess):
        if guess < self._number:
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')
    
    def _display_retry_after_invalid(self):
        return input('Invalid guess. Enter a number between 1 and 100:')
    
    def _display_loss(self):
        print('You have no more guesses. You lost!')
        
        
game = GuessingGame()
game.play()
# further exploration

# exercise 3
import random
import math

class GuessingGame:
    def __init__(self, low, high):
        self._number = None
        self._low = low
        self._high = high
        self._max_guesses = self._calculate_number_of_guesses()
        self._guesses = self._max_guesses
    
    def play(self):
        self._number = random.randint(self._low, self._high)
        self._reset()
        while self._guesses > 0:
            self._display_remaining_guesses()
            guess = self._enter_guess()
            
            if self._is_correct_guess(guess):
                self._display_win()
                return
            
            self._display_incorrect_guess_message(guess)    
            self._guesses -= 1
        self._display_loss()
    
    def _calculate_number_of_guesses(self):
        return int(math.log2(self._high - self._low + 1)) + 1
    
    def _reset(self):
        self._guesses = self._max_guesses
    
    def _enter_guess(self):
        while True:
            guess  = input(f'Enter a number between {self._low} and {self._high}:')
            try:
                num = int(guess)
            except ValueError:
                guess = self._display_retry_after_invalid()
                continue
            
            if not self._is_valid_guess(num):
                guess = self._display_retry_after_invalid()
                continue
                
            return num
    
    def _display_remaining_guesses(self):
        guess_word = 'guess' if self._guesses == 1 else 'guesses'
        print(f'You have {self._guesses} {guess_word} remaining.')
    
    def _is_valid_guess(self, num):
        return self._low <= num <= self._high
    
    def _is_correct_guess(self, guess):
        return guess == self._number
    
    def _display_win(self):
        print("That's the number!")
        print()
        print('You won!')
    
    def _display_incorrect_guess_message(self, guess):
        if guess < self._number:
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')
    
    def _display_retry_after_invalid(self):
        return input(f'Invalid guess. Enter a number between {self._low} and {self._high}:')
    
    def _display_loss(self):
        print('You have no more guesses. You lost!')
        
        
game = GuessingGame(500, 1500)
game.play()

# exercise 4
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._face_to_value(self.rank) == self._face_to_value(other.rank)
        
    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._face_to_value(self.rank) > self._face_to_value(other.rank)
    
    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._face_to_value(self.rank) < self._face_to_value(other.rank)
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def _face_to_value(self, rank):
        match rank:
            case 'Ace':
                return 14
            case 'King':
                return 13
            case 'Queen':
                return 12
            case 'Jack':
                return 11
            case _:
                return rank
    
cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True

# exercise 5
import random 
class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    def __init__(self):
        self.deck = self._new_deck()
        
    def draw(self):
        if not self.deck:
            self.deck = self._new_deck()
                        
        return self.deck.pop()

    def _new_deck(self):
        cards = [Card(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]
        random.shuffle(cards)
        return cards
        

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._face_to_value(self.rank) == self._face_to_value(other.rank)
        
    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._face_to_value(self.rank) > self._face_to_value(other.rank)
    
    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._face_to_value(self.rank) < self._face_to_value(other.rank)
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __repr__(self):
        return f'Card({repr(self.rank)}, {repr(self.suit)})'
    
    def _face_to_value(self, rank):
        match rank:
            case 'Ace':
                return 14
            case 'King':
                return 13
            case 'Queen':
                return 12
            case 'Jack':
                return 11
            case _:
                return rank
            
deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).
   

# exercise 6
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._face_to_value(self.rank) == self._face_to_value(other.rank)
        
    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._face_to_value(self.rank) > self._face_to_value(other.rank)
    
    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._face_to_value(self.rank) < self._face_to_value(other.rank)
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __repr__(self):
        return f'Card({repr(self.rank)}, {repr(self.suit)})'
    
    def _face_to_value(self, rank):
        match rank:
            case 'Ace':
                return 14
            case 'King':
                return 13
            case 'Queen':
                return 12
            case 'Jack':
                return 11
            case _:
                return rank

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    
    def __init__(self):
        self.deck = self._new_deck()
        
    def draw(self):
        if not self.deck:
            self.deck = self._new_deck()
                        
        return self.deck.pop()

    def _new_deck(self):
        cards = [Card(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]
        random.shuffle(cards)
        return cards
    
 
class PokerHand:
    def __init__(self, deck):
        self.cards = [deck.draw() for _ in range(5)]
        self.card_ranks = [card.rank for card in sorted(self.cards)]
        self.card_suits = {card.suit for card in self.cards}
        

    def print(self):
        for card in self.cards:
            print(card)
        
    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        royal_flush_ranks = {10, 'Jack', 'Queen', 'King', 'Ace'}
        
        if set(self.card_ranks) == royal_flush_ranks and len(self.card_suits) == 1:
            return True
        
        return False
            

    def _is_straight_flush(self):
        index = Deck.RANKS.index(self.card_ranks[0])
        straight_flush = Deck.RANKS[index: index + 5]
        
        if self.card_ranks == straight_flush and len(self.card_suits) == 1:
            return True
        
        return False

    def _is_four_of_a_kind(self):
        for card in self.card_ranks:
            if self.card_ranks.count(card) == 4:
                return True
        
        return False

    def _is_full_house(self):
        full_house_count = {3, 2}
        card_count = []
        for card in self.card_ranks:
            if self.card_ranks.count(card) in full_house_count:
                card_count.append(self.card_ranks.count(card))
        
        if set(card_count) == full_house_count:
            return True
        return False

    def _is_flush(self):
        if len(self.card_suits) == 1:
            return True
        return False

    def _is_straight(self):
        index = Deck.RANKS.index(self.card_ranks[0])
        straight = Deck.RANKS[index: index + 5]
        
        if self.card_ranks == straight:
            return True
        return False

    def _is_three_of_a_kind(self):
        for card in self.card_ranks:
            if self.card_ranks.count(card) == 3:
                return True
        return False

    def _is_two_pair(self):
        card_count = []
        for card in self.card_ranks:
            if self.card_ranks.count(card) == 2:
                card_count.append('card')
        if card_count.count('card') == 4:
            return True
        return False

    def _is_pair(self):
        for card in self.card_ranks:
            if self.card_ranks.count(card) == 2:
                return True
        return False



            
hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self.deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")