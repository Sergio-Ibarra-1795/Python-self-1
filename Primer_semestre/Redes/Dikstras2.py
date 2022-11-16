##FROM: https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/dijkstras-algorithm/
##Now that we've gone over the step-by-step process, let's see how we can implement Dijkstra's algorithm in Python! 
##To sort and keep track of the vertices we haven't visited yet - we'll use a PriorityQueue:

from queue import PriorityQueue

##Now, we'll implement a constructor for a class called Graph:
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

        ##Now, let's define a function which is going to add an edge to a graph:
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight



def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D



g = Graph(12)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 2)
g.add_edge(0, 3, 2.5)
g.add_edge(0, 4, 3)
g.add_edge(1, 5, 3)
g.add_edge(2, 5, 1.5)
g.add_edge(3, 2, 3)
g.add_edge(3, 6, 3)
g.add_edge(4, 3, 3.5)
g.add_edge(4, 6, 3)
g.add_edge(4, 7, 3)
g.add_edge(5, 8, 9)
g.add_edge(6, 5, 2)
g.add_edge(6, 8, 7.5)
g.add_edge(7, 10, 4) 
g.add_edge(8, 9, 7.5)
g.add_edge(8, 9, 7.5) 
g.add_edge(8, 11, 4)
g.add_edge(9, 11, 3.5) 
g.add_edge(9, 7, 10)
g.add_edge(10, 11, 6)


'''
##g = Graph(12)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2.5)
g.add_edge(1, 5, 3)
g.add_edge(2, 6, 3)
g.add_edge(3, 6, 1.5)
g.add_edge(4, 3, 3)
g.add_edge(4, 7, 3)
g.add_edge(5, 4, 3.5)
g.add_edge(5, 7, 3)
g.add_edge(5, 8, 3)
g.add_edge(6, 9, 9)
g.add_edge(7, 6, 2)
g.add_edge(7, 9, 7.5)
g.add_edge(8, 11, 4) 
g.add_edge(9, 10, 7.5)
g.add_edge(9, 10, 7.5) 
g.add_edge(9, 12, 4)
g.add_edge(10, 12, 3.5) 
g.add_edge(10, 8, 10)
g.add_edge(11, 10, 6)
'''

D = dijkstra(g, 0)

print(D)


for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])


