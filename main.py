import copy
import glob
import itertools
import json

import numpy as np

from functools import reduce
from operator import add

from data_processing import ball_filter, ball_filter2, ball_player, player_splitter, second_counter, \
    constellation_finder, indices_filter, constellation_constructor
from filehandling import write_to_file
from json_extract import json_extract, json_extract_all
from time_calc import increase_time_by_seconds
from timestamp_finder import timestamp_finder
from som import create_som, som_clustering, create_winners, find_neuron_constellations


# pos_xs = []
# pos_ys = []
# tss = []
# video_seconds = []
# marker_seconds = []
# timestamps = []
# halfs = []
# distances = []
# data = []

# extract data from input files
# for filepath in glob.iglob('Fitness_InStat_fajlok/fitness_1175413.json'):
# # for filepath in glob.iglob('Fitness_InStat_fajlok/*.json'):
#     with open(filepath) as json_file:
#         data = json.load(json_file)
#     pos_xs.append(json_extract(data, 'pos_x'))
#     pos_ys.append(json_extract(data, 'pos_y'))
#     halfs.append(json_extract(data, 'half'))
#     # tss.append(json_extract(data, 'ts'))
#     video_seconds.append(json_extract(data, 'video_second'))
#     # marker_seconds.append(json_extract(data, 'second'))
#     distances.append(json_extract(data, 'distance'))

filepath = 'Fitness_InStat_fajlok/fitness_1175413.json'
with open(filepath) as json_file:
    data = json.load(json_file)
pos_xs, pos_ys, video_seconds, halfs = json_extract_all(data)

# creating lists from the data
# pos_xs = list(itertools.chain.from_iterable(pos_xs))
# pos_ys = list(itertools.chain.from_iterable(pos_ys))
# halfs = list(itertools.chain.from_iterable(halfs))
# tss = list(itertools.chain.from_iterable(tss))
# video_seconds = list(itertools.chain.from_iterable(video_seconds))
# marker_seconds = list(itertools.chain.from_iterable(marker_seconds))
# distances = list(itertools.chain.from_iterable(distances))

# if length of timestamps and second is not equal, select the length of the sorter for comparison
# less = min(len(tss), len(video_seconds))
# less = min(len(tss), len(marker_seconds))

# increase timestamps with seconds (probably useless :( )
# for i in range(0, less):
#     if tss[i][0] == '2':
#         # timestamps.append(increase_time_by_seconds(tss[i], video_seconds[i]))
#         timestamps.append(increase_time_by_seconds(tss[i], marker_seconds[i]))
#
#     else:
#         timestamps.append(tss[i])

pos_xs_ball, pos_xs_player = ball_player(pos_xs)
pos_ys_ball, pos_ys_player = ball_player(pos_ys)
video_seconds_ball, video_seconds_player = ball_player(video_seconds)
halfs_ball, halfs_player = ball_player(halfs)

pos_xs_ball, pos_ys_ball, halfs_ball, video_seconds_ball = ball_filter(pos_xs_ball, pos_ys_ball, halfs_ball, video_seconds_ball)

ball_filter2(pos_xs_ball, pos_ys_ball, video_seconds_ball, halfs_ball)

pos_xs_player = player_splitter(pos_xs_player)
pos_ys_player = player_splitter(pos_ys_player)
video_seconds_player = player_splitter(video_seconds_player)
halfs_player = player_splitter(halfs_player)

indices = constellation_finder(video_seconds_player, halfs_player, video_seconds_ball, halfs_ball)
# write_to_file("result/indices_new.txt", indices)

indices_filtered = copy.deepcopy(indices)
indices_filtered = indices_filter(indices_filtered, pos_xs_ball, pos_ys_ball)
# write_to_file("result/indices_filtered.txt", indices_filtered)

constellations = constellation_constructor(pos_xs_ball, pos_ys_ball, pos_xs_player, pos_ys_player, indices_filtered)

# types_1, types_2, indices_1, indices_2 = second_counter(halfs, video_seconds)

# export results to file
# write_to_file("result/tss.txt", tss)
# write_to_file("result/pos_xs.txt", pos_xs)
# write_to_file("result/pos_ys.txt", pos_ys)
# write_to_file("result/distances.txt", distances)
# write_to_file("result/halfs.txt", halfs)
# write_to_file("result/video_seconds.txt", video_seconds)
# write_to_file("result/timestamps.txt", timestamps)
# write_to_file("result/types1.txt", types_1)
# write_to_file("result/types2.txt", types_2)
# write_to_file("result/indices1.txt", indices_1)
# write_to_file("result/indices2.txt", indices_2)
#
# f = open("result/markers.txt", "a")
# for i in range(0, len(ts_types)):
#     if len(indices[i]) >= 23:
#         print("full constellation: " + str(ts_types[i]) + ' ' + str(indices[i]), file=f)
#     else:
#         print(str(ts_types[i]) + ' ' + str(indices[i]), file=f)
# f.close()

# get the types of timestamps and their indices, then print them
# ts_types, indices = timestamp_finder(timestamps)
#
# for i in range(0, len(ts_types)):
#     print(ts_types[i] + "" + str(indices[i]))

# print(pos_ys)
# print(timestamps)

# print(halfs)
# print(len(halfs))
# halfs = ball_filter(halfs)
# print(halfs)
# print(len(halfs))
#
# create a column vector from positional data
# pos_xs = reduce(add, pos_xs)
# pos_ys = reduce(add, pos_ys)
#
# input_neurons = np.column_stack((pos_xs, pos_ys))

# some debug stuff
# times = json_extract(data, 'video_second')
# print(times)

# plotting for interpolation
# plot_3d(pos_xs, pos_ys, times)
# interpolate(pos_xs, pos_ys, "cubic")

# create map structure
input_neurons = np.array(constellations)
som = create_som(input_neurons)
winners = create_winners(som, input_neurons)
# write_to_file("result/winners.txt", winners)

constellations_at_13_5 = find_neuron_constellations(winners, constellations, 13, 5)
constellations_at_10_0 = find_neuron_constellations(winners, constellations, 10, 0)
constellations_at_6_0 = find_neuron_constellations(winners, constellations, 6, 0)

write_to_file("result/constellations_at_13_5.txt", constellations_at_13_5)
write_to_file("result/constellations_at_10_0.txt", constellations_at_10_0)
write_to_file("result/constellations_at_6_0.txt", constellations_at_6_0)
