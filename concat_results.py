from mido import MidiFile
import os
import sys

source = "./Results" # Within Interpolated Results
files = os.listdir(source) # 
mid = []
for i in range(0,len(files)):
	file_path = os.path.join(source,files[i])
	print(file_path)
	mid.append(MidiFile(file_path, clip = "True"))  # append files together as a midi


merged_mid = MidiFile() # make a new mid that has all of the new files merged
merged_mid.ticks_per_beat=mid[0].ticks_per_beat
merged_mid.tracks = mid[0].tracks + mid[1].tracks  + mid[2].tracks  + mid[3].tracks  + mid[4].tracks
merged_mid.save('merged.mid') # save with new name