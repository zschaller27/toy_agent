import os
import numpy as np
import matplotlib.pyplot as plt
from Grid import Grid
from WorldEnviroment import WorldEnv
from pymdp.agent import Agent

def plot_beliefs(belief_dist, title=""):
    if not isinstance(belief_dist, np.ndarray):
        values = belief_dist.values[:, 0]
    else:
        values = belief_dist
    plt.grid(zorder=0)
    plt.bar(range(belief_dist.shape[0]), values, color='r', zorder=3)
    plt.xticks(range(belief_dist.shape[0]))
    plt.title(title)
    plt.show()

env = WorldEnv(Grid("src/toy_agent/grids/grid1.txt"))

A = env.get_likelihood_dist()
B = env.get_transition_dist()

agent = Agent(A=A, B=B, control_fac_idx=[0])

agent.D = np.array([np.ones(Ns) for Ns in agent.n_states])

plot_beliefs(agent.D[0],"Original Beliefs about Initial Location")

agent.D[0] = np.eye(agent.n_states[0])[env.maze_grid.getStartLocation()]


#initial location with prior beliefs 
plot_beliefs(agent.D[0],"Update Beliefs about Initial Location")

plot_beliefs(agent.C, "Original Beliefs about Goal State")

agent.C[env.maze_grid.getGoalState()] = 1

plot_beliefs(agent.C, "Updated Beliefs about Goal State")

T = 1
observation = [env.state, env.distanceToEndState(env.state)]

for t in range(T):
    belief_state = agent.infer_states(observation)

    agent.infer_policies()

    print(agent.sample_action())