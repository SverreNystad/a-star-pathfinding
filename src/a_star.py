from src.Map import Map_Obj

class Frontier:
    """
    The frontier is a priority queue of nodes. The nodes are sorted by it cost.
    """
    def __init__(self, start_pos: list[int, int],  map_obj: "Map_Obj"):
        """ Instantiate a frontier object. """
        self.frontier = [start_pos]
        self._map = map_obj

    def get_frontier(self) -> list[int, int]:
        """ Getter for the frontier """
        return self.frontier
    
    def insert(self, node: list[int, int]):
        """
        Inserts a node into the frontier. The node is inserted in the
        correct position based on its cost.
        """
        self.frontier.append(node)
        self.frontier.sort(reverse=True, key=lambda node: self._map.get_cell_value(node))

    def pop(self):
        """
        Finds the node with the lowest cost in the frontier and returns it.
        As the frontier is sorted, the node with the lowest cost is the last
        """
        return self.frontier.pop()
    
    def is_empty(self):
        """ Checks if the frontier is empty """
        return len(self.frontier) == 0
    

def a_star(map: "Map_Obj", start_pos: list[int, int]=None, goal_pos: list[int, int]=None):
    """
    A* algorithm implementation
    """
    
    # Set start and goal positions if they are given or use the ones from the map
    if start_pos is not None:
        map.set_start_pos(start_pos)
    if goal_pos is not None:
        map.set_goal_pos(goal_pos)

    start_pos = map.get_start_pos()
    goal_pos = map.get_goal_pos()

def reconstruct_path(came_from: dict, current: list[int, int]) -> list[list[int, int]]:
    """
    Reconstructs the path from the start to the goal node

    Parameters
    ----------
    came_from : dict
        Dictionary with the path from the start to the goal node
    current : list[int, int]
        The goal node

    Returns
    -------
    list[list[int, int]]
        The path from the start to the goal node
    """
    total_path = [current]
    # Need to find the parent of the value in the dictionary
    while True:
        parent = _get_key_from_value(current, came_from)
        # There must be a parent and the path must not be a loop
        if parent is None or parent == current:
            break
        current = parent
        total_path.append(parent)
        
    
    # Reverse the path so that it starts from the start node
    total_path.reverse()
    return total_path

def _get_key_from_value(value: list[int, int], dictionary: dict) -> list[int, int]:
    """
    Returns the key of a dictionary based on the value
    """
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def a_star_heuristic(current_pos: list[int, int], goal_pos: list[int, int]) -> float:
    """
    A heuristic function for A*. Calculates the manhattan distance

    Parameters
    ----------
    pos : list[int, int]
        Position for which we want to calculate the heuristic

    Returns
    -------
    float
        Heuristic value for `pos`
    """
    # Calculate the heuristic value for the given position
    # Manhatten distance = |x1 - x2| + |y1 - y2|
    x_distance = abs(current_pos[0] - goal_pos[0])
    y_distance = abs(current_pos[1] - goal_pos[1])
    return x_distance + y_distance
    