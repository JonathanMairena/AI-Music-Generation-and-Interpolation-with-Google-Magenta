from mido import MidiFile
import os
import sys

source = "./pop909_midi_val" # Main Folder
files = os.listdir(source)
# os.remove("./pop909_midi_test/.DS_Store") # incase there is this crazy mac folder

for i in range(5,len(files)):  # iterate through files unconverted to melody
	file_path = os.path.join(source,files[i]) # make a path for individual file
	print(file_path) # print progress
	mid = MidiFile(file_path, clip = "True") # declare as a midi

	if(len(mid.tracks) > 1 ): # if it has more than the top track
		mid = MidiFile(file_path, clip = "True")  # redeclare for good measure

		for track in mid.tracks: #iterate through the tracks

			if track != 'MELODY': # if the track isnt called Melody
				mid.tracks.remove(track) # ANNIHALATE TRACK

		mid.tracks.remove(mid.tracks[1]) # ANNIHALATE extra track thats blank (data is kinda crazy)
		mid.save(file_path) # replacec original 

	else:
		print('skip') # if there is only one track then skip
