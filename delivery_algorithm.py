# delivery algorithm
# Dijkstra's algorithm?

class Vertex:
    def __init__(self, v_address, vertices = []) -> None:
        self.v_address = v_address
        self.vertices = vertices

def deliver_pkgs(truck, pkg_hashmap):
    delivery_queue = []
    for pkg in truck.packages:
        cur_pkg = pkg_hashmap.get_item(pkg)
        cur_pkg.status = "enroute"
        delivery_queue.append(cur_pkg)
    
    for pkg in delivery_queue:
        print(pkg.status)

def deliver_pkgs_dijkstra(start_v):
    # for each vertex cur_v in graph:
        # cur_v.distance = infinity
        # cur_v.pred_v = 0
        # enqueue cur_v in unvisited_queue
    
    # while unvisited_queue not None:
        # visit vertex with minimum distance from start_v
        # cur_v  = dequeue_min univisited_queue

        # for each vertex adj_v adjacent to cur_v:
            # edge_weight = weight of edge from cur_v to adj_v
            # alternate_path_distance = cur_v.distance + edge_weight

            # if shorter path from start_v to adj_v is found, update adj_v.distance and predecessor
            # if (alternate_path_distance < adj_v.distance):
                # adj_v.distance = alternate_path_distance
                # adj_v.pred_v = cur_v
    
    return None


# find shortest path from hub to node a to all other nodes to find shortest point from a to next node in list. Next shortest node will be xfj
# repeat until all are visisted

# if 