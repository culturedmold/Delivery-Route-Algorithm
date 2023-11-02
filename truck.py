# truck
class Truck:
    def __init__(self, packages, status, departure_time, miles_traveled = float(0)) -> None:
        # max 16 packages on truck - array of packages
        # if more than 16 packages are in the truck, they will be removed
        self.packages = packages

        # status: ready, driving, done
        self.status = status

        # when initialized, the truck will have traveled 0 miles
        self.miles_traveled = miles_traveled
        self.departure_time = departure_time
        self.cur_time = departure_time

        # avg speed of all trucks is 18
        self.avg_speed = 18

    def __str__(self) -> str:
        return "Packages %s, Status %s, Mileage %s, Hub Address %s, Depart Time %s" % (self.packages, self.status, self.miles_traveled, self.hub_address, self.depart_time)