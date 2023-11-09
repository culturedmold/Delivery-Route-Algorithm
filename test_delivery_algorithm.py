import unittest
import delivery_algorithm
from truck import Truck
import datetime
from hashmap import Hashmap
from delivery_graph import Address_Adj_Matrix

# Test variables
truck1 = Truck(3, [1,2,3,4,5,6,7,8,9,10], datetime.timedelta(hours=9, minutes=0))
truck2 = Truck(5, [66,77,88], datetime.timedelta(hours=10, minutes=10)) # test invalid package IDs
truck3 = Truck(9, [6], datetime.timedelta(hours=11, minutes=9)) # test single package
bad_truck = Truck(10, [9], datetime.timedelta(hours=1, minutes=1))

pkg_hashmap = Hashmap()
pkg_hashmap.create_pkg_hashmap("csv/packages.csv")
address_matrix = Address_Adj_Matrix("csv/addresses.csv", "csv/distances.csv")

start_address = address_matrix.address_matrix[0][1]
invalid_start_address = "hello"

class Test_Delivery_Algorithm(unittest.TestCase):

    def test_delivery_algorithm(self):
        self.assertEqual(delivery_algorithm.delivery_algorithm(truck1, pkg_hashmap, address_matrix, truck1.packages[1]), truck1.packages)
        self.assertIsNone(delivery_algorithm.delivery_algorithm(truck2, pkg_hashmap, address_matrix, 1), truck2.packages[1])
        self.assertEqual(delivery_algorithm.delivery_algorithm(truck3, pkg_hashmap, address_matrix, truck3.packages[0]), truck3.packages)

    def test_find_optimal_route(self):
        self.assertNotEqual(delivery_algorithm.find_optimal_route(truck1, pkg_hashmap, address_matrix), 0)

    

if __name__ == "__main__":
    unittest.main()