from Freenove_Micro_Rover import *
from Maze_Solving_Algorithm import *
from Maze import *                       #Import functions, our A* algo, maze and robot control class


def parse_maze(maze_str):
    return [row.split() for row in maze_str.strip().split("\n")]  #converts maze to string(2d array)


maze_string = Give_Maze()                  #a value maze_string = gets maze string
maze = parse_maze(maze_string)             #a value maze = maze string after conversion

Rover = Micro_Rover()                     #initializes the rover and imports all functions need from MicroRover class
display.show(Image.HAPPY)                 #displays :) to show that the rover is ready


def go_straight():                        #moves forward, both motors for 0.7 seconds
    Rover.all_led_show(0, 100, 0, 0)
    Rover.motor(50, 50)
    sleep(700)
    Rover.motor(0, 0)


def turn_around():                        #rotates 180 degrees
    Rover.motor(60, -60)
    sleep(1300)


def go_left():
    Rover.all_led_show(0, 100, 0, 0)
    Rover.motor(80, 80)
    sleep(500)
    Rover.motor(-60, 60)
    sleep(620)
    while (
        pin14.read_digital() == 0
        and pin15.read_digital() == 0
        and pin16.read_digital() == 0
    ):
        Rover.motor(-60, 60)
    Rover.motor(0, 0)


def go_right():
    Rover.all_led_show(0, 100, 0, 0)
    Rover.motor(80, 80)
    sleep(500)
    Rover.motor(60, -60)
    sleep(620)
    while (
        pin14.read_digital() == 0
        and pin15.read_digital() == 0
        and pin16.read_digital() == 0
    ):
        Rover.motor(60, -60)
    Rover.motor(0, 0)


# Run A* algorithm to find the shortest path as a list of coordinates
shortest_path = a_star_search(maze)

if shortest_path is None:                                            #if no path is found, output :(
    display.show(Image.SAD)
    raise ValueError("No valid path found in the maze!")  #raise error: no path found


def convert_path_to_commands(path):                                                       #trasnlates coordinates to commands for the rover (S,L,R)
    commands = []                                                                                   #Empty list of the commands
    directions = {(0, 1): "R", (1, 0): "D", (0, -1): "L", (-1, 0): "U"}                         #directions guide
    movement_sequence = [
        directions[(path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])]            #translates right down up and left to coordinates that translate to right,straight or left
        for i in range(len(path) - 1)
    ]
    direction_order = "RDLU"                                                         #needs to be done in order to let the rover know circular compass
    current_dir = "R"                                                              #current direction so it knows which direction it's at

    for move in movement_sequence:             #decides to move whether right or left according to the compass
        if move == current_dir:                #right direction = Straight in that direction
            commands.append("S")
        else:
            current_idx, move_idx = direction_order.index(          #
                current_dir
            ), direction_order.index(move)
            commands.append("R" if (move_idx - current_idx) % 4 == 1 else "L")
            current_dir = move
    return "".join(commands)                  #turns the list into 1 string


commands = convert_path_to_commands(shortest_path)
commands += 'S' # For completing the last command

while commands:
    sensor_value = (
        pin14.read_digital() << 2 | pin15.read_digital() << 1 | pin16.read_digital()
    )

    if commands and sensor_value == 7:
        current_command, commands = commands[0], commands[1:]
        if current_command == "S":
            go_straight()
        elif current_command == "R":
            go_right()
        elif current_command == "L":
            go_left()
    elif sensor_value in [2, 5]:
        Rover.motor(70, 70)
    elif sensor_value in [4, 6]:
        Rover.motor(20, 90)
    elif sensor_value in [1, 3]:
        Rover.motor(90, 20)
    elif sensor_value == 0:
        turn_around()

Rover.motor(0, 0)
Rover.all_led_show(100, 0, 0, 0)
display.show(Image.HEART)
