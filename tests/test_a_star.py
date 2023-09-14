import pytest
from src.Map import Map_Obj
from src.a_star import a_star, a_star_heuristic, reconstruct_path, Frontier

def test_frontier_init():
    # Arrange
    start_pos = (0, 0)
    goal_pos = (0, 1)
    frontier = Frontier(start_pos, goal_pos)
    # Act
    empty_frontier = frontier.get_frontier()
    # Assert
    assert empty_frontier == [start_pos]

def test_frontier_pop_when_only_one_element():
    # Arrange
    start_pos = (0, 0)
    goal_pos = (0, 1)
    frontier = Frontier(start_pos, goal_pos)
    # Act
    popped_element = frontier.pop()
    # Assert
    assert popped_element == start_pos

def test_frontier_pop_when_several_elements():
    # Arrange
    start_pos = (0, 0)
    goal_pos = (0, 2)
    neighbor_further_away_from_goal = [start_pos[0] + 1, start_pos[1]]
    frontier = Frontier(start_pos, goal_pos)
    frontier.insert(neighbor_further_away_from_goal)
    # Act
    popped_element = frontier.pop()
    # Assert
    assert popped_element == start_pos

def test_frontier_insert():
    # Arrange
    start_pos = (0, 0)
    goal_pos = (0, 2)
    neighbor_further_away_from_goal = (start_pos[0] + 1, start_pos[1])
    frontier = Frontier(start_pos, goal_pos)
    # Act
    frontier.insert(neighbor_further_away_from_goal)
    # Assert
    assert len(frontier.get_frontier()) == 2

def test_frontier_insert_sorts_descending():
    # Arrange
    start_pos = (0, 0)
    goal_pos = (0, 2)
    neighbor_further_away_from_goal = (start_pos[0] + 1, start_pos[1])
    frontier = Frontier(start_pos, goal_pos)

    descending_frontier = [neighbor_further_away_from_goal, start_pos]
    # Act
    frontier.insert(neighbor_further_away_from_goal)
    # Assert
    assert frontier.get_frontier() == descending_frontier

def test_frontier_inserting_same_element_twice():
    # Arrange
    start_pos = (0, 0)
    goal_pos = (0, 2)
    neighbor_further_away_from_goal = (start_pos[0] + 1, start_pos[1])
    frontier = Frontier(start_pos, goal_pos)
    # Act
    frontier.insert(neighbor_further_away_from_goal)
    frontier.insert(neighbor_further_away_from_goal)
    # Assert # TODO FIND CORRECT ANSWER
    # assert len(frontier.get_frontier()) == 2

def test_a_star_heuristic_no_difference():
    # Arrange
    start_pos = [0, 0]
    # Act
    manhattan_distance = a_star_heuristic(start_pos, start_pos)
    # Assert
    assert manhattan_distance == 0


def test_a_star_heuristic_difference():
     # Arrange
    start_pos = [0, 0]
    goal_pos = [5, 5]
    # Act
    manhattan_distance = a_star_heuristic(start_pos, goal_pos)
    # Assert
    assert manhattan_distance == 10

def test_a_star_heuristic_negative_difference():
    # Arrange
    start_pos = [0, 0]
    goal_pos = [-5, 5]
    # Act
    manhattan_distance = a_star_heuristic(start_pos, goal_pos)
    # Assert
    assert manhattan_distance == 10

def test_reconstructing_path():
    # Arrange
    came_from = {(0, 0): (0, 1), (0, 1): (0, 2), (0, 2): (0, 3)}
    current = (0, 3)
    # Act
    total_path = reconstruct_path(came_from, current)
    # Assert
    assert total_path == [(0, 0), (0, 1), (0, 2), (0, 3)]

def test_reconstructing_path_when_no_path_exists():
    # Arrange
    came_from = {(0, 0): (0, 1), (0, 1): (0, 2)}
    current = (0, 3)
    # Act
    total_path = reconstruct_path(came_from, current)
    # Assert
    assert total_path == [(0, 3)]

def test_reconstructing_path_when_start_is_goal():
    # Arrange
    came_from = {(0, 0): (0, 0)}
    current = (0, 0)
    # Act
    total_path = reconstruct_path(came_from, current)
    # Assert
    assert total_path == [(0, 0)]

def test_reconstructing_path_when_there_are_several_paths():
    # Arrange
    came_from_path_1 = {(0, 0): (0, 1), (0, 1): (0, 2)}
    came_from_path_2 = {(10, 0): (9, 1), (9, 1): (8, 2)}
    came_from_path_1.update(came_from_path_2)
    current_1 = (0, 2)
    current_2 = (8, 2)
    # Act
    total_path_1 = reconstruct_path(came_from_path_1, current_1)
    total_path_2 = reconstruct_path(came_from_path_2, current_2)
    # Assert
    assert total_path_1 == [(0, 0), (0, 1), (0, 2)]
    assert total_path_2 == [(10, 0), (9, 1), (8, 2)]


def test_a_star():
    # Arrange
    map_obj = Map_Obj()
    
    # Act
    path = a_star(map_obj)
    # Assert
    assert path != None

def test_a_star_when_start_is_goal():
    # Arrange
    map_obj = Map_Obj()
    map_obj.end_goal_pos = map_obj.start_pos
    # Act
    path = a_star(map_obj)
    # Assert
    assert path == [[0, 0]]