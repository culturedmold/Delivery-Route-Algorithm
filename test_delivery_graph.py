import delivery_graph
import unittest

# Test variables
address_matrix = delivery_graph.Address_Adj_Matrix("csv/addresses.csv", "csv/distances.csv")

class Test_Delivery_Graph(unittest.TestCase):
    def test_get_distance_between(self):
        self.assertIsNone(address_matrix.get_distance_between("hello", "hello"), None)
        self.assertIsNone(address_matrix.get_address_index("hello"), None)

if __name__ == "__main__":
    unittest.main()