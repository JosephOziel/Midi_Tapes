from midiutil import *
import os
from random import *
from math import pi

# A133058: a(0) = a(1) = 1; for n > 1, a(n) = a(n-1) + n + 1 if a(n-1) and n are coprime, otherwise a(n) = a(n-1)/gcd(a(n-1),n).
seq = [1,1,4,8,2,8,4,12,3,1,12,24,2,16,8,24,3,21,7,27,
 48,16,8,32,4,30,15,5,34,64,32,64,2,36,18,54,3,41,
 80,120,3,45,15,59,104,150,75,123,41,91,142,194,97,
 151,206,262,131,189,248,308,77,139,202,266,133,
 199,266,334,167]
seq2 = [abs(v-35) for v in seq]
seq3 = [(v+35) for v in reversed(seq)]

Tape = MIDIFile(3)

Tape.addTempo(0, 0, 108.88)

time = 0

def duration(v):
    if v <= 10:
        return v/8
    elif v <= 50:
        return v/45
    elif v <= 100:
        return v/85
    elif v <= 150:
        return v/135
    elif v <= 200:
        return v/185
    else:
        return v/235
    
# def duration(v):
#     return v / (10 if v<=10 else min(250,50*round((v+24)/50)))    

for v in seq:
    Tape.addProgramChange(0, 0, time, (v%128)+1)
    Tape.addNote(0, 0, (v%88)+1, time, duration(v), (v%50)+50)
    time = time + duration(v)

time = time + 2.1

for v in seq2:
    Tape.addProgramChange(0, 0, time, (v%128)+1)
    Tape.addNote(0, 0, (v%88)+1, time, duration(v), (v%50)+50)
    time = time + duration(v)

time = time + 2.2

for v in seq3:
    Tape.addProgramChange(0, 0, time, (v%128)+1)
    Tape.addNote(0, 0, (v%88)+1, time, duration(v), (v%50)+50)
    time = time + duration(v)

#-------------------------------

# A fractal array resembling the shape of a conifer tree read by rows. A mirror symmetric array of numbers where the n-th term is equal to the number of terms in the n-th row of the array.
cseq = [1,2,3,4,1,5,6,2,3,7,8,9,4,1,5,10,11,6,2,3,7,12,
 13,14,15,8,16,17,9,4,1,5,10,18,19,11,6,2,3,7,12,
 20,21,13,8,4,1,5,9,14,22,23,15,16,24,25,26,17,10,
 18,27,28,19,11,6,2,3,7,12,20,29,30,21,13,8]
cseq2 = [(x+45) for x in reversed(cseq)]
cseq3 = [(88-(x+21)) for x in cseq]

time = 50

Tape.addTempo(1, time, 123.45)

for v in [(x+25) for x in cseq]:
    Tape.addProgramChange(1, 1, time, (v%128)+1)
    Tape.addNote(1, 1, (v%88)+1, time, duration(v), (v%50)+50)
    time = time + duration(v)

time = time + 2.3

for v in cseq2:
    Tape.addProgramChange(1, 1, time, (v%128)+1)
    Tape.addNote(1, 1, (v%88)+1, time, duration(v), (v%50)+50)
    time = time + duration(v)

time = time + 2.4

for v in cseq3:
    Tape.addProgramChange(1, 1, time, (v%128)+1)
    Tape.addNote(1, 1, (v%88)+1, time, duration(v), (v%50)+50)
    time = time + duration(v)

#-------------------------------

rseq = [randint(1, 90) for _ in range(301)]

time = 190

Tape.addTempo(2, time, 33*pi)

for p in rseq[0:31]:
    Tape.addProgramChange(2, 2, time, p)
    Tape.addNote(2, 2, p, time, 1, 100)
    time = time + 1

for p in rseq[31:61]:
    Tape.addProgramChange(2, 2, time, p)
    Tape.addNote(2, 2, p, time, 0.9, 100)
    time = time + 0.9

for p in rseq[61:91]:
    Tape.addProgramChange(2, 2, time, p)
    Tape.addNote(2, 2, p, time, 0.8, 100)
    time = time + 0.8

for p in rseq[91:121]:
    Tape.addProgramChange(2, 2, time, p)
    Tape.addNote(2, 2, p, time, 0.7, 100)
    time = time + 0.7

for p in rseq[121:151]:
    Tape.addProgramChange(2, 2, time, p)
    Tape.addNote(2, 2, p, time, 0.6, 100)
    time = time + 0.6

for p in rseq[151:181]:
    Tape.addProgramChange(2, 2, time, p)
    Tape.addNote(2, 2, p, time, 0.5, 100)
    time = time + 0.5

for p in rseq[181:211]:
    Tape.addProgramChange(2, 2, time, p)
    Tape.addNote(2, 2, p, time, 0.4, 100)
    time = time + 0.4

for p in rseq[211:241]:
    Tape.addProgramChange(2, 2, time, p)
    Tape.addNote(2, 2, p, time, 0.3, 100)
    time = time + 0.3

for p in rseq[241:271]:
    Tape.addProgramChange(2, 2, time, p)
    Tape.addNote(2, 2, p, time, 0.2, 100)
    time = time + 0.2

for p in rseq[271:301]:
    Tape.addProgramChange(2, 2, time, p)
    Tape.addNote(2, 2, p, time, 0.1, 100)
    time = time + 0.1

Tape.addProgramChange(2, 2, time, rseq[300])
Tape.addNote(2, 2, rseq[300], time, 4, 100)

#-------------------------------
    
time = 240

for v in seq[21:32]:
    Tape.addProgramChange(0, 0, time, (v%128)+1)
    Tape.addNote(0, 0, (v%88)+1, time, 2.7, 100)
    time = time + 12


os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes\\Tape_3')
with open('Tape_3.mid', 'wb') as output_file:
    Tape.writeFile(output_file)