import csv

# package class
class Package:
    def __init__(self, ID, address, city, state, zip_code, deadline, weight, notes, status = "At Hub") -> None:
        # each ID must be unique
        self.ID = ID

        # delivery address of the package
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

        # delivery deadline
        self.deadline = deadline

        # package weight (kg)
        self.weight = weight

        # notes parsed from CSV
        self.notes = notes
        if self.notes == '':
            self.notes = None

        # at hub, enroute, delivered
        self.status = status

        # set departure_time and delivery_time as null initially
        self.departure_time = None # will be updated by the truck when the truck leaves the hub per delivery algorithm
        self.delivery_time = None # will be updated by the truck when the package is delivered per delivery algorithm

    # method will take a time input (provided by user in main function) and compare it against the departure time and delivery time of the packages
    def get_status_by_time(self, timestamp): 
        if self.delivery_time <= timestamp: # if delivery_time is less than or equal to time parameter, then the package has been delivered
            self.status = "Delivered"
        elif self.departure_time > timestamp: # if the departure_time is greater than the time passed as parameter, then the package is "Enroute". This case is only called if delivery_time !<= timestamp
            self.status = "Enroute"
        else: 
            self.status = "At Hub"

    def __str__(self) -> str:
        return "ID %s, Status %s, Address %s %s %s %s, Deadline %s, Weight %s, Notes %s, Status %s, Departure Time %s, Delivery Time %s" % (self.ID, self.status, self.address, self.city, self.state, self.zip_code, self.deadline, self.weight, self.notes, self.status, self.departure_time, self.delivery_time)

# # create a hashmap of packages from CSV  
# def create_pkg_hashmap(filename, pkg_hashmap):
#     with open(filename) as packages_csv:
#         csv_reader = csv.reader(packages_csv, delimiter = ',')

#         # loop through csv and and turn each row into a package object
#         # load each package object into hashmap
#         for row in csv_reader:
#             # temporary variables to ease initialization of package object from csv row
#             ID = int(row[0])
#             address = row[1]
#             city = row[2]
#             state = row[3]
#             zip_code = int(row[4])
#             deadline = row[5]
#             weight = float(row[6])
#             notes = row[7]
#             status = "At Hub"

#             # package to load into hashmap
#             new_package = Package(ID, address, city, state, zip_code, deadline, weight, notes, status)
#             # load object into hashmap
#             pkg_hashmap.insert(ID, new_package)