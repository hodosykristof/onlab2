import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def convert_list_to_number(data):
    result = []
    for i in range(0, len(data)):
        result.append(float(data[i]))

    return result


def plot_3d(x, y, time):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    pos_xs_float = convert_list_to_number(x)
    pos_ys_float = convert_list_to_number(y)
    times_float = convert_list_to_number(time)

    ax.scatter(pos_xs_float, pos_ys_float, times_float, c='r')
    ax.plot(pos_xs_float, pos_ys_float, times_float, c='r')

    ax.set_xlabel('X position')
    ax.set_ylabel('Y position')
    ax.set_zlabel('Time')

    plt.show()


def interpolate(x, y, type):
    x_float = convert_list_to_number(x)
    y_float = convert_list_to_number(y)

    x_sample = x_float[0:42]
    y_sample = y_float[0:42]
    x_sorted = sorted(x_sample)
    y_sorted = sorted(y_sample)

    if type == "linear":
        f = interp1d(x_float, y_float)
    elif type == "cubic":
        f = interp1d(x_sorted, y_sample, kind='cubic')

    plt.plot(x_sorted, y_sample, 'o', x_sorted, f(x_sorted), '-')
    plt.show()
    return
