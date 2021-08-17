import numpy as np

from src.Grid import Grid

class WorldEnv:
    def __init__(self, grid):
        self.maze_grid = grid
        self.likelihood_matrix = self.computeLikelihoodMatrix(grid.getStateMap())
        # self.transition_matrix = 

    def computeLikelihoodMatrix(self, statemap):
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

        return np.eye(len(statemap))

    def computeTransitionMatrix(self, grid):
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
        # TODO: finish implementation of this function
        pass
