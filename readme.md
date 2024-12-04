# TarjanPlanner

TarjanPlanner is a tool designed to help a user organize and prioritize tasks efficiently. This README provides an overview of the project structure and how to get started.

## Project Structure

The project structure is as follows:
```
TarjanPlanner/
├── mypackage/
│   ├── __init__.py               # Package initializer
│   ├── input_handler.py          # Handles input data
│   ├── path_transport.py         # Processes transportation and route data
│   ├── shortest_path.py          # Implements the shortest path algorithm
│   ├── transport_visualizer.py   # Visualizes transport-related data
│   ├── visualizer.py             # General visualization functions
│   └── config_data.py            # Manages configuration data
├── execution_log.txt             # Execution log file
├── main.py                       # Entry point for the program
├── setup.py                      # Installation script
├── test_poject.py                # Test script for the project
└── README.md                     # Documentation (this file)
```

## How to Use

To use TarjanPlanner, follow these steps:
### Option 1. Clone the repository 
    1. Clone the repository
    2. Install the required dependencies (requirements.txt)
    3. Run the program 
    

### Option 2. Download the ZIP file
    1. Download the zip file containing the project
    2. extract the zip file to a directory
    3. navigate to the project folder in a terminal
    4. Install dependencies
   
        ```bash
        pip install -r requirements.txt
        ```
    5. Run the program 

        ```bash
        python main.py
        ```


## Features
    - Shortest path calculation
    - visualization
    - customizable inputs
    - path with transportation modes
    - logging

## Testing
To test the functionalities of the program, you can run:

    ```bash
    python test_project.py
    ```

## License
This project is licensed under the MIT License.
