import datetime
import csv
from delivery_algorithm import deliver_pkgs
from truck import Truck
from package import Package
from hashmap import Hashmap
from driver import Driver

drivers = []
trucks = []
packages = []
pkg_hashmap = Hashmap()

# function to load packages into the hashmap
def create_pkg_hashmap(filename, pkg_hashmap):
    with open(filename) as packages_csv:
        csv_reader = csv.reader(packages_csv, delimiter = ',')

        # loop through csv and and turn each row into a package object
        # load each package object into hashmap
        for row in csv_reader:
            # temporary variables to ease initialization of package object from csv row
            ID = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = int(row[4])
            deadline = row[5]
            weight = float(row[6])
            notes = row[7]
            status = "At Hub"

            # package to load into hashmap
            new_package = Package(ID, address, city, state, zip_code, deadline, weight, notes, status)
            # load object into hashmap
            pkg_hashmap.insert(ID, new_package)

    
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
            create_pkg_hashmap("/Users/tylerhampton/Desktop/WGU/wgu_c950/csv/packages.csv", pkg_hashmap)
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
    
