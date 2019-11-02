######################################################################
# Author: Elaheh Jamali
# Username: Jamaliela

# Programming Assignment 2: Markov Decision Process
#
# Purpose: Markov Decision Processes are mathematical frameworks
# used to model a sequential decision-making problem.
#
# Acknowledgements: Emely Alfaro, Gerardo Soto and Elyor Tukhtasinov (Classmates. we worked on the homework together)
# Special thanks to Professor Shepherd and Giorgi Lomia
#
######################################################################
# In this assignment, there is one state per space in the grid.
# if you start in a state on the left edge of the grid and move left,
# the program should realize that the agent should stay in the same
# state as a result.  The rewards for the MDP are contained in the input.

import copy


class MDP:

    def __init__(self, grid):

        self.grid = grid
        self.A = ['^', 'v', '>', '<']   # Set of possible actions
        self.U = [[0 for j in range(len(self.grid[0]))] for i in range(len(self.grid))]  # An attribute to store state utility values.
        self.G = [[0 for j in range(len(self.grid[0]))] for i in range(len(self.grid))]
        self.policy = [[0 for j in range(len(self.grid[0]))] for i in range(len(self.grid))]
        print(self.U)

    def value_iteration(self):   # The value iteration algorithm.
        gamma = 0.9
        for k in range(100):
            for i in range(len(self.grid)):
                for j in range(len(self.grid)):
                    best_a = [self.get_expected_value(i, j, "v"), "v"]
                    for a in self.A:
                        if self.get_expected_value(i, j, a) > best_a[0]:
                            best_a = [self.get_expected_value(i, j, a), a]
                    print(best_a)
                    self.G[i][j] = self.grid[i][j] + gamma * best_a[0]
            print(self.U)
            self.U = copy.deepcopy(self.G)

    def get_policy(self):
        # Using the attribute self.U to determine the appropriate policy, and
        # returning a grid the same size as the input
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                best_a = [self.get_expected_value(i, j, "v"), "v"]
                for a in self.A:
                    if self.get_expected_value(i, j, a) > best_a[0]:
                        best_a = [self.get_expected_value(i, j, a), a]
                self.policy[i][j] = best_a[1]
        print(self.policy)

    def get_val(self, i, j): # self grid is the reward were we are keeping the self U is keep getting updated.
        if i < 0:
            return self.U[i+1][j]
        elif i > len(self.U) - 1:
            return self.U[i-1][j]
        if j < 0:
            return self.U[i][j+1]
        elif j > len(self.U[i])-1:
            return self.U[i][j-1]
        return self.U[i][j]

    def get_expected_value(self, i, j, a):
        expected_value = 0
        if a == '^':
            expected_value = self.get_val(i-1, j)*0.7 + self.get_val(i+1, j) * 0.1 + self.get_val(i, j+1) * 0.1 + self.get_val(i, j-1) * 0.1
        elif a == 'v':
            expected_value = self.get_val(i-1, j)*0.1 + self.get_val(i+1, j) * 0.7 + self.get_val(i, j+1) * 0.1 + self.get_val(i, j-1) * 0.1
        elif a == '>':
            expected_value = self.get_val(i-1, j)*0.1 + self.get_val(i+1, j) * 0.1 + self.get_val(i, j+1) * 0.7 + self.get_val(i, j-1) * 0.1
        elif a == '<':
            expected_value = self.get_val(i-1, j)*0.1 + self.get_val(i+1, j) * 0.1 + self.get_val(i, j+1) * 0.1 + self.get_val(i, j-1) * 0.7
        return expected_value


def main():
        grid = [[0, 0, 10],
                [0, -1, 0],
                [0, -1, 0]]
        grid_world = MDP(grid)
        grid_world.value_iteration()
        grid_world.get_policy()


main()
