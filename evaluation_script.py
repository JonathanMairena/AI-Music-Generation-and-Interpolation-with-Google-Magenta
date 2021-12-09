from mido import MidiFile
import pretty_midi
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import math
source = '/Users/jonathanmairena/Documents/Fall2021/CIS519/Project/Pretrained Results -interp/Pretrained_results_902_907'
files = os.listdir(source) 
global_tempo = []
velocity = [] 
key = []
tempo_list = []
num_changes = []
beat_range = []
beat_ratio = []

for i in range(0,len(files)):
	midi_file_name = os.path.join(source,files[i])
	# Store an empirical estimate of its global tempo
	midi_data = pretty_midi.PrettyMIDI(midi_file_name)
	# print ('Global Tempo \t',midi_data.estimate_tempo())
	# print (midi_data.estimate_tempo())
	global_tempo.append(midi_data.estimate_tempo())

	# Compute the relative amount of each semitone across the entire song,
	# a proxy for key
	total_velocity = sum(sum(midi_data.get_chroma()))
	velocity.append(total_velocity)
	# print('Total Velocity \t',total_velocity)
	# print(total_velocity)

	#relative amount of semitone accross entire song
	rel_pitches = [sum(semitone)/total_velocity for semitone in midi_data.get_chroma()]
	pitch_names = ['Do', 'Di', 'Re', 'Ri', 'Mi', 'Fa', 'Fi', 'Sol', 'Si', 'La', 'Li', 'Ti']
	key.append(np.argmax(rel_pitches))
	# plt.bar(pitch_names,rel_pitches)
	# plt.title('Relative presence of pitch in song ')
	# plt.savefig('Pitch_bar_plot')

	#compute the amount of times the tempo changes
	[time,tempo] = midi_data.get_tempo_changes()
	# print('Tempo Changes \t',len(time))
	# print('Tempo \t',tempo)
	# print(len(time))
	# print(tempo)
	tempo_list.append(tempo)
	num_changes.append(len(time))
	#get_pitch_class_histogram
	# plt.figure()
	# plt.bar(pitch_names,midi_data.get_pitch_class_histogram(use_duration=False, use_velocity=True, normalize=True))
	# plt.title('Pitch Histogram Weighed by Velocity')
	# plt.savefig('pitch_histogram')

	#transition matrix
	# print(midi_data.get_pitch_class_transition_matrix(normalize=False, time_thresh=0.05))

	#Get number of beats
	beats = midi_data.get_beats()
	# print('Number of Beats \t',len(beats))
	# print('Range of Beats \t', beats[np.argmax(beats)] - beats[np.argmin(beats)])
	beat_range.append(beats[np.argmax(beats)] - beats[np.argmin(beats)])
	# print(len(beats))
	# print(beats[np.argmax(beats)] - beats[np.argmin(beats)])

	#Get number of off beats
	down_beats = midi_data.get_downbeats()
	beat_ratio.append(len(beats)/len(down_beats))
	# print('Number of Down Beats \t', len(down_beats))
	# print(len(down_beats))
pitch_names = ['Do', 'Di', 'Re', 'Ri', 'Mi', 'Fa', 'Fi', 'Sol', 'Si', 'La', 'Li', 'Ti']
print(np.mean(global_tempo))
print(np.mean(velocity))
print(np.mean(tempo_list))
print(np.mean(num_changes))
print(np.mean(beat_range))
print(np.mean(beat_ratio))
print(pitch_names[math.floor(np.mean(key))])