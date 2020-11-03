import matplotlib.pyplot as plt
import numpy as np

from minisom import MiniSom

from matplotlib.patches import RegularPolygon
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import cm, colorbar


def create_som(input_neurons):
    som = MiniSom(15, 15, input_neurons.shape[1], sigma=1.5, learning_rate=.7, activation_distance='euclidean',
                  topology='hexagonal', neighborhood_function='gaussian', random_seed=10)

    som.train(input_neurons, 1000, verbose=True)

    f = plt.figure(figsize=(10, 10))
    ax = f.add_subplot(111)

    ax.set_aspect('equal')

    xx, yy = som.get_euclidean_coordinates()
    umatrix = som.distance_map()
    weights = som.get_weights()

    for i in range(weights.shape[0]):
        for j in range(weights.shape[1]):
            wy = yy[(i, j)] * 2 / np.sqrt(3) * 3 / 4
            hex = RegularPolygon((xx[(i, j)], wy), numVertices=6, radius=.95 / np.sqrt(3),
                                 facecolor=cm.Blues(umatrix[i, j]), alpha=.4, edgecolor='gray')
            ax.add_patch(hex)

    markers = ['o', '+', 'x']
    colors = ['C0', 'C1', 'C2']
    for cnt, x in enumerate(input_neurons):
        w = som.winner(x)  # getting the winner
        # place a marker on the winning position for the sample xx
        wx, wy = som.convert_map_to_euclidean(w)
        wy = wy * 2 / np.sqrt(3) * 3 / 4
        plt.plot(wx, wy, markerfacecolor='None',
                 markersize=12, markeredgewidth=2)

    xrange = np.arange(weights.shape[0])
    yrange = np.arange(weights.shape[1])
    plt.xticks(xrange - .5, xrange)
    plt.yticks(yrange * 2 / np.sqrt(3) * 3 / 4, yrange)

    divider = make_axes_locatable(plt.gca())
    ax_cb = divider.new_horizontal(size="5%", pad=0.05)
    cb1 = colorbar.ColorbarBase(ax_cb, cmap=cm.Blues,
                                orientation='vertical', alpha=.4)
    cb1.ax.get_yaxis().labelpad = 16
    cb1.ax.set_ylabel('distance from neurons in the neighbourhood',
                      rotation=270, fontsize=16)
    plt.gcf().add_axes(ax_cb)

    # legend_elements = [Line2D([0], [0], marker='o', color='C0', label='Kama',
    #                           markerfacecolor='w', markersize=14, linestyle='None', markeredgewidth=2),
    #                    Line2D([0], [0], marker='+', color='C1', label='Rosa',
    #                           markerfacecolor='w', markersize=14, linestyle='None', markeredgewidth=2),
    #                    Line2D([0], [0], marker='x', color='C2', label='Canadian',
    #                           markerfacecolor='w', markersize=14, linestyle='None', markeredgewidth=2)]
    # ax.legend(handles=legend_elements, bbox_to_anchor=(0.1, 1.08), loc='upper left',
    #           borderaxespad=0., ncol=3, fontsize=14)

    plt.savefig('som_seed_hex.png')
    plt.show()