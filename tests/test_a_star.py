import pytest
from src.Map import Map_Obj, Frontier

def test_frontier_init():
    # Arrange
    map = Map_Obj(task=1)
    start_pos = map.get_start_pos()
    frontier = Frontier(start_pos, map)
    # Act
    empty_frontier = frontier.get_frontier()
    # Assert
    assert empty_frontier == [start_pos]



def test_a_star_heuristic():
    # Arrange
    map = Map_Obj(task=1)
    start_pos = map.get_start_pos()
    frontier = Frontier(start_pos, map)
    # Act
    manhattan_distance = frontier.manhattan_distance(start_pos, start_pos)
    # Assert
    assert manhattan_distance == 0