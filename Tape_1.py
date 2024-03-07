from midiutil import MIDIFile
from math import *
import os

Tape = MIDIFile(2)

piano = 0
one = 0
two = 1
three = 2

tempo1 = 169

time = 0
time2 = 25
time3 = 65

volume = 90

Tape.addTempo(piano, one, tempo1)
Tape.addProgramChange(piano, one, time, 1)
Tape.addProgramChange(piano, two, time, 1)

intervals = [(pi/8)*x for x in range(0,16)]
intervals2 = [(pi/8)*x for x in range(62)]

def calc_sin_pitch(x,a):
    return ceil(44*sin(x)+a)

def calc_cos_pitch(x,a):
    return ceil(44*cos(x)+a)

def calc_sin_divx_pitch(x,a):
    if x == 0:
        return a
    else:
        return ceil(46*(sin(x)/x)+a)

for _ in range(20):
    for x in intervals:
        Tape.addNote(piano, one, calc_sin_pitch(x, 56), time, 0.3333, volume)
        time = time + 0.5

for _ in range(15):
    for x in intervals:
        Tape.addNote(piano, two, calc_cos_pitch(x, 57), time2, 0.7, volume)
        time2 = time2 + 0.7

for x in intervals2:
    Tape.addNote(piano, three, calc_sin_divx_pitch(x, 10), time3, 1.1, volume)
    time3 = time3 + 1.1

os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes')
with open('Tape_1.mid', 'wb') as output_file:
    Tape.writeFile(output_file)