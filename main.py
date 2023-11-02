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
            trucks.append(Truck(None, None, datetime.timedelta(hours = 12)))

            # load the hashmap of packages (pkg_hashmap)
            hashmap.create_pkg_hashmap("csv/packages.csv", pkg_hashmap)

            # LOAD THE TRUCKS
            # trucks loaded manually based on the following parameters:
                # if notes specify packages needed to go on a certain truck, those packages were loaded first
                # if notes specify packages needed to be delivered together, those packages were grouped together
                # remaining packages were loaded based on zip code - packages in the same zip code were loaded onto the same truck unless 
            trucks[0].packages = [30,13,10,2,7,29,33,24,1,19,20,40,14,15,16,34]
            trucks[1].packages = [3,8,27,35,39,5,37,38,25,6,12,17,31,36,22,18]
            trucks[2].packages = [9,4,21,28,26,11,23,32]

            # for truck in trucks:
            #     run_delivery_algorithm(truck, pkg_hashmap, address_adj_matrix)
            #     total_miles_traveled += truck.miles_traveled
            run_delivery_algorithm(trucks, pkg_hashmap, address_adj_matrix)
            
            total_miles_traveled = 0 # sum of miles traveled from all trucks

            for truck in trucks:
                total_miles_traveled += truck.miles_traveled

            print(total_miles_traveled)

            check_deliveries = [37,25,6,31,30,13,29,1,20,40,14,15,16,34]

            for pkg in check_deliveries:

                print(pkg_hashmap.get_item(pkg))

            # request user input after running program to determine if they'd like to run again or quit
            command = input("Enter Q to quit, R to run again: ")


    print("Closing program.")


if __name__ == "__main__":
    main()
    
