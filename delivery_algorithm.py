import datetime

# delivery algorithm
# find optimal path using nearest neighbor approach
# take truck, pkg_hashmap, address_adj_matrix as arguments
def run_delivery_algorithm(truck, pkg_hashmap, address_adj_matrix):
    unvisited_list = [] # initialize unvisited_list
        
    for pkg_ID in truck.packages: # all packages in list from truck are added to unvisited list
            
        pkg_hashmap.get_item(pkg_ID).status = "Enroute" # update package status to reflect current delivery status
        pkg_hashmap.get_item(pkg_ID).departure_time = truck.departure_time # set package departure time to match departure time of the truck (when the package departed hub and status become "Enroute")

        unvisited_list.append(pkg_hashmap.get_item(pkg_ID)) # use ID from truck packages list to get the corresponding package object from pkg_hashmap

    # cur_pkg is set to hub initially
    cur_pkg = address_adj_matrix.address_matrix[0][1]

    # WHILE LOOP - run until unvisited_list is empty
    while len(unvisited_list) > 0:
        min_distance = float('inf')
        next_location = None

        # calculate distance between final package delivered and hub
        # this will include travel distance back to hub after all packages have been delivered
        # calculating the return distance to the hub is technically not a constraint imposed by the project requirements, but it doesn't make any logical sense to NOT calculate that distance unless the delivery business intends for the driver to take the truck home at the end of each day
        if len(unvisited_list) == 1:
            truck.miles_traveled += address_adj_matrix.get_distance_between(address_adj_matrix.address_matrix[0][1], unvisited_list[0].address)

            # print(address_adj_matrix.get_distance_between(address_adj_matrix.address_matrix[0][1], unvisited_list[0].address))

        # FOR LOOP - iterate through all packages in unvisited list to find the package with the closest address to cur_pkg
        for pkg in unvisited_list:
            if address_adj_matrix.get_distance_between(pkg.address, cur_pkg) < min_distance:
                min_distance = address_adj_matrix.get_distance_between(pkg.address, cur_pkg) # set min_distance to the minimum distance of cur_pkg and pkg.address
                next_location = pkg

        cur_pkg = next_location.address # next_location is used to set cur_pkg.address - this will be put into the get_distance_between method to find the distance between cur_package and the next package in unvisited_list

        next_location.status = "Delivered" # update pkg status after it's been "delivered"
            
        truck.cur_time += datetime.timedelta(hours = min_distance / truck.avg_speed) # update current time of the truck at the point of each delivery

        next_location.delivery_time = truck.cur_time # update package delivery time to match the time the truck delivered the package

        unvisited_list.remove(next_location) # when an item is removed from the unvisited list, it has been "delivered"

        truck.miles_traveled += min_distance # update distance traveled by the truck along the delivery route

    return

# function will take a time input (provided by user in main function) and compare it against the departure time and delivery time of the packages determined by the delivery algorithm
def set_status_by_time(pkg, timestamp):
    pkg_status_at_time = None
    if pkg.delivery_time <= timestamp: # if delivery_time is less than or equal to time parameter, then the package has been delivered
        pkg_status_at_time = "Delivered"
    elif pkg.departure_time < timestamp: # if the departure_time is less than the time passed as parameter, then the package is "Enroute". This case is only called if delivery_time !<= timestamp
        pkg_status_at_time = "Enroute"
    else: 
        pkg_status_at_time = "At Hub"

    pkg.status = pkg_status_at_time
    return pkg.status

