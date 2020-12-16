"""
main module: inspects a list of timed node community assignments and outputs the community lifecycles

ref: Community identity in a temporal network: A taxonomy proposal submitted to Ecological Complexity, Pereira et al
"""

from transition import match_communities, create_confusion_matrix, \
    create_continuation_matrix, find_rebirths, State, vi
from constants import *
from network import Community, Nodes
from user_specifications import sigma, jaccard_null_model
from output_v2 import printouts
from input_csv import ReadData  # read one record at a time (time stamp/ node / community)
#from input import ReadData
import numpy as np

eof, timestamp, node_number, community_name = ReadData.return_single_node()

new_communities = []
dead_communities = []
nodes = []
states = []
states_count = []

while not eof:
    time_slice_previous = timestamp
    new_communities.append([])    # initiate a new community set
    while timestamp == time_slice_previous:
        Ts.timestamp = timestamp            # Ts.timestamp global used by objects
        try:
            index = [c.community_name for c in new_communities[-1]].index(community_name)
        except ValueError:
            index = -1
            new_community = Community(0, community_name)
            new_communities[-1].append(new_community)
        new_communities[-1][index].total_nodes += 1
        exists, node, _ = Nodes.is_node(node_number)
        if not exists:
            node = Nodes(new_communities[-1][index], node_number)
        else:
            node.change_community(new_communities[-1][index])
        node.set_lifecycle()
        new_communities[-1][index].nodes.append(node)

        eof, timestamp, node_number, community_name = ReadData.return_single_node()

        # find frequent clusterings
        state_names = (';'.join(map(str, sorted([comm.community_name for comm in new_communities[-1]]))))
    try:
        states_count[states.index(state_names)] += 1
    except ValueError:
        states.append(state_names)
        states_count.append(1)

    if len(new_communities) > 1:
        # match communities
        confusion = create_confusion_matrix(new_communities[-2], new_communities[-1])
        create_continuation_matrix(confusion, sigma, jaccard_null_model)
        #   [clean_old.set.set_ground_truth(event='reset') for clean_old in new_communities[-2]]
        match_communities(new_communities[-2], new_communities[-1],
                          dead_communities, confusion)

        state_transition = State(list(confusion[:-1, :-1].sum(axis=1)), list(confusion[:-1, :-1].sum(axis=0)), vi)
        state = np.reshape(confusion[:-1, :-1],  state_transition.edges_len)
        state_transition.set_state(state)
        score = state_transition.similarity

        # find rebirths
        # for dead in dead_communities:
        candidate_communities = [communities for communities in new_communities[-1]
                                 if communities.community_events[-1][1] != "P"]
        if candidate_communities:
            dead_confusion = create_confusion_matrix(dead_communities, candidate_communities)
            save_jaccard_index_matrix = Community.jaccard_index.copy()
            save_continuation_matrix = Community.continuation.copy()
            create_continuation_matrix(dead_confusion, sigma, jaccard_null_model)
            set_dead_communities = dead_communities.copy()
            find_rebirths(set_dead_communities, candidate_communities, dead_communities)
            Community.jaccard_index = save_jaccard_index_matrix
            Community.continuation = save_continuation_matrix

        printouts(confusion, score, new_communities[-2], new_communities[-1])
