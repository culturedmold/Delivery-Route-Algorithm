# driver
# only 2 drivers will exist at a time per business requirement
class Driver:
    def __init__(self, truck) -> None:
        self.truck = truck
        self.occupied = None

        