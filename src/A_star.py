"""
Module A_star.py
============

This module contains Pathfinding A-STAR ALGORITHM FOR AI
"""

__version__ = '1.0'
__author__ = 'Edan Gurin'


class Node():
    """
    Class Method :
        A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        """
        Initialize self
        :param parent - parent:
        :param position - node position:
        """
        self.parent = parent
        self.position = position

        self.g = 0  # g(n) — this represents the exact cost of the path from the starting node to any node n
        self.h = 0  # h(n) — this represents the heuristic estimated cost from node n to the goal node.
        self.f = 0  # f(n) — lowest cost in the neighboring node n

    def __eq__(self, other):
        return self.position == other.position


"""
ABOUT A* : 
A-star (also referred to as A*) is one of the most successful search algorithms to find the shortest path between 
nodes or graphs. It is an informed search algorithm, as it uses information about path cost and also uses heuristics 
to find the solution.

To understand how A* works, first we need to understand a few terminologies:

1. Node — All potential position or stops with a unique identification
2. Starting Node — Whereto start searching
3. Goal Node — The target to stop searching.
4. Search Space — A collection of nodes, like all board positions of a board game
5. Cost — Numerical value (say distance, time, or financial expense) for the path from a node to another node.
    g(n) — this represents the exact cost of the path from the starting node to any node n
    h(n) — this represents the heuristic estimated cost from node n to the goal node.
    f(n) — lowest cost in the neighboring node n

Each time A* enters a node, it calculates the cost, f(n) (n being the neighboring node), to travel to all of the neighboring 
nodes, and then enters the node with the lowest value of f(n).
These values we calculate using the following formula:
f(n) = g(n) + h(n) 
"""


def astar(maze, board, start, end, empire2, empire3, stance, type):
    """Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze: - board with terrain values
    :param board - board with empire locations:
    :param start - start coordinate:
    :param end - end coordinate:
    :param empire2 - empire2 rival empire:
    :param empire3 - empire2 rival empire:
    :param stance - stance of minimaxed empire - boolean (war / not war):
    :param type - determines which traverses the maze - land / sea unit:
    :return:
    """
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

        # block too long paths to reduce run time
        if type == 'land' and len(closed_list) > 20:
            return None

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        # division based on hex grid
        if current_node.position[1] % 2 == 0:
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (1, -1), (1, 1)]:  # Adjacent squares
                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                # Make sure within range
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                        len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                    continue
                # Make sure walkable terrain
                if type == 'land': # if the unit is land unit
                    if maze[node_position[0]][node_position[1]] == 'w' or maze[node_position[0]][
                        node_position[1]] == 'm':
                        continue
                    # if rival empire territory
                    if (stance is None or stance is False) and (
                            board[node_position[0]][node_position[1]] == empire2.name[0] or board[node_position[0]][
                        node_position[1]] == empire3.name[0]):
                        continue

                elif type == 'sea': # if unit is sea unit
                    if maze[node_position[0]][node_position[1]] == 'g' or maze[node_position[0]][
                        node_position[1]] == 'd' or maze[node_position[0]][node_position[1]] == 'c' or \
                            maze[node_position[0]][node_position[1]] == 'm':
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
                            break
                    else:
                        # Create the f, g, and h values
                        child.g = current_node.g + 1
                        # H: distance to end point
                        child.h = abs(child.position[0] - end_node.position[0]) + abs(
                            child.position[1] - end_node.position[1])
                        child.f = child.g + child.h

                        # Child is already in the open list
                        for open_node in open_list:
                            # check if the new path to children is worst or equal
                            # than one already in the open_list (by measuring g)
                            if child == open_node and child.g >= open_node.g:
                                break
                        else:
                            # Add the child to the open list
                            open_list.append(child)

        else:
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1)]:  # Adjacent squares
                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                # Make sure within range
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                        len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                    continue
                # Make sure walkable terrain
                if type == 'land':
                    if maze[node_position[0]][node_position[1]] == 'w' or maze[node_position[0]][
                        node_position[1]] == 'm':
                        continue

                    if (stance is None or stance is False) and (
                            board[node_position[0]][node_position[1]] == empire2.name[0] or board[node_position[0]][
                        node_position[1]] == empire3.name[0]):
                        continue

                elif type == 'sea':
                    if maze[node_position[0]][node_position[1]] == 'g' or maze[node_position[0]][
                        node_position[1]] == 'd' or maze[node_position[0]][node_position[1]] == 'c' or \
                            maze[node_position[0]][node_position[1]] == 'm':
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
                            break
                    else:
                        # Create the f, g, and h values
                        child.g = current_node.g + 1
                        # H: distance to end point
                        child.h = abs(child.position[0] - end_node.position[0]) + abs(
                            child.position[1] - end_node.position[1])
                        child.f = child.g + child.h

                        # Child is already in the open list
                        for open_node in open_list:
                            # check if the new path to children is worst or equal
                            # than one already in the open_list (by measuring g)
                            if child == open_node and child.g >= open_node.g:
                                break
                        else:
                            # Add the child to the open list
                            open_list.append(child)
