# Cory Hampton - Student ID: 010739720
# WGU_C950 - Data Structures and Algorithms II

import datetime
from delivery_algorithm import *
from truck import Truck
from hashmap import Hashmap
from delivery_graph import Address_Adj_Matrix

trucks = [] # all trucks that need to run through the delivery algorithm
packages = [] # all packages to be delivered
pkg_hashmap = Hashmap() # hashmap of packages. Call .get_item(pkg_ID) on the hashmap to lookup a package
address_adj_matrix = Address_Adj_Matrix("csv/addresses.csv", "csv/distances.csv") # delivery addresses

# main program and user interface
def main():
    # initialize our array of trucks
    trucks.append(Truck(1, None, datetime.timedelta(hours = 8))) # delivery can start at 8am. This truck does not contain any packages that arrive late or have other constraints beyond early delivery deadlines. 
    trucks.append(Truck(2, None, datetime.timedelta(hours = 9, minutes = 5))) # this truck contains packages that arrive late, so it does not depart at 8am
    trucks.append(Truck(3, None, datetime.timedelta(hours = 12))) # after multiple simulations, it was determined that truck three should always be able to depart earlier than 12pm. An improvement would be to handle this aspect programatically and set the departure_time of the final truck to be the time of whatever previous truck returns to the hub first.

    # load the hashmap of packages (pkg_hashmap)
    pkg_hashmap.create_pkg_hashmap("csv/packages.csv")

    # LOAD THE TRUCKS
    # trucks loaded manually based on the following parameters:
        # if notes specify packages needed to go on a certain truck, those packages were loaded first
        # if notes specify packages needed to be delivered together, those packages were grouped together
        # remaining packages were loaded based on zip code - packages in the same zip code were loaded onto the same truck unless 
    trucks[0].packages = [30,13,10,2,7,29,33,24,1,19,20,40,14,15,16,34] # packages with early deadline by zip code
    trucks[1].packages = [3,8,27,35,39,5,37,38,25,6,12,17,31,36,22,18] # late packages grouped by zip code; other packages with truck 2 requirement
    trucks[2].packages = [9,4,21,28,26,11,23,32] # remaining no-deadline packages and packages with wrong addresses

    # run function to find the optimal starting vertex for each truck route
    # NEEDS MORE OPTIMIZATION TO ACCOUNT FOR DEADLINES, but works for now
    optimal_start_v_truck1 = find_optimal_route(trucks[0], pkg_hashmap, address_adj_matrix)
    optimal_start_v_truck2 = find_optimal_route(trucks[1], pkg_hashmap, address_adj_matrix)

    # run delivery algorithm on trucks[0] and trucks[1]
    delivery_algorithm(trucks[0], pkg_hashmap, address_adj_matrix, optimal_start_v_truck1)
    delivery_algorithm(trucks[1], pkg_hashmap, address_adj_matrix, optimal_start_v_truck2)

    # update address of package 9 before it departs from the hub
    # address given to WGU at 10:20am, trucks[2] departs form the hub at 12pm
    # doing this programatically would be a great upgrade to improve program functionality, but is outside the scope of the current project
    pkg_hashmap.get_item(trucks[2].packages[0]).address = "410 S State St"
    pkg_hashmap.get_item(trucks[2].packages[0]).city = "Salt Lake City"
    pkg_hashmap.get_item(trucks[2].packages[0]).state = "UT"
    pkg_hashmap.get_item(trucks[2].packages[0]).zip = 84111

    # run delivery algorithm on trucks[2]
    optimal_start_v_truck3 = find_optimal_route(trucks[2], pkg_hashmap, address_adj_matrix)
    delivery_algorithm(trucks[2], pkg_hashmap, address_adj_matrix, optimal_start_v_truck3)

    # calculate total miles traveled for all trucks
    total_miles_traveled = 0 

    for truck in trucks:
        total_miles_traveled += truck.miles_traveled

    # MAIN USER INTERFACE
    print("\n")
    print("--------------------WGUPS DELIVERY SYSTEM--------------------\n")
    # upon startup, ask user if they'd like to run the program or quit
    command = input("Welcome! Type any key and press 'Enter' to run the program, or enter Q to quit: ")
    print("\n")

    # prompt user to run the program with "R" or quit with "Q"
    while command != "Q":
            print("TOTAL MILES ACROSS ALL ROUTES: %s miles" % (total_miles_traveled))

            # display of menu to the user and get their command
            # allow user to view one package, packages on a certain truck, or all packages
            num_pkgs_command = input("Enter 1 to view status of a single package, 2 for all packages on a certain truck, 3 for all packages on all trucks, or Q to quit: ")

            # allow the user to quit the program
            if num_pkgs_command == "Q":
                print("Closing program")
                return
            
            else:
                print("Please enter a time of day (24 hour clock).")
                hours_command = input("Hours: ")
                minutes_command = input("Minutes: ")

                user_timestamp = datetime.timedelta(hours = float(hours_command), minutes = float(minutes_command))

                if num_pkgs_command == '1':
                    print("\n")
                    pkg_ID_command = input("Please enter a package ID: ")
                    pkg_to_display = pkg_hashmap.get_item(int(pkg_ID_command))
                    if pkg_to_display == None:
                        print("Package not found.")
                    else:
                        print("---------Package %s at %s----------" % (pkg_ID_command, user_timestamp))
                        print(pkg_to_display.__str__())
                        print("\n")

                elif num_pkgs_command == '2':
                    print("\n")
                    truck_command = input("Please enter a truck (1-3): ")
                    print("\n")

                    if int(truck_command) > 3 or int(truck_command) < 1:
                        print("Truck not found")
                    else:
                        print("----------Status of all packages on truck %s at %s----------" % (truck_command, user_timestamp))
                        print("\n")
                        print("Miles traveled by truck %s: %s\n" % (truck_command, trucks[int(truck_command) - 1].miles_traveled))

                        for pkg in trucks[int(truck_command) - 1].packages:
                            pkg_to_display = pkg_hashmap.get_item(pkg)
                            set_status_by_time(pkg_to_display, user_timestamp)
                            print(pkg_to_display.__str__())
                    print("\n")

                elif num_pkgs_command == '3':
                    for truck in trucks:
                        print(truck.__str__())
                        print("Status of packages on truck at time %s\n" % (user_timestamp))
                        for pkg in truck.packages:
                            pkg_to_display = pkg_hashmap.get_item(pkg)
                            set_status_by_time(pkg_to_display, user_timestamp)
                            print(pkg_to_display.__str__())

                # request user input after running program to determine if they'd like to run again or quit
                command = input("Enter Q to quit, or enter R to run again: ")
                print("\n")

    print("Closing program")

if __name__ == "__main__":
    main()
    
