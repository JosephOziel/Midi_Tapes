from midiutil import *
import os

# A133058: a(0) = a(1) = 1; for n > 1, a(n) = a(n-1) + n + 1 if a(n-1) and n are coprime, otherwise a(n) = a(n-1)/gcd(a(n-1),n).
seq = [1,1,4,8,2,8,4,12,3,1,12,24,2,16,8,24,3,21,7,27,
 48,16,8,32,4,30,15,5,34,64,32,64,2,36,18,54,3,41,
 80,120,3,45,15,59,104,150,75,123,41,91,142,194,97,
 151,206,262,131,189,248,308,77,139,202,266,133,
 199,266,334,167]
seq2 = [abs(v-35) for v in seq]
seq3 = [(v+35) for v in reversed(seq)]

Tape = MIDIFile(1)

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
for v in seq2:
    Tape.addProgramChange(0, 0, time, (v%128)+1)
    Tape.addNote(0, 0, (v%88)+1, time, duration(v), (v%50)+50)
    time = time + duration(v)
for v in seq3:
    Tape.addProgramChange(0, 0, time, (v%128)+1)
    Tape.addNote(0, 0, (v%88)+1, time, duration(v), (v%50)+50)
    time = time + duration(v)

os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes\\Tape_3')
with open('Tape_3.mid', 'wb') as output_file:
    Tape.writeFile(output_file)