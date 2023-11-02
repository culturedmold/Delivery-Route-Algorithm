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

    def __str__(self) -> str:
        return "ID %s, Status %s, Address %s %s %s %s, Deadline %s, Weight %s, Notes %s, Status %s, Departure Time %s, Delivery Time %s" % (self.ID, self.status, self.address, self.city, self.state, self.zip_code, self.deadline, self.weight, self.notes, self.status, self.departure_time, self.delivery_time)
