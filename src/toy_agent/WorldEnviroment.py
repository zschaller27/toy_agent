import numpy as np

class WorldEnv:
    def __init__(self, grid):
        self.maze_grid = grid

    def computeLikelihoodMatrix(self):
        """
        Compute and return a likelihood matrix for the given maze grid. The result should be 
        n x n where n is the number of possible states from the statemap. The likelihood that an
        agent will observe state x is 1 when it is in state x, otherwise it's 0.

        Parameters:
            statemap - A dictionary where each state of the grid (value in the dictionary) has
            been mapped to an integer (key in the dictionary).

        Returns:
            Numpy identity matrix representing the likelihood matrix for the grid enviroment.
        """

        return np.eye(len(self.maze_grid.getStateMap()))

    def computeTransitionMatrix(self):
        """
        Compute and return a transition matrix for the given grid object. The matrix should show,
        for each starting state, what the final state would be for each action. If an action would
        put the agent off the grid or into a wall, the final state would be equal to the starting 
        state.

        Parameters:
            grid - A Grid object which holds all nessecary info for computing the transition matrix.

        Returns:
            A 3D numpy matrix which has the dimensions (starting state x final state x actions).
        """
        # First construct P dictionary
        P = {}
        x_dim, y_dim = self.maze_grid.getDimensions()
        actions = {"UP" : 0, "DOWN" : 1, "LEFT" : 2, "RIGHT" : 3}
        state_map = self.maze_grid.getStateMap()

        # Go through each state and construct a map of state after each possible action
        for state in state_map.keys():
            P[state] = {action : [] for action in range(len(actions))}
            x, y = state_map[state]

            ## Actions ##
            # UP
            if y == 0 or self.maze_grid.getState(state - y_dim) != '-':
                P[state]["UP"] = state
            else:
                P[state]["UP"] = state - y_dim
            
            # DOWN
            if y == y_dim - 1 or self.maze_grid.getState(state + y_dim) != '-':
                P[state]["DOWN"] = state
            else:
                P[state]["DOWN"] = state + y_dim

            # LEFT
            if x == 0 or self.maze_grid.getState(state - x_dim) != '-':
                P[state]["LEFT"] = state
            else:
                P[state]["LEFT"] = state - x_dim

            # RIGHT
            if x == x_dim - 1 or self.maze_grid.getState(state + x_dim) != '-':
                P[state]["RIGHT"] = state
            else:
                P[state]["RIGHT"] = state + x_dim
        
        # Construct 3D numpy matrix showing the transitions
        B = np.zeros([len(state_map), len(state_map), len(actions)])
        for state in state_map.keys():
            # For each action find the next state using the P matrix
            for action in actions.keys():
                new_state = P[state][actions[action]]

                B[new_state, state, actions[action]] = 1
        
        return B
