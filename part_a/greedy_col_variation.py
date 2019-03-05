import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5

def find_next_vertex(G):
    visited = []
    unvisited = []
    
    for i in G.nodes():
        if G.nodes[i]['color'] != 'never coloured':
            visited.append(i)
        else:
            unvisited.append(i)

    unvisited.sort()

    for i in unvisited:
        for j in G.adj[i]:
            if j in visited:
                return i
    return

def find_smallest_color(G,i):
    global kmax
    
    col = {0}
    x=1
    for j in G.adj[i]:
        if G.nodes[j]['color'] != 'never coloured':
            col.add(G.nodes[j]['color'])

    while x in col:
        x +=1

    if kmax < x:
        kmax = x
            
    return x

def greedy(G):
    global kmax
    kmax = 0
    n = len(G.nodes())

    i = 1
    for _ in range(0,n):
        G.nodes[i]['color'] = find_smallest_color(G,i)
        i = find_next_vertex(G)
        if i == None:
            break
    #end for
        
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    print()



print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)
