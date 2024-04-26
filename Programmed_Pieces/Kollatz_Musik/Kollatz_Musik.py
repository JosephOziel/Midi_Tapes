from midiutil import *
from math import *
import os
from random import *

T = MIDIFile(1) #maybe 2 channels later?

T.addProgramChange(0,0,0,1)
T.addProgramChange(0,1,0,1)
T.addProgramChange(0,2,0,1)
T.addProgramChange(0,3,0,1)

#COLLATZ MUSIC

dur = 0.5
time = 0
o = 29

def val(v):
    if v < 21:
        return v+21
    elif v<=108:
        return v
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
def kol3(s, h1, h2, i, ch):
    global time
    T.addNote(0,ch,val(s+o),time,dur/2,100)
    T.addNote(0,ch,val(s+o+h1),time,dur/2,100)
    T.addNote(0,ch,val(abs(i-((s+o)-i))),time,dur/2,100)
    T.addNote(0,ch,val(abs((i-((s+o)-i))+h2)),time,dur/2,100)
    time = time + dur
    while s != 1:
        if (s%2)==0:
            s = s//2
            T.addNote(0,ch,val(s+o),time,dur/2,100)
            T.addNote(0,ch,val(s+o+h1),time,dur/2,100)
            T.addNote(0,ch,val(abs(i-((s+o)-i))),time,dur/2,100)
            T.addNote(0,ch,val(abs((i-((s+o)-i))+h2)),time,dur/2,100)
            time = time + dur
        else:
            s = s*3+1
            T.addNote(0,ch,val(s+o),time,dur/2,100)
            T.addNote(0,ch,val(s+o+h1),time,dur/2,100)
            T.addNote(0,ch,val(abs(i-((s+o)-i))),time,dur/2,100)
            T.addNote(0,ch,val(abs((i-((s+o)-i))+h2)),time,dur/2,100)
            time = time + dur
    time = time + 1.5

#maybe add another version with harmony? FIXX
def kol4(s, h, r, cha):
    global time3, time2
    T.addNote(0,cha,val(s+o),time3,r,100)
    T.addNote(0,cha,val(s+o+h),time3,r,100)
    time3 = time3 + r
    while s != 1:
        if (s%2)==0:
            s = s//2
            T.addNote(0,cha,val(s+o),time3,r,100)
            T.addNote(0,cha,val(s+o+h),time3,r,100)
            time3 = time3 + r
        else:
            s = s*3+1
            T.addNote(0,cha,val(s+o),time3,r,100)
            T.addNote(0,cha,val(s+o+h),time3,r,100)
            time3 = time3 + r

#-------Piece-------

k = 10 # maybe 9?
    
temp = 159 
T.addTempo(0,time,temp)

for i in range(1,k+1):
    kol1(i)

T.addTempo(0,time,temp+10)

for i in range(k+1, 2*k):
    kol2(i, 3)

T.addTempo(0,time,temp+20)

for i in range(2*k, 3*k-3):
    kol3(i, 4, -3, 60, 0) 

time = time + 1

T.addTempo(0,time,temp+27)

for i in range(3*k-1, 3*k+4):
    time2 = time 
    kol3(i, 3, -4, 61, 0)
    o = 33
    time = time2
    kol3(i, 7, -6, 61, 0)
    o = 21
    time3 = time2
    kol4(i, 2, 1/3, 1)
    time3 = time
    o = 29

for i in range(3*k+4, 3*k+9):
    time2 = time 
    kol3(i, 3, -4, 61, 0)
    o = 33
    time = time2
    kol3(i, 7, -6, 61, 0)
    # o = 21 FIX
    # time = time2
    # time3 = time
    # kol4(i, 1/3, 1)
    o = 29
    # time3 = time

time2 = time

# for i in range(3*k+9, 3*k+14):
#     kol3(i, 3, -4, 61)
#     kol4(i, 7, 2/3, 1)
#     time2 = time

os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes\\Programmed_Pieces\\Kollatz_Musik')
with open('Kollatz_Musik.mid', 'wb') as output_file:
    T.writeFile(output_file)