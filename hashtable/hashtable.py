class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """
    def __init__(self, capacity):
        if capacity > MIN_CAPACITY:
            self.capacity = capacity
        else: 
            self.capacity = MIN_CAPACITY
        self.table = [None] * capacity
        self.count = 0
        self.old_table = None


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        """
        return self.capacity


    def get_load_factor(self):
        load_factor = self.count / self.capacity
        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        """
        hash = 5281
        for b in key:
            hash = ((hash << 5) + hash) + ord(b)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        """
        index = self.hash_index(key)
        if self.table[index] is None:
            self.table[index] = HashTableEntry(key, value)
            self.count += 1
        else:
            curr = self.table[index]
            while curr.next and curr.key != key:
                curr = curr.next
            if curr.key == key:
                curr.value = value
            else:
                curr.next = HashTableEntry(key, value)
                self.count += 1

        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        """
        index = self.hash_index(key)
        curr = self.table[index]
        prev = None
        if curr.key == key:
            if curr.next:
                self.table[index] = curr.next
            else:
                self.table[index] = None
        else:
            while curr is not None:
                if curr.key == key:
                    break
                prev = curr
                curr = curr.next

            if curr is None:
                print("Key is not in hashtable")
            else:
                prev.next = curr.next


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        """
        index = self.hash_index(key)
        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr.value
            else:
                curr = curr.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        self.count = 0
        self.old_table = self.table
        self.table = [None] * new_capacity
        self.capacity = new_capacity
        for index in range(len(self.old_table)):
            curr = self.old_table[index]
            while curr:
                self.put(curr.key, curr.value) 
                curr = curr.next
        self.old_table = None


    def print_table(self):
        for index in range(len(self.table)):
            print(f"{index} -------- ")
            curr = self.table[index]
            while curr:
                print(curr.key)
                curr = curr.next
        print("\n")


    def get_count(self):
        return self.count
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")


    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
