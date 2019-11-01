######################################################################
# Author: Elaheh Jamali
# Username: Jamalie

# Programming Assignment 2: Markov Decision Process
#
# Purpose: Markov Decision Processes are mathematical frameworks
# used to model a sequential decision-making problem.
#
# Acknowledgement: Giorgi Lomia
#
######################################################################
import random

class MDP():

    def __init__( self, grid ):


        self.grid = grid

    ## Set of possible actions
        self.A = ['^', 'v', '>', '<']


        ## In this assignment, there is one state per space in the grid.
        ## It is not required that you explicitly represent the states, but
        ## you may.  You are also given the transition probabilities.  Since
        ## the number of states is not constant (we will use different inputs),
        ## you may use a function (stub below) to calculate them.  For instance,
        ## if you start in a state on the left edge of the grid and move left,
        ## your program should realize that the agent should stay in the same
        ## state as a result.  The rewards for your MDP are contained in the
        ## input.


        ## An attribute to store state utility values.  You do not have to use
        ## a dictionary, but it helps keep the code clear.
        self.U = [[0 for j in range (len(self.grid[0]))] for i in range(len(self.grid))]
        print(self.U)

    def value_iteration(self):
        gamma = 0.9
        for i in range (len(self.grid)):
            for j in range(len(self.grid)):
                best_a = [self.get_expected_value(i,j,"v"),"v"]
                for a in self.A:
                    if self.get_expected_value(i,j,a) > best_a[0]:
                        best_a = [self.get_expected_value(i,j,a),a]
                self.U[i][j] = self.grid[i][j] + gamma * best_a[0]
        print(self.U)

    ## The value iteration algorithm.  You may use any value for gamma
        ## between 0 and 1 (typically set to something like 0.99).  The number
        ## of updates to carry out is not fixed, but you must run until the
        ## resulting policy converges and stops changing.  You can do this by
        ## iterating until the utility values stop changing by much.  Usually,
        ## this is accomplished by setting some parameter epsilon (small value,
        ## on the order of .1, .01, etc.), summing up the differences between
        ## state utility values before and after the update, and checking
        ## whether it is less than epsilon.


    def get_policy( self ):

        ## Use the attribute self.U to determine the appropriate policy, and
        ## return a grid the same size as the input
        gamma = 0.9
        for i in range (len(self.grid)):
            for j in range(len(self.grid)):
                best_a = [self.get_expected_value(i,j,"v"),"v"]
                for a in self.A:
                    if self.get_expected_value(i,j,a) > best_a[0]:
                        best_a = [self.get_expected_value(i,j,a),a]
                # self.U[i][j] = self.grid[i][j] + gamma * best_a[0]
                self.U[i][j] = best_a[1]
        print(self.U)

    def get_val(self,i,j):
        if i < 0:
            return self.grid[i+1][j]
        elif i > len(self.grid) - 1:
            return self.grid[i-1][j]
        if j < 0 :
            return self.grid[i][j+1]
        elif j > len(self.grid[i])-1:
            return self.grid[i][j-1]
        return self.grid[i][j]

    def get_expected_value(self, i ,j ,a):
        e_val = 0
        if a == '^':
           e_val = self.get_val(i-1, j)*0.7 + self.get_val(i+1,j) * 0.1 + self.get_val(i, j+1 )* 0.1 + self.get_val(i,j-1) * 0.1
        elif a == 'v':
           e_val = self.get_val(i-1, j)*0.1 + self.get_val(i+1,j) * 0.7 + self.get_val(i, j+1 )* 0.1 + self.get_val(i,j-1) * 0.1
        elif a == '>':
            e_val = self.get_val(i-1, j)*0.1 + self.get_val(i+1,j) * 0.1 + self.get_val(i, j+1 )* 0.7 + self.get_val(i,j-1) * 0.1
        elif a == '<':
            e_val = self.get_val(i-1, j)*0.1 + self.get_val(i+1,j) * 0.1 + self.get_val(i, j+1 )* 0.1 + self.get_val(i,j-1) * 0.7
        return e_val

def main():
        grid = [[0,0,10],
                [0,-1,0],
                [0,-1,0]]
        gridworld = MDP(grid)
        gridworld.value_iteration()
        gridworld.get_policy()

main()
