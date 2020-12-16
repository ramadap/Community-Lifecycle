*******************************************************************************************************
Taxonomy: Community-Lifecycle, Code to analyse a temporal network and output community lifecycle events
*******************************************************************************************************

Description
#############
Please refer to "Community identity in a temporal network: A taxonomy proposal", Pereira et al., on Ecological Complexity, in press. https://ciencia.iscte-iul.pt/publications/community-identity-in-a-temporal-network-a-taxonomy-proposal/77648
or to "A Taxonomy of Community Lifecycle Events in Temporal Networks", on IEEE Xplore repository https://ieeexplore.ieee.org/document/8930777/.

This python code uses various classes from "Syntgen: A synthetic temporal network generator with clustering and known ground truth" published in the IMA Journal of Complex Networks, https://doi.org/10.1093/comnet/cnz039. Syntgen code is available at https://github.com/ramadap/Syntgen

This package is a Python system to analyse a timestamped sequence of tuples containing a node and its community.
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
User should code a python module with a class ReadData that exposes a return_single_node() method that returns a boolean and a time ordered triple (timestamp, node number, community number) for every invocation. The boolean raises "True" if no more data is available, "False" otherwise. 
Two sample modules are provided, one for gephi gexf format (input_gexf) and another (input_csv) for a CSV file with one line per snapshot, where position indicates node number and the value, the community it belongs to. 


Output:
	Console text describing community events at the end and start of each timestep with additional statistics depending on parameters 


Parameters
=============

All input parameters are specified in file **user_specifications.py**
This file is shared with Syntgen, and only the two parameters included below are used in lifecycle determination. 

.. csv-table:: Behaviour parameters
   :header: "Parameter", "Description", "Default"
   :widths: 15, 100, 10

    "DEBUG",verbose output (debug),No
    "jaccard_null_model",whether to adjust the jaccard index to a null random model when comparing communities for lifecycle determination",TRUE
    "Sigma","jaccard threshold for community matching, value between [0,1] 1 requires exact matching",0.5

User defined functions
***********************

Withe the exception of the user input function, that should be specified in the file "Taxonomy.py", user defined functions are shared with Syntgen. Only the print parameters function should be changed for lifecycle determination.  

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
    exclude_continuations = True
    
