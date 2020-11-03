#felkerültem GitHubra juhú

import glob
import json

import numpy as np

from functools import reduce
from operator import add

from json_extract import json_extract
from time_calc import increase_time_by_seconds
from som import create_som


ball_pos_xs = []
ball_pos_ys = []
ball_tss = []
ball_video_seconds = []
ball_timestamps = []
data = []

for filepath in glob.iglob('Fitness_InStat_fajlok/fitness_1175403.json'):
# for filepath in glob.iglob('Fitness_InStat_fajlok/*.json'):
    with open(filepath) as json_file:
        data = json.load(json_file)
    ball_pos_xs.append(json_extract(data, 'pos_x', 'ball'))
    ball_pos_ys.append(json_extract(data, 'pos_y', 'ball'))
    ball_tss.append(json_extract(data, 'ts', 'ball'))
    ball_video_seconds.append(json_extract(data, 'video_second', 'ball'))

for i in range(0, len(ball_tss[0])):
    ball_timestamps.append(increase_time_by_seconds(ball_tss[0][i], ball_video_seconds[0][i]))

print(ball_pos_xs)
print(ball_pos_ys)
print(ball_timestamps)

pos_xs = reduce(add, ball_pos_xs)
pos_ys = reduce(add, ball_pos_ys)
timestamps = reduce(add, ball_timestamps)

input_neurons = np.column_stack((pos_xs, pos_ys))

# times = json_extract(data, 'video_second')
# print(times)

# plot_3d(pos_xs, pos_ys, times)
# interpolate(pos_xs, pos_ys, "cubic")

# create_som(input_neurons)
