import networkx 
print(networkx.__version__) # check the versionnn
 
DG=networkx.DiGraph() # make a directed graph (digraph)
DG.add_nodes_from(["S","A","B","C","D","E","T"]) # add nodes
DG.add_edges_from([("S","A"),("S","B"),("S","C"),("A","B"),("A","D"),("B","D"),("B","C"),
    ("B","E"),("C","E"),("D","T"),("E","T")])  
# specify the capacity values for the edges:
networkx.set_edge_attributes(DG, 'capacity', {('S','A'): 5.0, ('S','B'): 6.0, ('S','C'): 8.0, 
    ('A','B'): 4.0, ('A','D'): 10.0, ('B','D'): 3.0, ('B','C'): 2.0, ('B','E'): 11.0, 
    ('C','E'): 6.0, ('D','T'): 9.0, ('E','T'): 4.0})


import pygraphviz
G=pygraphviz.AGraph(strict=False,directed=True)
nodelist = ['A', 'B', 'C', 'D', 'E', 'S', 'T']
G.add_nodes_from(nodelist)
G.add_edge('S','A',label='5')
G.add_edge('S','B',label='6')
G.add_edge('S','C',label='8')
G.add_edge('A','B',label='4')
G.add_edge('A','D',label='10')
G.add_edge('B','D',label='3')
G.add_edge('B','E',label='11')
G.add_edge('B','C',label='2')
G.add_edge('C','E',label='6')
G.add_edge('D','T',label='9')
G.add_edge('E','T',label='4')
G.layout()
G.draw('file.png')