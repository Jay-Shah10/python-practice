# Hash Tables: 


## Intro: 

Hash tables in Python is basically a dict. This is based on key value pair. 
Then we run a hash on this dict. This will return a "key" where the dict will stored. 

Hash is one way. meaning is we take "nails" and hash it - and it gives you a `2`. You can cannot take in `2` hash and get "nails". 

For this, we are going to create our own "hash table" using list. this will create a list within a list. 



## Collisions. 
This happens when you put a key-value pair at a location where there is already a key-value pairs. 
In order to deal with collision, you use Sepearte Chaining. 

Linear Probing (open addressing) - make sure that you do not have more than one key-value pair at an address. what this does is when a key-value pair comes in - it will check the memory space, if full, then  moves to the next one. repeat. 

we are going to do Seperate Chainig = using linked lists at the memory address. 

## Constrctor: 
* one of the best practice is to use prime numbers - increases the randomness of the memory. 
* list of 0-7. 

## Set method: 
running the hash method on the key which will create the index in the list. 

```python

def set_item(self, key, value):
    index = self.__hash(key): 
    if self.data_map[index] == None:
        self.data_map[index] = []
    self.data_map[index].append([key, value])

```

## Big O
* The hash method itself is going to be O(1)
* setting is also O(1)
* get function is O(n)



## Common interview question: 
you have two lists and you want to find if they have something in commnon. 
* Two approaches. 
1. you have nested for-loops. you can check if each value is in each.  O(n^2)

```python
def item_common(list1, list2):
    for i in list1: 
        for j in list2: 
            if i == j: 
                return True
    return False
```

2. Better option. we put one list in a dic with list1 values as key and values as true. Now you only have to look for this key in the dict using list2. O(n)

```python
def item_common(list1, list2):
    mydict = {}
    for i in list1: 
        mydict[i] = True
    for j in list2: 
        if j in mydict: 
            return True
    return False
```