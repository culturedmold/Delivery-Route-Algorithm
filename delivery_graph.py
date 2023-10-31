import csv

# address hashmap
# contains a hashmap of addresses : distances (an adjacenty matrix)
class Address_Adj_Matrix:
    def __init__(self, addresses_CSV, distances_CSV):
        self.address_matrix = self.create_addresses_matrix(addresses_CSV)
        self.distance_matrix = self.create_distances_matrix(distances_CSV)

        # initialize.address_adj_matrix
        self.address_adj_matrix = self.create_adj_matrix()


    # ADDRESSES AND DISTANCES
    # addresses (vertices) and distances (edges) are separated into separate CSV files.
    # CSV "rows" indicate which address belongs to which adjacent edges
    # example: the value at distance_matrix[address x][address y] indicates the distance (edge weights) between the two addresses (vertices)

    # create a matrix of distances
    # returns a multidimensional array of distances
    def create_distances_matrix(self, filename_CSV):
        # initialize delivery graph from 
        with open(filename_CSV) as distances_csv:
            distances = csv.reader(distances_csv)
            distances = list(distances)

            for i in range(0, len(distances)):
                for j in range(0, len(distances[i])):
                    if distances[i][j] == '':
                        distances[i][j] = distances[j][i]

        return distances
    
    # method to create addresses_list matrix
    # takes CSV filename as parameter (string) and returns list of addresses_list
    def create_addresses_matrix(self, filename_CSV):
        # get addresses_list into a matrix of [name, street_address] for each
        with open(filename_CSV) as addresses_csv:
            csv_reader = csv.reader(addresses_csv, delimiter = ',')
            addresses_list = []
            for row in csv_reader:
                name = row[0]
                street_address = row[1]

                temp = [name, street_address]

                addresses_list.append(temp)

        return addresses_list

    # fixes distances in CSV for empty cells
    def fix_distances(self, graph):
        for i in range(0, len(graph)):
            for j in range(0, len(graph[i])):
                if graph[i][j] == '':
                    graph[i][j] = graph[j][i]

    # create a hashmap of {address : distance}
    # returns a hashmap/j_matrix(self, distances_matrix):
    def create_adj_matrix(self):
        # matrix is stored as dictionary
        # address is dictionary bucket, followed by all adjacent edges
        address_adj_matrix = dict()
        for i in range(0, len(self.distance_matrix)):
            address_adj_matrix[self.address_matrix[i][1]] = self.distance_matrix[i]
        
        return address_adj_matrix
    
    # get address from address_adj_matrix
    # returns the index of the key if it exists in the hashmap
    def get_address_index(self, address):
        if address in self.address_adj_matrix.keys():
            return list(self.address_adj_matrix).index(address)
    
    # return distance between two addresses_list (vertices) and return the distances between them
    # uses the distance_matrix imported from CSV
    def get_distance_between(self, address_1, address_2):
        x = self.get_address_index(address_1)
        y = self.get_address_index(address_2)

        distance = self.distance_matrix[x][y]

        # shouldn't be needed since we "fixed" the empty cells, but here just in case
        if distance == '':
            distance = self.distance_matrix[y][x]

        return float(distance)
