import numpy as np
from Grid import Grid
from WorldEnviroment import WorldEnv

from pymdp.agent import Agent

env = WorldEnv(Grid("src/toy_agent/grids/test_grid.txt"))

# print(env.computeTransitionMatrix())

agent = Agent(A=env.computeLikelihoodMatrix(), B=env.computeTransitionMatrix(), control_fac_idx=[0])
