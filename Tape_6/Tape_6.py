from midiutil import *
import os

Tape = MIDIFile(8)

# Messiaen fifth mode of transposition
scale = [60, 62, 64, 65, 66, 68, 70, 71]

tempo_interval = 0.21

init = 130 #BPM

instr = 1 #Piano, for now

num = 210

#---

Tape.addTempo(0, 0, init)
Tape.addProgramChange(0, 0, 0, instr)

time = 0

for _ in range(num):
    Tape.addNote(0, 0, scale[0], time, 1, 100)
    time = time + 1

#--
    
Tape.addTempo(1, 1, init+tempo_interval)
Tape.addProgramChange(1, 1, 0, instr)  

time = 0

for _ in range(num):
    Tape.addNote(1, 1, scale[1], time, 1, 100)
    time = time + 1

#--
    
Tape.addTempo(2, 2, init+2*tempo_interval)
Tape.addProgramChange(2, 2, 0, instr)  

time = 0

for _ in range(num):
    Tape.addNote(2, 2, scale[2], time, 1, 100)
    time = time + 1


#----
    
os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes\\Tape_6')
with open('Tape_6.mid', 'wb') as output_file:
    Tape.writeFile(output_file)