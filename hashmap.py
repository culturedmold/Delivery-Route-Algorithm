class Hashmap:
    def __init__(self, initial_size = 16) -> None:
        # initial value 16 since that is the size of an empty truck
        self.list = []
        for i in range(initial_size):
            self.list.append([])
        
    def insert(self, key, item):
        bucket = hash(key) % len(self.list) # bucket is key modulo list size
        bucket_elements = self.list[bucket] # bucket elements are the key value pairs stored in the list[bucket] subarray

        # update existing entry if exists
        for key_value_pair in bucket_elements:
            print(key_value_pair)
            if key_value_pair[0] == key:
                key_value_pair[1] = item
                return
        
        # add key value pair to buck if not already there
        key_value_pair = [key, item]
        bucket_elements.append(key_value_pair)
        return
    
    # return an item from the hashmap if it exists
    def get_item(self, key):
        bucket = hash(key) % len(self.list)
        bucket_elements = self.list[bucket]

        # check if key value pair exists in the bucket and return it
        for key_value_pair in bucket_elements:
            if key_value_pair[0] == key:
                return key_value_pair[1]
            
        return None # if not found, return none

    def get_size(self):
        return len(self.list)