from midiutil import *
from math import *
import os
from random import *

T = MIDIFile(1) #maybe 2 channels later?

temp = 150 # subject to change
T.addTempo(0,0,temp)

T.addProgramChange(0,0,0,1)

#COLLATZ MUSIC

dur = 0.5
time = 0
o = 29

def kol1(s):
    global time
    T.addNote(0,0,s+o,time,dur/2,100)
    time = time + dur
    while s != 1:
        if (s%2)==0:
            s = s//2
            T.addNote(0,0,s+o,time,dur/2,100)
            time = time + dur
        else:
            s = s*3+1
            T.addNote(0,0,s+o,time,dur/2,100)
            time = time + dur
    time = time + 1.5

for i in range(1,18):
    kol1(i)

os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes\\Programmed_Pieces\\Kollatz_Musik')
with open('Kollatz_Musik.mid', 'wb') as output_file:
    T.writeFile(output_file)