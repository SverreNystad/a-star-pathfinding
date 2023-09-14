import pytest
from src.a_star import a_star_heuristic, reconstruct_path, Frontier

# def test_frontier_init():
#     # Arrange
#     map = Map_Obj(task=1)
#     start_pos = map.get_start_pos()
#     frontier = Frontier(start_pos, map)
#     # Act
#     empty_frontier = frontier.get_frontier()
#     # Assert
#     assert empty_frontier == [start_pos]



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
