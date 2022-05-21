# Graphs: 

## Notes: 

Vertex or node. 
Edge or connection. 

```
      3
44 - - - - 76
           | 
           |  15 
           | 
           32
```

Edges can be weighted or not not. 
depending on the weight of this - you can determine which path you want to take and how much we want to travel. 


Trees are a form of graphs. Linked List is a form of Tree. There for a linked list is form of Graph. 


### Adjacency Matrix: 
* This would be having a matric that has a 1 for edge and 0 for no edges. 

```
  x a b c d e
  a 0 1 0 0 1
  b 1 0 1 0 0 
  c 0 1 0 1 0
  d 0 0 1 0 1
  e 1 0 0 1 0
```

Y-axis above are the verties and the x-axis is the edge. 
The edges are bi-directional and usually the edges have a symtry


### Adjacency List: 
* The graph will be represented with dictionary and list in it. 

```python
{ 
    'A' : ['B', 'E'],
    'B' : ['A', 'C'], 
    'C' : ['B', 'D'], 
    'D' : ['C', 'E'],
    'E' : ['A', 'D']
}
```

Time Complexity: 
* when adding a new: O(|V|^2) for the matrix and O(1) for the list. 
* Rmoving: matrix: O(|V|^2) and list: O(|V| + |E|)


### Graph: Add Vertix
* this is adding in a node or vertix. 

```python
class Graph: 
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
```

### Graph: Add Edge
* connecting the two or more vertices. 

```python
def add_edge(self, v1, v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():  
        self.adj_list[v].append(v2)
        self.adj_list[v].append(v1) # we only want to do this if they exist. 
        return True
    return False
```

### Graph: remove edge: 
* We are removing the connection between the vertex. 
* We do this by modifying the dict. 
* We are going to have to verify if they are in the list. 
* We also want to add in try/except to cover any value exception for a vertex that might not have a connection. 
* We are covering for ValueError.


### Graph: Remove Vertex: 
* when we want to remove a vertex we are going to remove all the edges and then remove the vertex. 
* When graphs are bi-directional. If on vertex has an edge with another vertex - we know those two are in two places and we can simply remove the edge. 
* We are going to do this with a for-loop. 


### Quiz: 
1. adding a new vertex in adj list is O(1): True
2. Graphs are go to data structure when you need to represent entites and the relationships between them: True 
3. Removing a vertex is O(1): False