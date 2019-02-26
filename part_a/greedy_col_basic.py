import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5

kmax = 0

def find_smallest_color(G,i):
    global kmax
    n = len(G.nodes())
    
    col = {0}
    x=1
    for j in G.neighbors(i):
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
    
    for i in range(1,n+1):
        G.nodes[i]['color'] = find_smallest_color(G,i)
    #end for
        
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)


print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)
