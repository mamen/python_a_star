import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from heapq import *

# F = G * H
# F = total cost
# G = distance between current and start
# H = distance between current and goal

# horizontal/vertical: 1
# diagonal: sqrt(2)

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


# h(n)
def getDistance(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2




def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)




map = []
N = 20

def plotData(path):
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
            if 18 == i and 1 == j:
                ax.text(j, i, "S", ha="center", va="center", color="red", weight='bold')

            if 1 == i and 18 == j:
                ax.text(j, i, "Z", ha="center", va="center", color="green", weight='bold')

    ax.set_xticks(ticks)
    ax.set_yticks(ticks)

    ax.set_xticklabels(range(0, N))
    ax.set_yticklabels(range(0, N))

    X = [i[0] for i in path]
    Y = [i[1] for i in path]

    plt.plot(X, Y, '-o', markersize=1.5, linewidth=1, color="gray")

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

    path = astar(map, (18, 1), (1, 18))

    print(path)

    plotData(path)



if __name__ == "__main__":
    main()