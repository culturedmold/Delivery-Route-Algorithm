import datetime
from delivery_algorithm import deliver_pkgs
from truck import Truck
from package import Package
from package import create_pkg_hashmap
from hashmap import Hashmap
from driver import Driver

drivers = []
trucks = []
packages = []
pkg_hashmap = Hashmap()

    
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
            create_pkg_hashmap("csv/packages.csv", pkg_hashmap)
            print(pkg_hashmap.get_size())

            print(pkg_hashmap.get_item(12))

            # load the trucks

            trucks[0].packages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

            deliver_pkgs(trucks[0], pkg_hashmap)

            # print(pkg_hashmap.return_item(trucks[0].packages[1]))

            # request user input after running program to determine if they'd like to run again or quit
            command = input("Enter Q to quit, R to run again. ")
        
    print("Closing program.")


if __name__ == "__main__":
    main()
    
