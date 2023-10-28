import datetime
import csv
from truck import Truck
from package import Package
from hashmap import Hashmap
from driver import Driver

def main():
    drivers = []
    trucks = []
    packages = []

    # initialize trucks
    # per business requirements, there are 3 trucks
    for i in range(0, 3):
        temp_truck = Truck([], None, None, None, None)
        trucks.append(temp_truck)

    # initialize drivers
    # per business requirements, there are two drivers
    for i in range(0, 2):
        drivers.append(Driver(None))

    # initialize packages and store in hash table by parsing CSV file
    with open('/Users/tylerhampton/Desktop/WGU/wgu_c950/csv/packages.csv') as packages_csv:
        csv_reader = csv.reader(packages_csv, delimiter = ',')
        for row in csv_reader:
            
            ID = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = int(row[4])
            deadline = row[5]
            weight = float(row[6])
            notes = row[7]
            status = "At Hub"

            packages.append(Package(ID, address, city, state, zip_code, deadline, weight, notes, status))

    print(len(drivers))
    print(len(packages))

    print(trucks[1].__str__())
    print(packages[1].__str__())

    # load the trucks with the packages
    temp = 0
    for truck in trucks:
        if temp + 16 > len(packages):
            truck.packages = packages[temp:]
            break
        else:
            truck.packages = packages[temp:temp + 16]
        temp += 16

    print(len(trucks[2].packages))

if __name__ == "__main__":
    main()


