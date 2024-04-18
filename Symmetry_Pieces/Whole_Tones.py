from midiutil import *
from math import *
import os
from random import *

Tape = MIDIFile(2)

os.chdir('C:\\Users\\vatis\\OneDrive\\Documents\\Midi_Tapes\\Symmetry_Pieces')
with open('Symmetry_1.mid', 'wb') as output_file:
    Tape.writeFile(output_file)