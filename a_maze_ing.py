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


#Parsing
"""
Context managers — do you know Python's open("file.txt") as f
"""

#Error handling
"""
Your program must handle all errors gracefully: invalid configuration, file not found, bad
syntax, impossible maze parameters, etc. It must never crash unexpectedly, and must always
provide a clear error message to the user.

The "42" pattern may be omitted in case the maze size does not allow it (i.e. too small).
> Print an error message on the console in that case.

 Graceful errors: missing file, bad syntax, missing key, out-of-bounds entry/exit,
      entry == exit, impossible dimensions
"""


#Menu
"""
- **A graphical display using the MiniLibX (MLX) library.**

=== A-Maze-ing ===
1. Re-generate a new maze
2. Show / Hide the shortest path
3. Rotate the wall colours
4. Quit
Choice? (1-4): _
"""