import glob
import json

from json_extract import json_extract
from time_calc import increase_time_by_seconds


events = []
eventarray = []
eventnums = []
team_names = []
tss = []
seconds = []
timestamps = []

for filepath in glob.iglob('Fitness_InStat_fajlok/markers_1175413.json'):
    with open(filepath) as json_file:
        data = json.load(json_file)
    events = json_extract(data, 'action_name')
    team_names = json_extract(data, 'team_name')
    tss = json_extract(data, 'ts')
    seconds = json_extract(data, 'second')

for i in range(0, len(tss)):
    if tss[i][0] == '2':
        timestamps.append(increase_time_by_seconds(tss[i], seconds[i]))

    else:
        timestamps.append(tss[i])

print(team_names)

for i in range(0, len(events)-1):
    if eventarray:
        j = 0
        for j in range(0, len(eventarray)):
            if eventarray[j] == events[i]:
                eventnums[j] += 1
                break
            if j == len(eventarray)-1:
                eventarray.append(events[i])
                eventnums.append(1)
    else:
        eventarray.append(events[i])
        eventnums.append(1)

for i in range(0, len(eventarray)-1):
    print(eventarray[i])
    print(eventnums[i])
