from typing import Any
from fractions import Fraction
from dataclasses import dataclass
import random

class SingleTon:
    _instances = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls, *args, **kwargs)
        return cls._instances[cls]
    
class Pitch(SingleTon):      
    def __init__(self, pitch: str, ord: int) -> None:
        self._pitch = pitch
        self._ord = ord
    
    def __gt__(self, __value) -> bool:
        return self._ord > __value._ord
    
    def __str__(self):
        return self._pitch

class Do (Pitch):
    def __init__(self) -> None:
        super().__init__('C', 1)  

class Re (Pitch):
    def __init__(self) -> None:
        super().__init__('D', 2)
        
class Mi (Pitch):
    def __init__(self) -> None:
        super().__init__('E', 3)
        
class Fa (Pitch):
    def __init__(self) -> None:
        super().__init__('F', 4)
        
class Sol (Pitch):
    def __init__(self) -> None:
        super().__init__('G', 5)

class La (Pitch):
    def __init__(self) -> None:
        super().__init__('A', 6)

class Si (Pitch):
    def __init__(self) -> None:
        super().__init__('B', 7)

class Rest(Pitch):
    def __init__(self) -> None:
        super().__init__('Z', 0)


class Duration(SingleTon): 
    def __init__(self, duration) -> None:
        self._duration = duration
    
    def __str__(self):
        return str(self._duration)

class WholeNote(Duration):
    def __init__(self) -> None:
        super().__init__(4)

class HalfNote(Duration):
    def __init__(self) -> None:
        super().__init__(2)

class QuarterNote(Duration):
    def __init__(self) -> None:
        super().__init__(1)

class Eighth(Duration):
    def __init__(self) -> None:
        super().__init__(Fraction(1, 2))

class Sixteenth(Duration):
    def __init__(self) -> None:
        super().__init__(Fraction(1, 4))

class ThirtySecond(Duration):
    def __init__(self) -> None:
        super().__init__(Fraction(1, 8))

class SixtyForth(Duration):
    def __init__(self) -> None:
        super().__init__(Fraction(1, 16))

class Note:
    def __init__(self, pitch, duration) -> None:
        self.pitch = pitch
        self.duration = duration
    
    def __eq__(self, __value) -> bool:
        return self.pitch == __value.pitch and self.duration == __value.duration
    
    def __str__(self):
        return f"{self.pitch}-{self.duration}"

def generate_song(n_notes=10):
    notes = []
    for noteIndex in range(n_notes):
        notes.append(Note(random.choice(pitchs)(), random.choice(durations)()))
    return notes

def display_notes(notes):
    for note in notes:
        print(note, end=', ' if note != notes[-1] else '')

QUARTER_REST = Note(Rest(), QuarterNote())

def count_quarter_rest(notes):
    return sum(note == QUARTER_REST for note in notes)
    
def get_max_pitch(notes):
    return max(notes, key=lambda note: note.pitch)

if __name__ == '__main__':
    pitchs = (Do, Re, Mi, Fa, Sol, La, Si, Rest)
    durations = (WholeNote, HalfNote, QuarterNote, Eighth, Sixteenth, ThirtySecond, SixtyForth)
    
    n_notes = int(input('Please enter number of notes: '))
    notes = generate_song(n_notes)
    display_notes(notes)
    
    print(f"\nQuarter rest: {count_quarter_rest(notes)}")
    print(f"Max pitch: {get_max_pitch(notes)}")