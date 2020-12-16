"""
module with names that should not be changed during the execution of the system.

Some are constants (INTRA, INTER) others control system behaviour

"""
import sys

# NO CHANGES
# to index array in node object: ugly but I found no other way in python
INTRA = 0
INTER = 1

# in case we want the max degree of a node in a community
# < community_size *( max degree in the largest community / largest community size)
# set ADJUSTED_MAX_DEGREE = True
ADJUSTED_MAX_DEGREE = False

# maximum number of cycles to try to link a community or a network before giving up
MAX_CYCLES = 100

# do not allow disjoint communities (can happen if minimum degree < community size -1
ALLOW_DISJOINT_COMMUNITIES = False

# joint distribution of node degrees, auxiliary variables
ALFA_MAX = 5            # Strongest dissortative (used for beta_assortativity distribution as 
# alfa_assortativity and beta_assortativity parameters)
BETA_MAX = 5           # Strongest assortative

EVENT_DICT = {'N': 'Begin',
              'R': 'Regenerate',
              'G': 'Grow',
              'C': 'Contract',
              'P': 'Preserve',
              'O': 'Replace',
              'S': 'Split',
              'M': 'Merge',
              'F': 'Vanish',
              'A': 'Absorb',
              'B': 'Resurge'}

TYPE_DICT = {'S': 'Start',          # current state
             'E': 'End',            # what happened at the end of the transition
             'T': 'To',
             'F': 'From'}


# Create a global timestamp for dynamic time management
class Ts:
    timestamp = 0


sys.setrecursionlimit(10000)            # needed for scanning the network for disjoint communities
