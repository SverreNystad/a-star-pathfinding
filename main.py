from src.Map import Map_Obj
from src.a_star import a_star

def run_a_star_for_task(task_num):
    # Instantiate a map object for task 1
    task_map = Map_Obj(task_num)
    # Run the A* algorithm and find the path
    path = a_star(task_map)
    # Mark the path on the map
    task_map.mark_path(path)
    # Add the start and goal positions to the map
    themap = task_map.str_map
    task_map.set_start_pos_str_marker(task_map.start_pos, themap)
    task_map.set_goal_pos_str_marker(task_map.goal_pos, themap)
    task_map.show_map()

if __name__ == '__main__':
    run_a_star_for_task(1)
    run_a_star_for_task(2)
    run_a_star_for_task(3)
    run_a_star_for_task(4)
    run_a_star_for_task(5)