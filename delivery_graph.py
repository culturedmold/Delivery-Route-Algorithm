import csv

# initialize delivery graph from 
with open("csv/distances.csv") as distances_csv:
    distance_graph = csv.reader(distances_csv)
    distance_graph = list(distance_graph)

# find distance between two nodes
def get_distance_between(x, y):
    distance = distance_graph[x][y]
    if distance == '':
        distance = distance_graph[y][x]
    
    return float(distance)

# fix distances for empty cells in csv
def fix_distances(graph):
    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            if graph[i][j] == '':
                graph[i][j] = graph[j][i]

fix_distances(distance_graph)

# get addresses into a matrix of [name, street_address] for each
with open("csv/addresses.csv") as addresses_csv:
    csv_reader = csv.reader(addresses_csv, delimiter = ',')
    addresses = []
    for row in csv_reader:
        name = row[0]
        street_address = row[1]

        temp = [name, street_address]

        addresses.append(temp)


# get address from addresses hashmap
def get_address_index(address, addresses_hashmap):
    if address in addresses_hashmap.keys():
        return list(addresses_hashmap).index(address)

# create a hashmap of address : distance
def create_address_hashmap(distance_graph):
    addresses_hashmap = dict()
    for i in range(0, len(distance_graph)):
        addresses_hashmap[addresses[i][1]] = distance_graph[i]
    
    return addresses_hashmap

address_hashmap = create_address_hashmap(distance_graph)

print(get_address_index("2835 Main St", address_hashmap))

print(get_distance_between(get_address_index("2835 Main St", address_hashmap), get_address_index("2835 Main St", address_hashmap)))