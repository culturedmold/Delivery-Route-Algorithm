import datetime
from delivery_algorithm import run_delivery_algorithm
from truck import Truck
import hashmap
from delivery_graph import Address_Adj_Matrix

trucks = []
packages = []
pkg_hashmap = hashmap.Hashmap()
address_adj_matrix = Address_Adj_Matrix("csv/addresses.csv", "csv/distances.csv")

# main program and user interface
def main():
    # upon startup, ask user if they'd like to run the program or quit
    command = input("Welcome! Press any key to run the program, or enter Q to quit: ")

    while command != "Q":
        if command != "R":
            command = input("Not a valid command. Please enter R to run program, or Q to quit: ")
        else:
            trucks.append(Truck(None, None, datetime.timedelta(hours = 8)))
            trucks.append(Truck(None, None, datetime.timedelta(hours = 9, minutes = 5)))
            trucks.append(Truck(None, None, datetime.timedelta(hours = 12))) # after multiple simulations, it was determined that truck three should always be able to depart earlier than 12pm. An improvement would be to handle this aspect programatically and set the departure_time of the final truck to be the time of whatever previous truck returns to the hub first.

            # load the hashmap of packages (pkg_hashmap)
            hashmap.create_pkg_hashmap("csv/packages.csv", pkg_hashmap)

            # LOAD THE TRUCKS
            # trucks loaded manually based on the following parameters:
                # if notes specify packages needed to go on a certain truck, those packages were loaded first
                # if notes specify packages needed to be delivered together, those packages were grouped together
                # remaining packages were loaded based on zip code - packages in the same zip code were loaded onto the same truck unless 
            trucks[0].packages = [30,13,10,2,7,29,33,24,1,19,20,40,14,15,16,34] # packages with early deadline by zip code
            trucks[1].packages = [3,8,27,35,39,5,37,38,25,6,12,17,31,36,22,18] # late packages grouped by zip code; other packages with truck 2 requirement
            trucks[2].packages = [9,4,21,28,26,11,23,32] # remaining no-deadline packages and packages with wrong addresses

            run_delivery_algorithm(trucks[0], pkg_hashmap, address_adj_matrix)
            run_delivery_algorithm(trucks[1], pkg_hashmap, address_adj_matrix)

            # update address of package 9 before it departs from the hub
            # address given to WGU at 10:20am, trucks[3] departs form the hub at 12pm
            pkg_hashmap.get_item(trucks[2].packages[0]).address = "410 S State St"
            pkg_hashmap.get_item(trucks[2].packages[0]).city = "Salt Lake City"
            pkg_hashmap.get_item(trucks[2].packages[0]).state = "UT"
            pkg_hashmap.get_item(trucks[2].packages[0]).zip = 84111

            run_delivery_algorithm(trucks[2], pkg_hashmap, address_adj_matrix)
            
            total_miles_traveled = 0 # sum of miles traveled from all trucks

            for truck in trucks:
                total_miles_traveled += truck.miles_traveled

            print(total_miles_traveled)

            for pkg in trucks[2].packages:

                print(pkg_hashmap.get_item(pkg).delivery_time)

            # request user input after running program to determine if they'd like to run again or quit
            command = input("Enter Q to quit, R to run again: ")

    print("Closing program.")


if __name__ == "__main__":
    main()
    
