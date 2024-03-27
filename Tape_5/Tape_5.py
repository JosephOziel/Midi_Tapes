# This script takes a bunch of .wav files from a given folder, chops them up into
# lots of short snippets and then randomly puts the snippets of multiple simultaneous
# audios back together, preserving the original order of the snippets of each source
# audio in the result. idk, have fun

import os
import random
import numpy as np
import soundfile as sf

# enter parameters here
simultaneous_audios = 3
min_chop_seconds = 1.5
max_chop_seconds = 5
result_filename = "Tape_5"

# Adjust only if necessary
samples_dir = "pieces"
fs = 44100

# calculating and checking some data and reading files
files = os.listdir(''.join(["./",samples_dir,"/"]))
filepaths = [f"./{samples_dir}/{file}" for file in files if ".wav" in file]
assert min_chop_seconds <= max_chop_seconds, "Error, \"min_chop_seconds\" must be smaller than or equal to \"max_chop_seconds\""
assert int(fs*min_chop_seconds) > 0, "Error, \"min_chop_seconds\" is too small"
assert simultaneous_audios <= len(files), f"Error, \"simultaneous_audios\" must be less or equal to the number of files in ./{samples_dir}/"
assert simultaneous_audios >= 2, f"Error, \"simultaneous_audios\" must be at least 2"
assert len(filepaths) > 1, f"Error, no .wav files found in ./{samples_dir}/"
audios_and_fs = [sf.read(audio) for audio in filepaths]
assert all([True if elem[1] == fs else False for elem in audios_and_fs]), f"Error, the samplerate fs of one or more .wav files in ./{samples_dir}/ does not match the given fs = {fs}Hz"
audios = [elem[0] for elem in audios_and_fs]
print("reading files complete")
min_chop_frames = int(fs*min_chop_seconds) 
max_chop_frames = int(fs*max_chop_seconds)


# defining some functions

# choose some files to start with
def choose_random_start(files: list, amount: int=simultaneous_audios):
    """
    Choose a random subset of audio files to start with.

    Parameters:
    -----------
    files : list
        A list of ndarrays representing the individual audio files in the samples directory
    amount : int
        The number of files that should be chopped together at any given time

    Returns:
    --------
    list of ndarrays
        Random subset of the input files
    """
    remaining_files = files
    chosen_files = []
    for i in range(amount):
        idx = random.randint(0, len(remaining_files)-1)
        chosen_files.append(remaining_files[idx])
        del remaining_files[idx]
    return chosen_files, remaining_files


# queues new file once one of the currently used ones goes empty
def fill_up(current_files: list, remaining_files: list):
    """
    When one file has been used up for chopping, choose a new file randomly from the remaining files to queue up into the algorithm.

    Parameters:
    -----------
    current_files : list
        A list of ndarrays representing the individual audio files that are currently used for chopping.
    remaining_files : list
        A list of ndarrays representing the individual audio files that have not yet been used for chopping.

    Returns:
    --------
    list of ndarrays
        List containing all elements of current_files plus one random element from remaining_files
    """
    new_remaining_files = remaining_files
    new_current_files = current_files
    idx = random.randint(0, len(remaining_files)-1)
    new_current_files.append(remaining_files[idx])
    del new_remaining_files[idx]
    return new_current_files, new_remaining_files

# initialize
musik = []
current_files, remaining_files = choose_random_start(audios, simultaneous_audios)

# the fun, generate musik
while True:
    file_idx = random.randint(0,simultaneous_audios-1)
    length = random.randint(min_chop_frames, max_chop_frames)
    file = current_files[file_idx]
    # if a file gets used up and there's nothing new to queue, stop the loop
    if len(file) < length and len(remaining_files) == 0:
        break
    # if a file gets used up and there's more files to queue, queue a new file randomly
    elif len(file) == 0 or len(file) < length:
        del current_files[file_idx]
        current_files, remaining_files = fill_up(current_files, remaining_files)
    # else: scrape off some of the currently selected file and append it to the result
    else:
        current_files[file_idx] = file[length:]
    musik.extend(file[:length])

# write result to .wav file
print(len(musik)/44100, "seconds of music generated (", len(musik)/2646000, "minutes ), writing to file...")
final_musik = np.asarray(musik)
sf.write(f"{result_filename}.wav", final_musik, fs)
print("done!")