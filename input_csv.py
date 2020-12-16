class ReadData:
    list_node_community = []
    node_number = 0
    time_slice = 0
    file = ""
    start = True

    @staticmethod
    def read_snapshot():
        full_list = ReadData.file.readline()
        if not full_list:
            ReadData.list_node_community = []
            return
        ReadData.list_node_community = full_list.split(',')
        ReadData.time_slice += 1
        ReadData.node_number = 0
        # print(FootballData.time_slice, full_list)

    @staticmethod
    def return_single_node():
        if ReadData.start:
            ReadData.file = open("football.csv")
            ReadData.start = False
        if not ReadData.list_node_community:
            ReadData.read_snapshot()
        if not ReadData.list_node_community:
            return True, None, None, None           # end of file
        else:
            node_available = False
            while not node_available:
                node_available = True
                ReadData.node_number += 1
                try:
                    community = int(ReadData.list_node_community.pop(0))
                except ValueError:
                    node_available = False
                if node_available:
                    return False, ReadData.time_slice, ReadData.node_number, \
                           community
                else:
                    if not ReadData.list_node_community:
                        ReadData.read_snapshot()
                    if not ReadData.list_node_community:
                        return True, None, None, None  # end of file
