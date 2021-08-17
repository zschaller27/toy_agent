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

# Likelihood Matrix
 Since this is a grid world as well the likelihood matrix should be the same as in the example. This could be something we look to change to increase complexity, but I'm not sure what other type of world would be a good idea. 

 My current idea is to have a helper function that takes a state space (from the Grid object function) and returns a numpy identity matrix with the required shape.

# Transition Matrix

 Again this will be very similar to the tutorial because there are the same possible moves, without the STAY option.

 The idea is similar, have a helper function that takes in information from the Grid object and returns a 3D numpy transition matrix.

# Todo:
 1. Build Grid class in Grid.py ✓
 2. Build function to create likelihood matrix (A) ✓
 3. Build function to create transition matrix (B) ✓
 4. Test implementation of steps 2 and 3
 5. Plan Variational Inference steps
