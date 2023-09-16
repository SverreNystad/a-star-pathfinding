""" Creates a visualization of the exploration of the environment. """
from PIL import Image, ImageDraw
from copy import deepcopy

from src.Map import Map
from src.a_star import Frontier, a_star_heuristic, reconstruct_path

def a_star_with_visualization(map: Map, start_pos: list[int, int]=None, goal_pos: list[int, int]=None):
    """
    A* algorithm implementation

    Args:
        map (Map): The map on which the algorithm is run
        start_pos (list[int, int], optional): The start position. Defaults to None.
        goal_pos (list[int, int], optional): The goal position. Defaults to None.
    Returns:
        The path from the start to the goal node or None if no path exists
    """
    frames = []
    # Visualization
    closed_set = set()
    open_set = set()

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
        closed_set.add(tuple(current))
        
        for neighbor in map.get_neighbors(current):
            # Calculate the cost to reach the neighbor through current
            # tentative_cost_to_reach is the distance from start to the neighbor through current
            tentative_cost_to_reach = cost_to_reach_position[tuple(current)] + map.get_cell_value(neighbor)
            current_cost = cost_to_reach_position.get(tuple(neighbor))
            # Visualization
            open_set.add(tuple(neighbor))

            if current_cost is None or tentative_cost_to_reach < current_cost:
                # This path to neighbor is better than any previous one. Record it!
                
                came_from[tuple(neighbor)] = tuple(current)
                cost_to_reach_position[tuple(neighbor)] = tentative_cost_to_reach
                estimated_remaining_distance[tuple(neighbor)] = tentative_cost_to_reach + a_star_heuristic(neighbor, goal_pos)

                # Add the neighbor to the frontier if it is not explored yet
                if neighbor not in frontier.get_frontier():
                    frontier.insert(neighbor, tentative_cost_to_reach)
        open_set -= closed_set
        path = reconstruct_path(came_from, tuple(current)) if current == goal_pos else []
        # Visualization
        frame = visualize(map, open_set, closed_set, path)
        frames.append(deepcopy(frame))

        if len(path) > 0:
            return frames
        
    return None


def visualize(map, open_set, closed_set, path) -> ImageDraw:
    # Define scale of the image
    SCALE = 20
    # Create an all-yellow image
    image = map.create_image()
    # image = Image.new('RGB', (width * SCALE, height * SCALE),
    #                   (255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Draw open set in blue
    for node in open_set:
        y, x = node
        draw.ellipse([x*SCALE, y*SCALE, (x+1)*SCALE, (y+1)*SCALE], outline="blue", width=3)
        
    # Draw closed set in red
    for node in closed_set:
        y, x = node
        draw.ellipse([x*SCALE, y*SCALE, (x+1)*SCALE, (y+1)*SCALE], outline="red", width=3)
        
    # Draw path in green
    for node in path:
        y, x = node
        draw.ellipse([x*SCALE, y*SCALE, (x+1)*SCALE, (y+1)*SCALE], outline="green", width=3)
    map.image = image
    return image

