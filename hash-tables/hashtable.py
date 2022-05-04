class HashTable: 
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size  # this will create a list filled with None. 
    
    def __hash(self, key): 
        my_hash = 0
        for letter in key: 
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) # returning the hash table address from 0-6
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None: 
            self.data_map[index] = []
        self.data_map[index].append([key,value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None: 
            for i in range(len(self.data_map[index])): # this is for the list within the list at that index. 
                if self.data_map[index][i][0] == key: # for this i is list at the index. 0 is the key at the i's values. 
                    return self.data_map[index][i][1]
        return None

    
    
    
    def print_table(self):
        for i, v in enumerate(self.data_map):
            print(i, ": ", v)

def main(): 
    table = HashTable()
    table.set_item("bolts", 1400)
    table.set_item("washer", 50)
    table.set_item("lumber", 70)
    table.set_item("test", 4)
    table.print_table()
    print()

    print(table.get_item('bolts'))
    



if __name__ == "__main__":
    main()