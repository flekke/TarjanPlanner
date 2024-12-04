from geopy.distance import geodesic
from .config_data import relatives, transportation_mode
from mypackage.shortest_path import find_shortest_path



'''
Distance that the transportation is available
Train	5km<n
Bus	2km<n
Bicycle	1km<n
Walk	0km<n
'''

#with transportation
the_path = find_shortest_path()[1]

#minimal time
def transport_minimal_time():
    total_time = 0
    for i in range(len(the_path)-1):
        start = relatives[the_path[i]]
        end = relatives[the_path[i+1]]
        distance = geodesic(start, end).km
        
        # Choose transportation based on distance
        if distance > 5:
            transport = 'train'
        elif 2 < distance <= 5:
            transport = 'bus'
        elif 1 < distance <= 2:
            transport = 'bicycle'
        else:
            transport = 'walking'
            
        time = (distance / transportation_mode[transport]['speed']) + transportation_mode[transport]['transfer_time']
        total_time += time
        print(f"{the_path[i]}->{the_path[i+1]}: {transport.capitalize()} ({distance:.2f}km, {time:.0f} minutes)")
    
    print(f"\nTotal journey time: {total_time:.2f} minutes")


#minimal cost
def transport_minimal_cost():
    total_cost = 0
    for i in range(len(the_path)-1):
        start = relatives[the_path[i]]
        end = relatives[the_path[i+1]]
        distance = geodesic(start, end).km
        
        # Prioritize walking and bicycle for no cost
        if distance <= 1:
            transport = 'walking'
        else:
            transport = 'bicycle'
        
        cost = transportation_mode[transport]['cost']
        total_cost += cost    
        print(f"{the_path[i]}->{the_path[i+1]}: {transport.capitalize()} ({distance:.2f}km)")
    
    print(f"\nTotal journey cost: {total_cost}")

def transport_minimal_transfer():
    distances = []
    total_time = 0
    
    for i in range(len(the_path)-1):
        start = relatives[the_path[i]]
        end = relatives[the_path[i+1]]
        distance = geodesic(start, end).km
        distances.append((i, distance))
    
    sorted_distances = sorted(distances, key=lambda x: x[1], reverse=True)
    
    # Counters for limited transportation modes
    bus_count = 1
    train_count = 2
    bicycle_count = 3
    
    choices = ['walking'] * len(distances)
 
    # Assign transportation modes starting with longest distances
    for i, distance in sorted_distances:
        if distance > 5 and train_count > 0:
            choices[i] = 'train'
            train_count -= 1
        elif distance > 2 and bus_count > 0:
            choices[i] = 'bus'
            bus_count -= 1
        elif distance > 1:
            choices[i] = 'bicycle'
        else:
            choices[i] = 'walking'

    # Track previous mode for transfer time calculation
    prev_mode = None
    total_time = 0

    for i in range(len(the_path)-1):
        distance = distances[i][1]
        mode = choices[i]
        
        # Only add transfer time if transportation mode changes
        transfer = transportation_mode[mode]['transfer_time'] if prev_mode != mode else 0
        time = (distance / transportation_mode[mode]['speed']) + transfer
        total_time += time
        print(f"{the_path[i]}->{the_path[i+1]}: {mode.capitalize()} ({distance:.2f}km, {time:.0f} minutes)")
        
        prev_mode = mode

    print(f"\nTotal journey time: {total_time:.2f} minutes")

