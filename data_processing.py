# throws away unnecessary parts of halves data, returns index of last valid element
def ball_filter(pos_xs, pos_ys, halfs, seconds):
    for i in range(1, len(halfs)):
        if halfs[i] == 2 and halfs[i - 1] == 1:
            halfs = halfs[:i]
            pos_xs = pos_xs[:i]
            pos_ys = pos_ys[:i]
            seconds = seconds[:i]
            break

    return pos_xs, pos_ys, halfs, seconds


def ball_player(data):
    ball = []
    players = []

    for i in range(1, len(data)):
        if data[i] == 'players:':
            ball = data[:i]
            players = data[i + 1:]
            break

    return ball, players


def player_splitter(data):
    result = []
    index = 0

    for i in range(0, len(data) - 1):
        if isinstance(data[i], str):
            if all(x.isalpha() or x.isspace() for x in data[i]):
                result.append(data[index:i])
                index = i

    return result


def type_checker(types, indices, i, seconds):
    j = 0

    for j in range(0, len(types)):
        if types[j] == seconds[i]:
            indices[j].append(i)
            j = -1
            break
    if j != -1:
        types.append(seconds[i])
        indices.append([])
        indices[len(types) - 1].append(i)


def second_counter(halves, seconds):
    types_1 = []
    types_2 = []
    indices_1 = [[]]
    indices_2 = [[]]

    # if halves[1] == '1':
    #     types_1.append(seconds[1])
    #     indices_1.append([])
    #     indices_1[1].append(1)

    for i in range(1, len(seconds)):
        if halves[i] == '1':
            if not any(types_1):
                types_1.append(seconds[0])
                indices_1[0].append(0)
            else:
                type_checker(types_1, indices_1, i, seconds)

        elif halves[i] == '2':
            if not any(types_2):
                types_2.append(seconds[0])
                indices_2[0].append(0)
            else:
                type_checker(types_2, indices_2, i, seconds)

    return types_1, types_2, indices_1, indices_2


def ball_filter2(pos_xs, pos_ys, seconds, halfs):
    length = len(seconds)
    i = 1

    while i < length:
        if seconds[i] == seconds[i - 1]:
            del pos_xs[i]
            del pos_ys[i]
            del seconds[i]
            del halfs[i]
            i -= 1
            length -= 1

        i += 1


def constellation_finder(seconds, halfs, seconds_ref, halfs_ref):
    indices = [[]]
    k = 0

    for i in range(0, len(seconds_ref)):
        indices.append([])
        for j in range(1, len(seconds)):
            for k in range(0, len(seconds[j])):
                if seconds[j][k] == seconds_ref[i]:
                    if halfs[j][k] == halfs_ref[i]:
                        indices[i].append(k)
                        k = -1
                        break

            if k != -1:
                indices[i].append(-1)

    del indices[len(indices)-1]
    return indices


def indices_filter(indices, pos_xs_ball, pos_ys_ball):
    length = len(indices)
    i = 0
    while i < length:
        invalid = 0
        for j in range(0, len(indices[i])):
            if indices[i][j] == -1:
                invalid += 1

        if len(indices[i]) - invalid < 21:
            del indices[i]
            del pos_xs_ball[i]
            del pos_ys_ball[i]
            i -= 1
            length -= 1

        i += 1

    return indices


def constellation_constructor(pos_xs_ball, pos_ys_ball, pos_xs_player, pos_ys_player, indices):
    constellations = [[]]

    for i in range(0, len(indices)):
        constellations.append([])
        constellations[i].append(pos_xs_ball[i])
        constellations[i].append(pos_ys_ball[i])
        for j in range(0, len(indices[i])):
            if indices[i][j] == -1:
                constellations[i].append(-100)
                constellations[i].append(-100)
            else:
                constellations[i].append(pos_xs_player[j+1][indices[i][j]])
                constellations[i].append(pos_ys_player[j+1][indices[i][j]])

    del constellations[-1]
    return constellations

