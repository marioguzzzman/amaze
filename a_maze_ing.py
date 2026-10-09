"""A-Maze-ing: entry point.

Usage: python3 a_maze_ing.py config.txt

Reads the configuration file, asks ``mazegen.MazeGenerator`` for a maze,
writes the hex output file, and runs the interactive terminal display.
"""

# Notes on building:
#   1. config parsing   -> validated settings and errors
#   2. maze generation  -> mazegen/generator.py
#   3. output file      -> hex grid + entry + exit + path
#   4. display + menu   
