from midiutil import MIDIFile
from math import *
import os

Tape = MIDIFile(2)

piano = 0
rh = 0
lh = 1
tempo1 = 169

time = 0
time2 = 15  

volume = 100

Tape.addTempo(piano, 0, tempo1)

intervals = [(pi/8)*x for x in range(0,16)]

def calc_sin_pitch(x,a):
    return ceil(44*sin(x)+a)
def calc_cos_pitch(x,a):
    return ceil(44*cos(x)+a)

for _ in range(20):
#    volume = volume - 3
    for x in intervals:
        Tape.addNote(piano, rh, calc_sin_pitch(x, 44), time, 0.3333, volume)
        time = time + 0.5

volume = 100

for _ in range(15):
#    volume = volume - 4
    for x in intervals:
        Tape.addNote(piano, lh, calc_cos_pitch(x, 45), time2, 0.7, volume)
        time2 = time2 + 0.7

os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes')
with open('Tape_1.mid', 'wb') as output_file:
    Tape.writeFile(output_file)