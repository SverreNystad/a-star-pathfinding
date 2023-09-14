from src.Map import Map_Obj
from src.a_star import a_star

def run_astar_for_task(task_num):
    # Instantiate a map object for task 1
    task_map = Map_Obj(task_num)
    # Run the A* algorithm and find the path
    path = a_star(task_map)
    # Mark the path on the map
    task_map.mark_path(path)
    task_map.show_map()

if __name__ == '__main__':
    run_astar_for_task(1)
    run_astar_for_task(2)
    run_astar_for_task(3)
    run_astar_for_task(4)
    run_astar_for_task(5)