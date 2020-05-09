import csv, ast


class ReadData:
    """
    must code a method "return_single_node" that returns:
    time slice (int)
    node number (int)
    community_number (int)
    example below, reading a node csv file in gephi format
    """
    temp_communities = []  # list of tuples (time, node, community)
    start = True
    current_node = 0

    @staticmethod
    def load_gephi():
        ReadData.temp_communities = []
        ReadData.current_node = 0
        with open("graphnodes.csv") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=';')
            next(csv_reader)        # skip header
            for row in csv_reader:
                node = int(row[0])
                list_comms = ast.literal_eval(row[2].replace('<', '[').replace('>', ']'))
                [ReadData.temp_communities.append((int(entry[0]), node, int(entry[1]))) for entry in list_comms]
        ReadData.temp_communities.sort(key=lambda x: x[0])

        # print(ReadData.time_slice, full_list)

    @staticmethod
    def return_single_node():
        if ReadData.start:
            ReadData.load_gephi()
        ReadData.start = False
        if ReadData.current_node < len(ReadData.temp_communities):
            ts, node_number, comm_number = ReadData.temp_communities[ReadData.current_node]
            ReadData.current_node += 1
            return False, ts, node_number, comm_number
        return True, None, None, None           # end of file