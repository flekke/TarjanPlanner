from mypackage.config_data import *
from mypackage.input_handler import get_user_input
from mypackage.shortest_path import find_shortest_path
from mypackage.path_transport import *
from mypackage.visualizer import draw_graph
import time
import functools
from pathlib import Path
from mypackage.transport_visualizer import visualize_transport_path



def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        
        log_path = Path('execution_log.txt')
        with open(log_path, 'a') as f:
            f.write(f"{func.__name__} executed in {execution_time:.4f} seconds\n")
        
        return result
    return wrapper

@log_execution_time
def main():

    answer = get_user_input()
    service_type = answer[0]    
    priority = answer[1] if len(answer) == 2 else None

    #service_type = 1  meaning shortest path
    if service_type == 1:   
        result = find_shortest_path()
        print(f"total distance is {result[0]}km and the route is {result[1]}")
        draw_graph()

    #sesrvice_type = 2 meaning transportation
    else:
        if priority == 1: 
            transport_minimal_time()
            visualize_transport_path(1)
        elif priority == 2:
            transport_minimal_cost()
            visualize_transport_path(2)
        else:
            transport_minimal_transfer()
            visualize_transport_path(3)

if __name__ == "__main__":
    main()  

