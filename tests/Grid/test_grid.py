from src.Grid import Grid

def test_grid():
    # Create test grid object
    test_grid = Grid("src\\grids\\grid1.txt")

    # Test member functions
    assert test_grid.agent_start == (0,0)
    assert test_grid.isGoalState((0, 0)) == False
    assert test_grid.isGoalState((8, 8)) == True