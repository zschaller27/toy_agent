import numpy as np

from pymdp.envs import Env

LOCATION_FACTOR_ID = 0
TRIAL_FACTOR_ID = 1

class WorldEnv(Env):
    def __init__(self, grid):
        super(WorldEnv, self).__init__()
        self.maze_grid = grid
        self.actions = {"UP" : 0, "DOWN" : 1, "LEFT" : 2, "RIGHT" : 3}

        self._transition_dist = self.computeTransitionMatrix()
        self._likelihood_dist = self.computeLikelihoodMatrix()
        
        self.state = None
        self.reset()

    def euclidianDistance(self, x, y):
        x = np.array(x)
        y = np.array(y)
        return np.linalg.norm(x - y)

    def distanceToEndState(self, state):
        state_id = np.where(state == 1)[0][0]
        print(state_id)
        return self.euclidianDistance(self.maze_grid.getStateMapIntToTuple()[state_id], self.maze_grid.getStateMapIntToTuple()[self.maze_grid.getGoalState()])

    def get_likelihood_dist(self):
        return self._likelihood_dist.copy()

    def get_transition_dist(self):
        return self._transition_dist.copy()

    def step(self, action):
        x_dim, y_dim = self.maze_grid.getDimensions()
        state_map_int = self.maze_grid.getStateMapIntToTuple()
        state_map_tuple = self.maze_grid.getStateMapTupleToInt()

        x, y = state_map_int[self.state]

        if action == "UP" and y > 0:
            self.state = state_map_tuple[(x, y - 1)]
        elif action == "DOWN" and y < y_dim - 1:
            self.state = state_map_tuple[(x, y + 1)]
        elif action == "LEFT" and x > 0:
            self.state = state_map_tuple[(x - 1, y)]
        elif action == "RIGHT" and x < x_dim - 1:
            self.state = state_map_tuple[(x + 1, y)]
        
        return self.state

    def reset(self):
        self.state = self.maze_grid.getStartLocation()

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

        A = np.eye(len(self.maze_grid.getStateMapIntToTuple()))

        return A

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
        state_map_int = self.maze_grid.getStateMapIntToTuple()
        state_map_tuple = self.maze_grid.getStateMapTupleToInt()

        # Go through each state and construct a map of state after each possible action
        for state in state_map_int.keys():
            P[state] = {action : [] for action in range(len(self.actions))}
            x, y = state_map_int[state]

            if y <= 0:
                P[state][self.actions['UP']] = state
            else:
                P[state][self.actions['UP']] =  state_map_tuple[(x, y - 1)]

            if y >= y_dim - 1:
                P[state][self.actions["DOWN"]] = state
            else:
                P[state][self.actions["DOWN"]] = state_map_tuple[(x, y + 1)]

            if x <= 0:
                P[state][self.actions['LEFT']] = state
            else:
                P[state][self.actions['LEFT']] = state_map_tuple[(x - 1, y)]
            
            if x >= x_dim - 1:
                P[state][self.actions['RIGHT']] = state
            else:
                P[state][self.actions['RIGHT']] = state_map_tuple[(x + 1, y)]

            for action in self.actions.keys():
                if self.maze_grid.getState(P[state][self.actions[action]]) == "#":
                    P[state][self.actions[action]] = state

        # Construct 3D numpy matrix showing the transitions
        B = np.zeros([len(state_map_int), len(state_map_int), len(self.actions)])
        for state in state_map_int.keys():
            # For each action find the next state using the P matrix
            for action in self.actions.keys():
                new_state = P[state][self.actions[action]]

                B[new_state, state, self.actions[action]] = 1
        
        return B
