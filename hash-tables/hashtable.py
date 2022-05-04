class HashTable: 
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size  # this will create a list filled with None. 
    
    def _hash(self, key): 
        my_hash = 0
        for letter in key: 
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) # returning the hash table address from 0-6
        return my_hash

def main(): 
    pass


if __name__ == "__main__":
    main()