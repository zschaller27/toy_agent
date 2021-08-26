from toy_agent.WorldEnviroment import WorldEnv
from toy_agent.Grid import Grid

def test_construction():
    test_env = WorldEnv(Grid("C:\\Users\\Zach\\Documents\\Nested Minds\\toy_agent\\src\\toy_agent\\grids\\grid1.txt"))

    assert isinstance(test_env, WorldEnv)

def test_A_matrix():
    test_env = WorldEnv(Grid("C:\\Users\\Zach\\Documents\\Nested Minds\\toy_agent\\src\\toy_agent\\grids\\grid1.txt"))
    
    assert test_env.computeLikelihoodMatrix().shape == (81, 81)

def test_B_matrix():
    test_env = WorldEnv(Grid("C:\\Users\\Zach\\Documents\\Nested Minds\\toy_agent\\src\\toy_agent\\grids\\grid1.txt"))
    
    print(test_env.computeTransitionMatrix())