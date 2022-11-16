##The first thing you need to implement is a Graph class. It represents a graph and defines all methods you might need when 
##working with graphs

class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = []

    def add_edge(self, node1, node2, weight):
        self.m_graph.append([node1, node2, weight])

        # Finds the root node of a subtree containing node `i`
    def find_subtree(self, parent, i):
        if parent[i] == i:
           return i
        return self.find_subtree(parent, parent[i])

        # Connects subtrees containing nodes `x` and `y`
    def connect_subtrees(self, parent, subtree_sizes, x, y):
       xroot = self.find_subtree(parent, x)
       yroot = self.find_subtree(parent, y)
       if subtree_sizes[xroot] < subtree_sizes[yroot]:
           parent[xroot] = yroot
       elif subtree_sizes[xroot] > subtree_sizes[yroot]:
           parent[yroot] = xroot
       else:
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1
    



##First of all, assuming that you already have a list of edges (represented in a previously described way), you should sort it from the smallest edge weight to the largest.

##After that, you should initialize and maintain two auxiliary arrays - parent and subtree_sizes. The way they are constructed is of
## great importance, so follow along carefully. Both of them have the size that corresponds to the number of nodes in the initial graph (i.e. if the initial graph has n nodes, those two arrays have n elements).


def kruskals_mst(self):
    # Resulting tree
    result = []
    
    # Iterator
    i = 0
    # Number of edges in MST
    e = 0

    # Sort edges by their weight
    self.m_graph = sorted(self.m_graph, key=lambda item: item[2])
    
    # Auxiliary arrays
    parent = []
    subtree_sizes = []

    # Initialize `parent` and `subtree_sizes` arrays
    for node in range(self.m_num_of_nodes):
        parent.append(node)
        subtree_sizes.append(0)

    # Important property of MSTs
    # number of egdes in a MST is 
    # equal to (m_num_of_nodes - 1)
    while e < (self.m_num_of_nodes - 1):
        # Pick an edge with the minimal weight
        node1, node2, weight = self.m_graph[i]
        i = i + 1

        x = self.find_subtree(parent, node1)
        y = self.find_subtree(parent, node2)

        if x != y:
            e = e + 1
            result.append([node1, node2, weight])
            self.connect_subtrees(parent, subtree_sizes, x, y)
    
    # Print the resulting MST
    for node1, node2, weight in result:
        print("%d - %d: %d" % (node1, node2, weight))



# Example graph has 9 nodes
example_graph = Graph(5)



##Then you add all nodes from the example grah to the example_graph using add_edge() method:
example_graph.add_edge(0, 2, 75)
example_graph.add_edge(0, 1, 9)
example_graph.add_edge(2, 1, 95)
example_graph.add_edge(2, 3, 51)
example_graph.add_edge(1, 3, 19)
example_graph.add_edge(1, 4, 41)
example_graph.add_edge(4, 3, 31)



kruskals_mst(example_graph)

