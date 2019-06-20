import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable


map = []
N = 20
start = np.array([18, 1])
goal = np.array([1, 18])

def plotData():
    global map

    fig = plt.figure(dpi=500)
    # fig.tight_layout()

    gs = gridspec.GridSpec(1, 1)

    # =======
    # Map
    # =======

    ax = fig.add_subplot(gs[0])

    ax.matshow(map, vmin=0, vmax=1, cmap='Greys')

    plt.title('Map', x=0.5, y=1.2)

    ticks = np.arange(0, N, 1)

    plt.grid(which='major', axis='both', linestyle=':', color='black')

    for i in range(len(map)):
        for j in range(len(map)):
            if start[0] == i and start[1] == j:
                ax.text(j, i, "S", ha="center", va="center", color="red", weight='bold')

            if goal[0] == i and goal[1] == j:
                ax.text(j, i, "Z", ha="center", va="center", color="green", weight='bold')

    ax.set_xticks(ticks)
    ax.set_yticks(ticks)

    ax.set_xticklabels(range(0, N))
    ax.set_yticklabels(range(0, N))

    # =======
    # Path
    # =======

    plt.show()

def main():
    global map

    map = np.empty((N, N))
    map[:] = 0

    map[13, 0] = 1
    map[13, 1] = 1
    map[2, 2] = 1
    map[8, 2] = 1
    map[13, 2] = 1
    map[2, 3] = 1
    map[8, 3] = 1
    map[13, 3] = 1
    map[16, 3] = 1
    map[17, 3] = 1
    map[18, 3] = 1
    map[19, 3] = 1
    map[2, 4] = 1
    map[8, 4] = 1
    map[2, 5] = 1
    map[4, 5] = 1
    map[5, 5] = 1
    map[8, 5] = 1
    map[2, 6] = 1
    map[8, 6] = 1
    map[2, 7] = 1
    map[8, 7] = 1
    map[2, 8] = 1
    map[8, 8] = 1
    map[7, 9] = 1
    map[8, 9] = 1
    map[9, 9] = 1
    map[10, 9] = 1
    map[15, 9] = 1
    map[15, 10] = 1
    map[5, 11] = 1
    map[15, 11] = 1
    map[0, 12] = 1
    map[1, 12] = 1
    map[2, 12] = 1
    map[3, 12] = 1
    map[5, 12] = 1
    map[8, 12] = 1
    map[12, 12] = 1
    map[13, 12] = 1
    map[14, 12] = 1
    map[15, 12] = 1
    map[8, 13] = 1
    map[8, 14] = 1
    map[4, 15] = 1
    map[6, 15] = 1
    map[7, 15] = 1
    map[8, 15] = 1
    map[16, 15] = 1
    map[17, 15] = 1
    map[18, 15] = 1
    map[19, 15] = 1
    map[4, 16] = 1
    map[8, 16] = 1
    map[4, 17] = 1
    map[8, 17] = 1
    map[4, 18] = 1
    map[5, 18] = 1
    map[6, 18] = 1
    map[8, 18] = 1
    map[4, 19] = 1

    plotData()

    print("hallo")


if __name__ == "__main__":
    main()