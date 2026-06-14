# Rover Maze Solver

Autonomous maze-solving rover built for a university robotics course. The rover uses an A* pathfinding algorithm to compute the shortest route through a grid maze, then converts that path into motor commands, using line-following and distance sensors to correct its position along the way.

## Contents

- `Maze_Solving_Algorithm.py` - A* search implementation for finding the shortest path through the maze grid.
- `Milestone 2(a-star).py` - Earlier A* implementation milestone.
- `milestone1_lib.py` - Helper functions for basic rover movement (drive, turn, line following).
- `main.py` - Example usage of the milestone 1 movement functions.
- `SolvingMaze.py` - Combines the maze, A* path, and rover control to drive the maze end to end.
- `Automotive Final Presentation.pdf` - Final presentation slides for the project.

## How it works

1. The maze is read in as a grid with a start (`S`) and end (`E`) cell.
2. A* search finds the shortest path from start to end while avoiding walls.
3. The path is converted into a sequence of moves (forward, turn left, turn right) based on the rover's current heading.
4. The rover executes each move, using its line sensors to stay aligned at corners.

## Hardware

Built on the Freenove Micro Rover platform with a micro:bit controller.
