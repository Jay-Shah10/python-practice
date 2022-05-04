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


