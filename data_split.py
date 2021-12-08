# Splits the data randomly into folders that are compatible with magenta conversion

import random
import shutil
import os
import sys

source = "./pop909_midi" # Source Folder for spliting data

files = os.listdir(source) #getting all file names in folder
random.shuffle(files) # randomly shuffling files 

os.mkdir("./pop909_midi_train") # Making all Dir
os.mkdir("./pop909_midi_val") # Making all Dir
os.mkdir("./pop909_midi_test") # Making all Dir

train = files[0:726] # 80 percent 
val = files[727:817] # 10 percent
test = files[818:907] # 10 percent

for i in range(0,len(train)):
	shutil.copy(os.path.join(source,train[i]), "./pop909_midi_train") # Copying to folder

for i in range(0,len(val)):
	shutil.copy(os.path.join(source,val[i]), "./pop909_midi_val") # Copying to folder

for i in range(0,len(test)):
	shutil.copy(os.path.join(source,test[i]), "./pop909_midi_test") # Copying to folder
