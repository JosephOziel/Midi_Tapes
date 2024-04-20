from midiutil import *
from math import *
import os
from random import *

Tape = MIDIFile(2)

def wholetonegen(s):
    # s is either 1 or 0 (the two kinds)
    l = []
    for _ in range(6):
        l.append(s)
        s = s+2
    return l

symm = 61

Tape.addTempo(0, 0, 169)
Tape.addProgramChange(0, 0, 0, 1)

w1 = wholetonegen(0)
w2 = wholetonegen(1)

time = 0

for _ in range(2*13):
    shuffle(w1)
    # full list: [1,2,3,4,5,6,7]
    w1 = [(n+choice([1,2,3,4,5,6,7,7,7])*12) for n in w1]
    harmo = choice([x for x in range(1, 13)])
    # print(w1)
    for n in w1:
        dur = choice([0.3, 0.2, 0.4, 0.6,0.7,0.8])
        Tape.addNote(0,0,n,time,dur,100)
        Tape.addNote(0,0,n+harmo,time,dur,100)
        Tape.addNote(0,0,symm-(n-symm),time,dur,100)
        Tape.addNote(0,0,abs((symm-(n-symm))-harmo),time,dur,100)
        time = time + dur
        # print([n,n+harmo,88-n,abs((88-n)-harmo)])
    w1 = wholetonegen(0)

time = 25
w2.reverse()
w2 = [(n+6*12) for n in w2]
for _ in range(3):
    harmo2 = choice([x for x in range(1, 13)])
    for n in w2:
        Tape.addNote(0,1,n,time,1,60)
        Tape.addNote(0,1,n+harmo2,time,1,60)
        Tape.addNote(0,1,n-harmo2,time,1,60)
        Tape.addNote(0,1,n-2*harmo2,time,1,60)
        time = time + 1
    time = time+15

os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes\\Symmetry_Pieces')
with open('Whole_Tones.mid', 'wb') as output_file:
    Tape.writeFile(output_file)