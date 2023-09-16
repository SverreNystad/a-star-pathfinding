from src.Map import Map_Obj
from src.a_star import a_star
from src.visualize_exploration import a_star_with_visualization

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

def run_a_star_for_task_with_creation_of_gif(task_num):
    task_map = Map_Obj(task_num)
    frames = a_star_with_visualization(task_map)
    # After the A* algorithm completes, compile the frames into a GIF
    frames[0].save(f'docs/exploration_of_task_{task_num}.gif', save_all=True, append_images=frames[1:], loop=0, duration=100)

if __name__ == '__main__':
    TASKS = 5
    
    print("Running A* for the tasks...")
    for task in range(1, TASKS+1):
        print(f"Task {task}:")
        run_a_star_for_task(task)
    
    print("Creating GIFs for the exploration of the maps...")
    for task in range(1, TASKS+1):
        print(f"Task {task}:")
        run_a_star_for_task_with_creation_of_gif(task)
        print(f"Created GIF for task {task}.")
