from midiutil import *
from math import *
import os
from random import *

T = MIDIFile(1) #maybe 2 channels later?

temp = 150 # subject to change
T.addTempo(0,0,temp)

T.addProgramChange(0,0,0,1)
T.addProgramChange(0,1,0,1)

#COLLATZ MUSIC

dur = 0.5
time = 0
o = 29

def val(v):
    if v<=108:
        return v
    elif v < 21:
        return v+21
    else: 
        return v%87+21

def kol1(s):
    global time
    T.addNote(0,0,val(s+o),time,dur/2,100)
    time = time + dur
    while s != 1:
        if (s%2)==0:
            s = s//2
            T.addNote(0,0,val(s+o),time,dur/2,100)
            time = time + dur
        else:
            s = s*3+1
            T.addNote(0,0,val(s+o),time,dur/2,100)
            time = time + dur
    time = time + 1.5

def kol2(s, h):
    global time
    T.addNote(0,0,val(s+o),time,dur/2,100)
    T.addNote(0,0,val(s+o+h),time,dur/2,100)
    time = time + dur
    while s != 1:
        if (s%2)==0:
            s = s//2
            T.addNote(0,0,val(s+o),time,dur/2,100)
            T.addNote(0,0,val(s+o+h),time,dur/2,100)
            time = time + dur
        else:
            s = s*3+1
            T.addNote(0,0,val(s+o),time,dur/2,100)
            T.addNote(0,0,val(s+o+h),time,dur/2,100)
            time = time + dur
    time = time + 1.5

#symmetry
def kol3(s, h1, h2, i):
    global time
    T.addNote(0,0,val(s+o),time,dur/2,100)
    T.addNote(0,0,val(s+o+h1),time,dur/2,100)
    T.addNote(0,0,val(abs(i-((s+o)-i))),time,dur/2,100)
    T.addNote(0,0,val(abs((i-((s+o)-i))-h2)),time,dur/2,100)
    time = time + dur
    while s != 1:
        if (s%2)==0:
            s = s//2
            T.addNote(0,0,val(s+o),time,dur/2,100)
            T.addNote(0,0,val(s+o+h1),time,dur/2,100)
            T.addNote(0,0,val(abs(i-((s+o)-i))),time,dur/2,100)
            T.addNote(0,0,val(abs((i-((s+o)-i))-h2)),time,dur/2,100)
            time = time + dur
        else:
            s = s*3+1
            T.addNote(0,0,val(s+o),time,dur/2,100)
            T.addNote(0,0,val(s+o+h1),time,dur/2,100)
            T.addNote(0,0,val(abs(i-((s+o)-i))),time,dur/2,100)
            T.addNote(0,0,val(abs((i-((s+o)-i))-h2)),time,dur/2,100)
            time = time + dur
    time = time + 1.5

#--MODIFY AND FIX FOR LATER: POLYRHYTHMS
def kol4(s, h, r):
    global time, time2
    T.addNote(0,0,val(s+o),time,dur/2,100)
    T.addNote(0,1,val(s+o-h),time2,r,100)
    time = time + dur
    time2 = time2 + r
    while s != 1:
        if (s%2)==0:
            s = s//2
            T.addNote(0,0,val(s+o),time,dur/2,100)
            T.addNote(0,1,val(s+o-h),time2,r,100)
            time = time + dur
            time2 = time2 + r
        else:
            s = s*3+1
            T.addNote(0,0,val(s+o),time,dur/2,100)
            T.addNote(0,1,val(s+o-h),time2,r,100)
            time = time + dur
            time2 = time2 + r
    time = time + 1.5
    time2 = time

#-------Piece-------
    
for i in range(1,16):
    kol1(i)

for i in range(16, 30):
    kol2(i, 3)

for i in range(30, 42):
    kol3(i, 4, 3, 60) 

time = time + 1
time2 = time

os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes\\Programmed_Pieces\\Kollatz_Musik')
with open('Kollatz_Musik.mid', 'wb') as output_file:
    T.writeFile(output_file)