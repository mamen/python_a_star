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

N = 20


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.f = 0
        self.g = 0
        self.h = 0

    def __lt__(self, other):
        if self.f < other.f:
            return self
        else:
            return other


# H(n)
def getDistanceToGoal(node, goal):
    return (goal[0] - node[0]) ** 2 + (goal[1] - node[1]) ** 2


def getPath(endNode):
    path = []
    currentNode = endNode

    # reconstruct the path from goal to start
    while currentNode is not None:
        path.append(currentNode.position)
        currentNode = currentNode.parent

    return path[::-1]


def generateChildrenForNode(currentNode, maze):
    children = []

    for possiblePosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

        position = (currentNode.position[0] + possiblePosition[0], currentNode.position[1] + possiblePosition[1])

        # Out of bounds?
        if position[0] < 0 or position[0] > (N - 1) or \
                position[1] < 0 or position[1] > (N - 1):
            continue

        # Check for walls
        if maze[position[1]][position[0]] != 0:
            continue

        children.append(Node(currentNode, position))

    return children


def calculatePath(maze, startPosition, goalPosition):

    # Initialisation
    nodeStart = Node(None, startPosition)
    nodeEnd = Node(None, goalPosition)

    openNodes = [nodeStart]
    closedNodes = []

    while len(openNodes) > 0:

        currentNode = openNodes[0]
        currentNodeIndex = 0

        # get open node with lowest costs
        for index, item in enumerate(openNodes):
            if item.f < currentNode.f:
                currentNode = item
                currentNodeIndex = index

        openNodes.pop(currentNodeIndex)
        closedNodes.append(currentNode)

        # goal reached?
        if currentNode.position == nodeEnd.position:
            return getPath(currentNode), currentNode.f

        children = generateChildrenForNode(currentNode, maze)

        for child in children:

            skip = False

            # Skip children which are already on the closed list
            for node in closedNodes:
                if child.position == node.position:
                    skip = True
                    break

            if skip:
                continue

            costs = 1

            if isDiagonalChild(currentNode.position, child.position):
                costs = np.sqrt(2)

            child.g = currentNode.g + costs
            child.h = getDistanceToGoal(child.position, nodeEnd.position)
            child.f = child.g + child.h

            skip = False

            # Skip children which are already on the open list
            for node in openNodes:
                if child.position == node.position and child.g > node.g:
                    skip = True
                    break

            if skip:
                continue

            openNodes.append(child)


    return -1, -1

def isDiagonalChild(parentPos, childPos):

    # top-left
    if (parentPos[0] - 1 == childPos[0] and parentPos[1] - 1 == childPos[1]):
        return True

    # top-right
    if (parentPos[0] - 1 == childPos[0] and parentPos[1] + 1 == childPos[1]):
        return True

    # bottom-right
    if (parentPos[0] + 1 == childPos[0] and parentPos[1] + 1 == childPos[1]):
        return True

    # bottom-left
    if (parentPos[0] + 1 == childPos[0] and parentPos[1] - 1 == childPos[1]):
        return True

    return False


def plotData(board, path):

    fig = plt.figure(dpi=500)
    # fig.tight_layout()

    gs = gridspec.GridSpec(1, 1)

    # =======
    # Map
    # =======

    ax = fig.add_subplot(gs[0])

    ax.matshow(board, vmin=0, vmax=1, cmap='Greys')

    plt.title('Map', x=0.5, y=1.2)

    ticks = np.arange(0, N, 1)

    plt.grid(which='major', axis='both', linestyle=':', color='black')

    for i in range(len(board)):
        for j in range(len(board)):
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

    board = np.empty((N, N))
    board[:] = 0

    board[13, 0] = 1
    board[13, 1] = 1
    board[2, 2] = 1
    board[8, 2] = 1
    board[13, 2] = 1
    board[2, 3] = 1
    board[8, 3] = 1
    board[13, 3] = 1
    board[16, 3] = 1
    board[17, 3] = 1
    board[18, 3] = 1
    board[19, 3] = 1
    board[2, 4] = 1
    board[8, 4] = 1
    board[2, 5] = 1
    board[4, 5] = 1
    board[5, 5] = 1
    board[8, 5] = 1
    board[2, 6] = 1
    board[8, 6] = 1
    board[2, 7] = 1
    board[8, 7] = 1
    board[2, 8] = 1
    board[8, 8] = 1
    board[7, 9] = 1
    board[8, 9] = 1
    board[9, 9] = 1
    board[10, 9] = 1
    board[15, 9] = 1
    board[15, 10] = 1
    board[5, 11] = 1
    board[15, 11] = 1
    board[0, 12] = 1
    board[1, 12] = 1
    board[2, 12] = 1
    board[3, 12] = 1
    board[5, 12] = 1
    board[8, 12] = 1
    board[12, 12] = 1
    board[13, 12] = 1
    board[14, 12] = 1
    board[15, 12] = 1
    board[8, 13] = 1
    board[8, 14] = 1
    board[4, 15] = 1
    board[6, 15] = 1
    board[7, 15] = 1
    board[8, 15] = 1
    board[16, 15] = 1
    board[17, 15] = 1
    board[18, 15] = 1
    board[19, 15] = 1
    board[4, 16] = 1
    board[8, 16] = 1
    board[4, 17] = 1
    board[8, 17] = 1
    board[4, 18] = 1
    board[5, 18] = 1
    board[6, 18] = 1
    board[8, 18] = 1
    board[4, 19] = 1



    # # obstacles to complete block goal:
    # board[4, 12] = 1
    # board[4, 13] = 1
    # board[4, 14] = 1

    path, costs = calculatePath(board, (1, 18), (18, 1))

    if path == -1 and costs == -1:
        print("No path found")
    else:
        print("Found a path with costs of ", costs)
        print("Path: ")
        print(path)
        plotData(board, path)


if __name__ == "__main__":
    main()
