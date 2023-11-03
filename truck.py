# truck
class Truck:
    def __init__(self, ID, packages, departure_time = None, miles_traveled = float(0)) -> None:
        self.ID = ID
        # max 16 packages on truck - array of packages
        # if more than 16 packages are in the truck, they will be removed
        self.packages = packages

        # when initialized, the truck will have traveled 0 miles
        self.miles_traveled = miles_traveled
        self.departure_time = departure_time
        self.cur_time = departure_time

        # avg speed of all trucks is 18
        self.avg_speed = 18

    def __str__(self) -> str:
        truck_str = "----------Truck ID: %s----------\nPackages on Truck: %s\nMiles Traveled on Route: %s\nDepart Time: %s\nRoute Completion Time: %s\n" % (self.ID, self.packages, self.miles_traveled, self.departure_time, self.cur_time)

        return truck_str