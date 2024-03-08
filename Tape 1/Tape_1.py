from midiutil import *
from math import *
import os
from random import *

Tape = MIDIFile(2)

piano = 0
one = 0
two = 1
three = 2

tempo1 = 169

time = 0

volume = 90

Tape.addTempo(piano, one, tempo1)

Tape.addProgramChange(piano, one, time, 1)
Tape.addProgramChange(piano, two, time, 1)
Tape.addProgramChange(piano, three, time, 1)

intervals = [(pi/8)*x for x in range(16)]
intervals2 = [(pi/8)*x for x in range(102)]
intervals3 = [(1/16)*x for x in range (17)]

def calc_sin_pitch(x,a):
    return ceil(44*sin(x)+a)

def calc_cos_pitch(x,a):
    return ceil(44*cos(x)+a)

def calc_sin_divx_pitch(x,a):
    if x == 0:
        return a+46
    else:
        return ceil(46*(sin(x)/x)+a)
    
def calc_arcsin_pitch(x,a,b):
    return ceil(b*asin(x-1)+a)

def calc_arccos_pitch(x,a,b):
    return ceil(b*acos(x-1)+a)

for _ in range(20):
    for x in intervals:
        Tape.addNote(piano, one, calc_sin_pitch(x, 56), time, 0.3333, volume)
        time = time + 0.5

time = 25

for _ in range(15):
    for x in intervals:
        Tape.addNote(piano, two, calc_cos_pitch(x, 57), time, 0.7, volume)
        time = time + 0.7

time = 100

for x in intervals2:
    Tape.addNote(piano, three, calc_sin_divx_pitch(x, 21), time, 1.1, volume)
    time = time + 1.1

time = 211 

for _ in range (25):
    for x in intervals3:
        Tape.addNote(piano, one, calc_arcsin_pitch(x, 34, 3), time, 0.2, volume)
        time = time + 0.4

time = 236.6

for _ in range(21):
    for x in intervals3:
        Tape.addNote(piano, two, calc_arcsin_pitch(x, 56, 17), time, 0.3333, volume)
        time = time + 0.5

time = 257.6

for _ in range(18):
    for x in intervals3:
        Tape.addNote(piano, three, calc_arccos_pitch(x, 27, 26), time, 0.8, volume)
        time = time + 0.8

os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes')
with open('Tape_1.mid', 'wb') as output_file:
    Tape.writeFile(output_file)