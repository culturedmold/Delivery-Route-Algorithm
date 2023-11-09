import datetime

# delivery algorithm
# find optimal path using nearest neighbor approach
# take truck, pkg_hashmap, address_adj_matrix as arguments

# TIME COMPLEXITY
# O(N^2)
def delivery_algorithm(truck, pkg_hashmap, address_adj_matrix, starting_package):
    truck.miles_traveled = float(0)
    truck.cur_time = truck.departure_time

    unvisited_list = [] # initialize unvisited_list
        
    for pkg_ID in truck.packages: # all packages in list from truck are added to unvisited list
            
        pkg_hashmap.get_item(pkg_ID).status = "Enroute" # update package status to reflect current delivery status
        pkg_hashmap.get_item(pkg_ID).departure_time = truck.departure_time # set package departure time to match departure time of the truck (when the package departed hub and status become "Enroute")

        unvisited_list.append(pkg_hashmap.get_item(pkg_ID)) # use ID from truck packages list to get the corresponding package object from pkg_hashmap

    # cur_pkg is set to hub initially
    starting_package = pkg_hashmap.get_item(starting_package)
    cur_pkg = starting_package.address

    truck.miles_traveled += address_adj_matrix.get_distance_between(cur_pkg, address_adj_matrix.address_matrix[0][1])
    truck.cur_time += datetime.timedelta(hours = truck.miles_traveled / 18)
    starting_package.delivery_time = truck.cur_time
    # unvisited_list.remove(starting_package)

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

    return truck.miles_traveled

# TIME COMPLEXITY
# O(1)
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

# call this function to determine the most optimal route using our delivery algorithm
# this function runs through all packages on a trucks route and uses our delivery algorithm defined elsewhere to determine the best possible starting address from the list of packages to be delivered on the truck
# TIME COMPLEXITY
# O(N^3)
def find_optimal_route(truck, pkg_hashmap, address_adj_matrix):

    possible_route_starting_v_list = []
    earliest_deadline = datetime.timedelta(hours=23, minutes=59)

    first_package = None

    for pkg in truck.packages:
        if pkg_hashmap.get_item(pkg).deadline != "EOD":
            # deliver the delayed packages first to ensure deadlines are met
            # return the first found delayed package
            if pkg_hashmap.get_item(pkg).notes == "Delayed on flight---will not arrive to depot until 9:05 am":
                return pkg
            
            # get the earliest deadline of all packages
            pkg_deadline = pkg_hashmap.get_item(pkg).deadline
            if pkg_deadline < earliest_deadline:
                earliest_deadline = pkg_deadline
                # print("Earliest Deadline:" + str(earliest_deadline))
                first_package = pkg

        else:
            truck.cur_time = truck.departure_time
            cur_mileage = delivery_algorithm(truck, pkg_hashmap, address_adj_matrix, pkg)
            temp = [pkg, cur_mileage] 
            possible_route_starting_v_list.append(temp)

    # if we have identified a package with an early deadline, return that package as the package we need to start with for deliveries
    if first_package is not None:
        # print(pkg_hashmap.get_item(first_package).deadline)
        return first_package
    
    best_start = possible_route_starting_v_list[0][0]
    smallest_dist = possible_route_starting_v_list[0][1]

    for k in possible_route_starting_v_list:
        if k[1] < smallest_dist:
            best_start = k[0]
            smallest_dist = k[1]
    
    return best_start

