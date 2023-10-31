import datetime
from delivery_algorithm import deliver_pkgs
from truck import Truck
import hashmap
from driver import Driver
from delivery_graph import Address_Adj_Matrix

drivers = []
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
            # initialize trucks
            # per business requirements, there are 3 trucks
            for i in range(0, 3):
                new_truck = Truck([], None, None, None, None)
                trucks.append(new_truck)

            # initialize drivers
            # per business requirements, there are two drivers
            for i in range(0, 2):
                drivers.append(Driver(None))

            # load the hashmap of packages (pkg_hashmap)
            hashmap.create_pkg_hashmap("csv/packages.csv", pkg_hashmap)
            print(pkg_hashmap.get_size())

            print(pkg_hashmap.get_item(12))

            # load the trucks
            trucks[0].packages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

            deliver_pkgs(trucks[0], pkg_hashmap)

            # look up the item in the hashmap and return it, then pass the propeties as needed into functions
            temp_pkg = pkg_hashmap.get_item(trucks[0].packages[1])
            temp_pkg_2 = pkg_hashmap.get_item(trucks[0].packages[4])

            print(address_adj_matrix.get_distance_between(temp_pkg.address, temp_pkg_2.address))

            # request user input after running program to determine if they'd like to run again or quit
            command = input("Enter Q to quit, R to run again: ")


        
    print("Closing program.")


if __name__ == "__main__":
    main()
    
