# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
 
# Library for INT_MAX
import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    def printSolution(self, dist):
        print ("Vertex \tDistance from Source")
        for node in range(self.V):
            print (node,"\t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]
 
        self.printSolution(dist)
 
# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
 
g.dijkstra(0);

 
# This code is contributed by Divyanshu Mehta


#Notas:  
#1) El c??digo calcula la distancia m??s corta pero no calcula la informaci??n de la ruta. Podemos crear una matriz principal, actualizar la matriz principal cuando se actualiza la distancia (como la implementaci??n de prim ) y usarla para mostrar la ruta m??s corta desde la fuente a diferentes v??rtices.
#2) El c??digo es para gr??ficos no dirigidos, la misma funci??n de Dijkstra se puede utilizar tambi??n para gr??ficos dirigidos.
#3) El c??digo encuentra las distancias m??s cortas desde la fuente hasta todos los v??rtices. Si estamos interesados ??????solo en la distancia m??s corta desde la fuente a un solo objetivo, podemos romper el bucle for cuando el v??rtice de distancia m??nima elegido es igual al objetivo (Paso 3.a del algoritmo).
#4)La complejidad temporal de la implementaci??n es O (V ^ 2). Si el gr??fico de entrada se representa mediante una lista de adyacencia , se puede reducir a O (E log V) con la ayuda de un mont??n binario. Consulte 
#el algoritmo de Dijkstra para la representaci??n de listas de adyacencia para obtener m??s detalles.
#5) El algoritmo de Dijkstra no funciona para gr??ficos con ciclos de peso negativos. Puede dar resultados correctos para un gr??fico con bordes negativos, pero debe permitir que un v??rtice se pueda visitar varias veces y esa versi??n perder?? su complejidad de tiempo r??pido. Para gr??ficos con aristas y ciclos de peso negativo, se puede usar el algoritmo de Bellman-Ford ; pronto lo discutiremos como una publicaci??n separada.