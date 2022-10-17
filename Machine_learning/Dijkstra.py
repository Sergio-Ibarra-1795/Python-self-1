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
#1) El código calcula la distancia más corta pero no calcula la información de la ruta. Podemos crear una matriz principal, actualizar la matriz principal cuando se actualiza la distancia (como la implementación de prim ) y usarla para mostrar la ruta más corta desde la fuente a diferentes vértices.
#2) El código es para gráficos no dirigidos, la misma función de Dijkstra se puede utilizar también para gráficos dirigidos.
#3) El código encuentra las distancias más cortas desde la fuente hasta todos los vértices. Si estamos interesados ​​solo en la distancia más corta desde la fuente a un solo objetivo, podemos romper el bucle for cuando el vértice de distancia mínima elegido es igual al objetivo (Paso 3.a del algoritmo).
#4)La complejidad temporal de la implementación es O (V ^ 2). Si el gráfico de entrada se representa mediante una lista de adyacencia , se puede reducir a O (E log V) con la ayuda de un montón binario. Consulte 
#el algoritmo de Dijkstra para la representación de listas de adyacencia para obtener más detalles.
#5) El algoritmo de Dijkstra no funciona para gráficos con ciclos de peso negativos. Puede dar resultados correctos para un gráfico con bordes negativos, pero debe permitir que un vértice se pueda visitar varias veces y esa versión perderá su complejidad de tiempo rápido. Para gráficos con aristas y ciclos de peso negativo, se puede usar el algoritmo de Bellman-Ford ; pronto lo discutiremos como una publicación separada.