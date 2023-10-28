class Truck:
    def __init__(self, packages, status, miles_traveled, hub_address, depart_time) -> None:
        # max 16 packages on truck - array of packages
        # if more than 16 packages are in the truck, they will be removed
        self.packages = packages
        if len(packages) > 16:
            packages = packages[:16]
            print("More than 16 packages loaded on truck. Only first 16 will be kept.")

        # status: ready, driving, done
        self.status = status

        # when initialized, the truck will have traveled 0 miles
        self.miles_traveled = miles_traveled

        self.hub_address = hub_address
        self.depart_time = depart_time

    def __str__(self) -> str:
        return "Packages %s, Status %s, Mileage %s, Hub Address %s, Depart Time %s" % (self.packages, self.status, self.miles_traveled, self.hub_address, self.depart_time)