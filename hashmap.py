# chaining hash table
class Hashmap:
    def __init__(self, initial_capacity=16) -> None:
        self.list = []
        # initialize the list with 16 empty buckets
        # 16 was chosen because that is the max capacity of a delivery truck
        for i in range(initial_capacity):
            self.list.append([])

    # CITING SOURCE: WGU - c950 Webinar 1 - Let's Go Hashing 
    # Source Link: https://srm--c.vf.force.com/apex/CourseArticle?id=kA03x000000e1fuCAA
    def insert(self, key, item):
        bucket = hash(key) % len(self.list) # determine bucket based on key mod (length of list)
        bucket_list = self.list[bucket] # bucket_list is a 2d array of key_value pairs in the bucket

        # UPDATE KEY VALUE PAIR IF ALREADY IN BUCKET
        # key value pair takes form of [key (package ID), package object]
        # search the bucket list at index 0 for all kv in the list
        # if we find the key at kv[0], we update k[1] with the new item (a package object)
        for kv in bucket_list:
            # print(kv)
            if kv[0] == key:
                kv[1] = item
                return
            
        # add key_value to the bucket list if not already there
        key_value = [key, item] # key value pair to add to put into bucket
        bucket_list.append(key_value)
        return
    
    def get_package(self, key):
        # use the key to find the bucket to search
        # bucket is hash(key) modulo (length of list)
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket] # bucket_list is a 2d array of key_value pairs in th ebucket

        # key value pair takes form of [key (package ID), package object]
        # search the bucket list at index 0 for all kv in the list
        # if we find the key at kv[0], we return the associated package object kv[1]
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1] # return the package associated with the key
            
        return None # not found in bucket

    def get_size(self):
        return len(self.list)
    