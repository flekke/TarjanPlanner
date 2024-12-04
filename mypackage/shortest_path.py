from geopy.distance import geodesic
from .config_data import relatives


def find_shortest_path():
    visited = set()
    path = []
    current = "R8"
    total_distance = 0

    while len(visited) < len(relatives):
        visited.add(current)
        path.append(current)
        next_relative = None
        min_distance = float('inf')

        for relative, coords in relatives.items():
            if relative not in visited:
                distance = geodesic(relatives[current], coords).kilometers
                if distance < min_distance:
                    next_relative = relative
                    min_distance = distance

        if next_relative is None:
            break

        total_distance += min_distance
        current = next_relative
    
    total_distance = int(total_distance)    
    
    return [total_distance, path]

