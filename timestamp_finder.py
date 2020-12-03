def timestamp_finder(tss):
    ts_types = []
    indices = [[]]

    ts_types.append(tss[0])
    indices[0].append(0)

    for i in range(1, len(tss)):
        j = 0
        for j in range(0, len(ts_types)):
            if ts_types[j] == tss[i]:
                indices[j].append(i)
                break
            if j == len(ts_types) - 1:
                ts_types.append(tss[i])
                indices.append([])
                indices[len(ts_types) - 1].append(i)

    return ts_types, indices
