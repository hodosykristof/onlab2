import glob
import json

from json_extract import json_extract


events = []
eventarray = []
eventnums = []

for filepath in glob.iglob('Fitness_InStat_fajlok/markers_1175413.json'):
    with open(filepath) as json_file:
        data = json.load(json_file)
    events.append(json_extract(data, 'action_name'))

print(events)

for i in range(0, len(events[0])-1):
    if eventarray:
        j = 0
        for j in range(0, len(eventarray)):
            if eventarray[j] == events[0][i]:
                eventnums[j] += 1
                break
            if j == len(eventarray)-1:
                eventarray.append(events[0][i])
                eventnums.append(1)
    else:
        eventarray.append(events[0][i])
        eventnums.append(1)

for i in range(0, len(eventarray)-1):
    print(eventarray[i])
    print(eventnums[i])
