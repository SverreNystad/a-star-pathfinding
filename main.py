from src.Map import Map_Obj
from src.a_star import a_star


# Instantiate a map object for task 1
task_1_map = Map_Obj(1)
# Run the A* algorithm and find the path
path_1 = a_star(task_1_map)
print(path_1)
# Mark the path on the map
task_1_map.mark_path(path_1)
task_1_map.show_map()

# Instantiate a map object for task 2
task_2_map = Map_Obj(2)
# Run the A* algorithm and find the path
path_2 = a_star(task_2_map)
print(path_2)
# Mark the path on the map
task_2_map.mark_path(path_2)
task_2_map.show_map()

# Instantiate a map object for task 3
task_3_map = Map_Obj(3)
# Run the A* algorithm and find the path
path_3 = a_star(task_3_map)
print(path_3)
# Mark the path on the map
task_3_map.mark_path(path_3)
task_3_map.show_map()