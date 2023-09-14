from src.Map import Map_Obj

class Frontier:
    """
    The frontier is a priority queue of nodes. The nodes are sorted by it cost.
    """
    def __init__(self, start_pos: list[int, int], goal_pos: list[int, int]):
        """ Instantiate a frontier object. """
        self.frontier = [start_pos]
        self.goal_pos = goal_pos

    def get_frontier(self) -> list[int, int]:
        """ Getter for the frontier """
        return self.frontier
    
    def insert(self, node: list[int, int]):
        """
        Inserts a node into the frontier. The node is inserted in the
        correct position based on its cost.
        """
        self.frontier.append(node)
        self.frontier.sort(reverse=True, key=lambda node: a_star_heuristic(node, self.goal_pos))

    def pop(self):
        """
        Finds the node with the lowest cost in the frontier and returns it.
        As the frontier is sorted, the node with the lowest cost is the last
        """
        return self.frontier.pop()
    
    def is_empty(self):
        """ Checks if the frontier is empty """
        return len(self.frontier) == 0
    

def a_star(map: Map_Obj, start_pos: list[int, int]=None, goal_pos: list[int, int]=None):
    """
    A* algorithm implementation

    Returns:
        The path from the start to the goal node or None if no path exists
    """
    
    # Set start and goal positions if they are given or use the ones from the map
    if start_pos is not None:
        map.set_start_pos(start_pos)
    if goal_pos is not None:
        map.set_goal_pos(goal_pos)

    start_pos = map.get_start_pos()
    goal_pos = map.get_goal_pos()

    # Initialize the frontier with the start position
    frontier = Frontier(start_pos, goal_pos)
    # Initialize the came_from dictionary
    # For node n, came_from[n] is the node immediately preceding it on the cheapest path from the start to n currently known.

    came_from = {}
    # Initialize the cost_to_reach_position dictionary, the first node has no cost
    # The sentinel value is not infinity but rather None, So all values not explicitly set are None
    cost_to_reach_position = {}
    cost_to_reach_position[tuple(start_pos)] = 0

    estimated_remaining_distance = {}
    estimated_remaining_distance[tuple(start_pos)] = a_star_heuristic(start_pos, goal_pos)

    while not frontier.is_empty():
        # Get the node with the lowest estimated distance from goal_pos from the frontier
        # And remove it from the frontier
        current = frontier.pop()
        if current == goal_pos:
            return reconstruct_path(came_from, tuple(current))

        for neighbor in map.get_neighbors(current):
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_cost_to_reach is the distance from start to the neighbor through current
            tentative_cost_to_reach = cost_to_reach_position[tuple(current)] + map.get_cell_value(neighbor)
            current_cost = cost_to_reach_position.get(tuple(neighbor))
            
            if current_cost is None or tentative_cost_to_reach < current_cost:
                # This path to neighbor is better than any previous one. Record it!
                
                came_from[tuple(neighbor)] = tuple(current)
                cost_to_reach_position[tuple(neighbor)] = tentative_cost_to_reach
                estimated_remaining_distance[tuple(neighbor)] = tentative_cost_to_reach + a_star_heuristic(neighbor, goal_pos)
                if neighbor not in frontier.get_frontier():
                    frontier.insert(neighbor)
    return None
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
    while current in came_from.keys():
        # Stop if there is a cycle in the path
        if current == came_from[current]:
            break
        current = came_from[current]
        total_path.append(current)
    return total_path


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
    