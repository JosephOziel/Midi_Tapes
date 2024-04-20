from midiutil import *
from math import *
import os
from random import *

Tape = MIDIFile(2)

# function to use: f(x)=sin(x)^1/3+cos(x)^1/5

os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes\\Symmetry_Pieces')
with open('Kollatz_Musik.mid', 'wb') as output_file:
    Tape.writeFile(output_file)