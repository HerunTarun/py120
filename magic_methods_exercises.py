# exercise 1
class Car:
    def __init__(self, name, year, color):
        self._name = name
        self._year = year
        self._color = color
        
    def __str__(self):
        return f'{self._color.title()} {self._year} {self._name}'
    
    def __repr__(self):
        return f"Car({repr(self._name)}, {repr(self._year)}, {repr(self._color)})"
    
    
vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

# exercise 2
import math
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)
    
    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        return (self.x * other.x) + (self.y * other.y)
    
    def __abs__(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 + v2)      # Vector(18, 8)
print(v1 - v2) # Vector(-8, 16)
print(v1 * v2) # 17
print(abs(v1)) # 13.0

# exercise 3
class Candidate:
    def __init__(self, name):
        self.name = name
        self._vote = 0
        
    def __iadd__(self, num):
        if not isinstance(num, int):
            return NotImplemented
        
        self._vote += num
        
        return self
    
class Election:
    def __init__(self, candidates):
        self.candidates = candidates
    
    def winner(self):
        all_results = {candidate._vote: candidate.name for candidate in self.candidates}
        winner = max(all_results)
        return (all_results[winner], winner)

    def results(self):
        for candidate in self.candidates:
            print(f'{candidate.name}: {candidate._vote} votes')

        winner, winner_vote = self.winner()
        total_votes = sum([candidate._vote for candidate in self.candidates])
        percent = (winner_vote / total_votes) * 100

        print(f'{winner} won: {percent}% of votes')
            
            
mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()
            