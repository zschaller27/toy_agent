# toy_agent
 Simple Active Inference maze agent which is built to find the shortest route through a maze.

# Grid
 Grids can be imported by giving the Grid class a valid text file with the following format:
    S : starting position of the agent
    X : the maze exit
    # : impassable wall
    - : agent can use this space to move

# Possible Actions
 The agent can go North, South, East, and West as long as they don't go off the grid or walk into a wall.

# Todo:
 1. Build Grid class in Grid.py ✓
 2. Build function to create likelihood matrix (A)
 3. Build function to create transition matrix (B)
 4. Plan Variational Inference steps
