*******************************************************************************************************
Taxonomy: Community-Lifecycle, Code to analyse a temporal network and output community lifecycle events
*******************************************************************************************************

Description
#############
Please refer to "Community identity in a temporal network: A taxonomy proposal", Pereira et al., pre-print submitted to Elsevier.
or to "A Taxonomy of Community Lifecycle Events in Temporal Networks", on IEEE Xplore repository.

This python code uses various classes from "Syntgen: A synthetic temporal network generator with clustering and known ground truth"  published in the IMA Journal of Complex Networks, https://doi.org/10.1093/comnet/cnz039. Syntgen code is available at https://github.com/ramadap/Syntgen

This package is a Python system to analyse a timestamped sequence of tuples containing a note and its community.
It outputs a printed list of community lifecycle events as described in the referenced paper. 

The main program expects a triple of integers (timestamp, node number, community number) for every input invocation. 
Lifecycle events are dependent on community changes and external thresholds, as specified in input specifications.  

Pre-requisites
==============
Python v3.5+

Libraries: numpy, itertools, random, bisect, csv, ast

Operation
==========
to run:
    execute taxonomy


Input:
User should code an input function that returns the time ordered triple (timestamp, node number, community number) for every invocation. 
Two samples functions are provided, one for gephi gexf format (input) and another (input_football), a CSV file with one line per snapshot, where position indicates node number and the value, the community it belongs to. 


Output:
	Console text describing community events at the end and start of each timestep with additional stattistics depending on parameters 


Parameters
=============

All input specified in file **user_specifications.py**
This file is shared with Syntgen, and only the two parameters included below are used in lifecycle determination. 

.. csv-table:: Behaviour parameters
   :header: "Parameter", "Description", "Default"
   :widths: 15, 100, 10

    "DEBUG",verbose output (debug),No
    "jaccard_null_model",whether to adjust the jaccard index to a null random model when comparing communities for lifecycle determination",TRUE
    "Sigma","jaccard threshold for community matching, value between [0,1] 1 requires exact matching",0.2

User defined functions
***********************

User defined functions are shared with Syntgen. Only the print parameters function should be changed for lifecycle determination 

Print parameters
*********************************************************
.. code:: python

    def print_parameters():
        """
        Return booleans to control print output at the end of each snapshot
        :return: confusion_matrix_print, confusion_matrix_percentage, jaccard_index, continuity, \
               community_events_t0, community_events_t1
    # Defaults
    confusion_matrix_print = True
    confusion_matrix_percentage = True
    jaccard_index = True
    continuity = False
    community_events_t0 = True
    community_events_t1 = True


Sample of User Changes Function
*******************************
.. code:: python

    def user_changes_specs(communities: 'list[Community]', nodes: 'list[Nodes]') -> 'list[Nodes]':
        """ returns a list of nodes to delete. it's up to the user which nodes should be killed
        :param communities: list of community objects
        :param nodes: list of node objects
        :return: dead_node_vector: list of nodes to delete (default 10% randomly selected)

Sample of community distribution functions
*******************************************
.. code:: python

    def community_distribution_power_law() -> 'list[int]':
        """ returns a community size distribution in a list

        In this example a power law distribution according to default parameters is returned. User is free to code it's own
        distribution.

        :return: list of community sizes

Sample of node distribution function
************************************
.. code:: python

    def node_distribution_power_law(community_sizes: 'list[int]', retries) -> 'list[int],list[int]':
        """
        returns two node degree distributions: total  and INTRA

        to generate feasible distributions there should not be a skew towards large and small degrees (bathtub)
        maximum degree should be substantially lower than community size???
        :param community_sizes: Community sizes distribution
        :param retries:  retry number if previous sequence non graphic

        :return: lists of total and INTRA node degrees


Parameters for user supplied functions examples
***********************************************
.. parsed-literal::

    community_distribution samples parameters:
	community_distribution_power_law
	desired_number_of_nodes.........................................500
	delta (power exponent)..........................................1.5
	max_community_sizes.............................................300
	min_community_sizes.............................................20

	community_distribution_exponential
	desired_number_of_nodes.........................................500
	beta (scale parameter and mean).................................1
	max_community_sizes.............................................300
	min_community_sizes.............................................20

	community_distribution_random
	desired_number_of_nodes.........................................500
	max_community_sizes.............................................300
	min_community_sizes.............................................20


    node_distribution samples parameters:
	node_distribution_power_law
	mix_ratio (intra to total) .....................................0.7
	fixed (or bernoulli)............................................False
	gamma (power exponent)..........................................2.5
	max_degree......................................................40
	min_degree......................................................8

	node_distribution_exponential
	mix_ratio (intra to total) .....................................0.7
	fixed (or bernoulli)............................................False
	gamma(power exponent)...........................................4
	max_degree......................................................40
	min_degree......................................................8

	node_distribution_random
	pkk (probability of intra link).................................0.2
	pkn (probability of inter link).................................0.002
	fixed (or bernoulli)............................................False
	mix_ratio (intra to total)......................................0.7

