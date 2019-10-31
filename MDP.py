import random ## this is new

class MDP():

    def __init__( self, grid ):

        ## In this assignment, there is one state per space in the grid.
        ## It is not required that you explicitly represent the states, but
        ## you may.  You are also given the transition probabilities.  Since
        ## the number of states is not constant (we will use different inputs),
        ## you may use a function (stub below) to calculate them.  For instance,
        ## if you start in a state on the left edge of the grid and move left,
        ## your program should realize that the agent should stay in the same
        ## state as a result.  The rewards for your MDP are contained in the
        ## input.

        ## Set of possible actions
        self.A = ['^', 'v', '>', '<']

        ## An attribute to store state utility values.  You do not have to use
        ## a dictionary, but it helps keep the code clear.
        self.U = dict()

    def T( self, s, a, sprime ):

        ## Return the probability of moving to state sprime after taking action
        ## a in state s.  If sprime is unreachable from s, return 0.

    def value_iteration( self ):

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
