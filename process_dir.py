#Creates a new folder with just midi data from 
#Pop909 that is compatible with magenta conversion
import os
import sys
import glob
import shutil
import numpy as np


#Extracting path names to all midi files
path = "./POP909" # Main Data Path
folder_names = ["/%03d" % i for i in range(1,909)] #Creates list of folder names
new_path = "./pop909_midi_train" # new path for data
names_list = []

for name in folder_names:
	midi_file_name = glob.glob(path + name +"/*.mid", recursive = True) #finding path in folder
	for a in midi_file_name:
		shutil.copy(a,new_path) # copying to new folder


#Checking if they are the correct path names 
print(len(folder_names))
print(folder_names[0])


#Creating a a directory with only the midi files in text_files ONLY ONCE
# os.mkdir(new_path)

