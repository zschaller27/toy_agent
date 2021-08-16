import os
class Grid:
    def __init__(self, file_path):
        """
        Initialize a grid object to have 3 member variables.

        grid_loc_dict - a dictionary which links coordinates to whether that position is a wall or not.
        agent_start - the coordinates where the agent should start.
        goal_state - the coordinates of the goal state.
        """
        # Check if file_path is a valid path
        if not os.path.isfile(file_path):
            raise RuntimeError("invalid file_path given \"%s\" no file found that at that location" %(file_path))
        
        # Open the given file path and read in information from the text file.
        grid_file = open(file_path, "r")
        
        # Go through each grid location (x, y), starts at (0, 0) which is the top left of the grid. 
        # Each '\n' moves to a new y value. x values designate the columns, and y values designate
        # the rows.
        #   - : a spot where the agent can move to
        #   # : a wall spot where the agent cannot move to
        #   X : the goal state

        self.grid_loc_dict = {}     # initalize the dictionary (Key = coordinates, Value = character)
        coords = (0, 0)             # initalize the x and y coords

        # Loop through each char in the file
        for loc in grid_file.read():
            # Check if the given character is '\n'
            if loc == '\n':
                coords = (0, coords[1] + 1)
                continue
            
            # Check if the given character is 'S' denoting starting state
            if loc == 'S':
                self.grid_loc_dict[coords] = '-'
                self.agent_start = coords
            # Check if hte given character is 'X' denoting goal state
            elif loc == 'X':
                self.grid_loc_dict[coords] = '-'
                self.goal_state = coords
            # Otherwise add dictionary entry
            else:
                self.grid_loc_dict[coords] = loc

            coords = (coords[0] + 1, coords[1])

    def getState(self, coords):
        """
        Returns the saved grid value for a given coordinate location

        Paramters:
            coords - a coordinate tuple in the form of (x, y)
        
        Returns:
            grid character associated with the the given coordinates
        """
        return self.grid_loc_dict[coords]
    
    def getStartLocation(self):
        """
        Returns the coordinates that the agent is designated to start at

        Returns:
            Coordinate tuple in the form of (x, y)
        """
        return self.agent_start
    
    def isGoalState(self, coords):
        """
        Returns a boolean indicating whether the given coordinates are the
        goal state.

        Parameters:
            coords - a coordinate tuple in the form of (x, y)

        Returns:
            True - if the given coordinates is the goal state.
            False - othwerwise
        """
        return coords == self.goal_state
    
    def getStateMap(self):
        """
        Returns a dictionary which maps each state to a single integer.

        Returns:
            dictionary where each key is an integer and associated with a single
            coordinate.
        """
        return_dict = {}    # Initialize a dictionary to update

        # For each key, assign it the next avalible integer
        for i, key in enumerate(self.grid_loc_dict.keys()):
            return_dict[i] = key

        return return_dict
