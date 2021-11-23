from src.toy_agent.WorldEnviroment import WorldEnv
from src.toy_agent.Grid import Grid

def test_construction():
    test_env = WorldEnv(Grid("../src/toy_agent/grids/grid1.txt"))

    assert isinstance(test_env, WorldEnv)

def test_A_matrix():
    test_env = WorldEnv(Grid("../src/toy_agent/grids/grid1.txt"))
    
    test_env.computeLikelihoodMatrix()

    assert True

def test_B_matrix():
    test_env = WorldEnv(Grid("../src/toy_agent/grids/grid1.txt"))
    
    test_env.computeTransitionMatrix()

    assert True