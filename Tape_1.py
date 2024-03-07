from midiutil import MIDIFile
from math import *
import os

Tape = MIDIFile(2)

piano = 0
rh = 0
lh = 1
tempo1 = 169

time = 0

Tape.addTempo(piano, 0, tempo1)

sinpitches = [(pi/8)*x for x in range(0,16)]

def calc_sin_pitch(x):
    return ceil(44*sin(x)+44)

for _ in range(20):
    for x in sinpitches:
        Tape.addNote(piano, rh, calc_sin_pitch(x), time, 0.3333, 100)
        time = time + 0.5

os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes')
with open('Tape_1.mid', 'wb') as output_file:
    Tape.writeFile(output_file)