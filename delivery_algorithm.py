# delivery algorithm
# Dijkstra's algorithm

def deliver_pkgs(truck, pkg_hashmap):
    delivery_queue = []
    for pkg in truck.packages:
        cur_pkg = pkg_hashmap.get_item(pkg)
        cur_pkg.status = "enroute"
        delivery_queue.append(cur_pkg)
    
    for pkg in delivery_queue:
        print(pkg.status)