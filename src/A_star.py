class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end, empire2, empire3, stance):
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
        if len(closed_list) > 20:
            return None

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
        if current_node.position[1] % 2 == 0:
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (1, -1), (1, 1)]: # Adjacent squares
                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                # Make sure within range
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                        len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                    continue
                # Make sure walkable terrain
                if maze[node_position[0]][node_position[1]] == 'w' or maze[node_position[0]][node_position[1]] == 'm':
                    continue

                if stance == None and (maze[node_position[0]][node_position[1]] == empire2.name[0] or maze[node_position[0]][node_position[1]] == empire3.name[0]):
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
                        # H: Manhattan distance to end point
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
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1)]: # Adjacent squares
                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                # Make sure within range
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue
                # Make sure walkable terrain
                if maze[node_position[0]][node_position[1]] == 'w' or maze[node_position[0]][node_position[1]] == 'm' :
                    continue

                if stance == None and (maze[node_position[0]][node_position[1]] == empire2.name[0] or maze[node_position[0]][node_position[1]] == empire3.name[0]):
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
                        # H: Manhattan distance to end point
                        child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
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