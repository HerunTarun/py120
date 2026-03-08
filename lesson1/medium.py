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
# exercise 5
# exercise 6