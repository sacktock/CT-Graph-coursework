import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10

def dfs(G,u,b):
    n = len(G.nodes())
    global visited_counter
    G.node[u]['visited'] = 'yes'
    visited_counter = visited_counter + 1
    print(u)
    if G.node[b]['visited'] == 'yes':
        return
    if visited_counter < n:
        for v in G.neighbors(u):
            if G.node[v]['visited'] == 'no':
                dfs(G,v,b)
                if G.node[b]['visited'] == 'yes':
                    return
            


print()
G6=graph6.Graph()
visited_counter = 0
print('The nodes of G6 are visited by depth-first-search in this order:')
dfs(G6,12,40)
print()


G7=graph7.Graph()
visited_counter = 0
print('The nodes of G7 are visited by depth-first-search in this order:')
dfs(G7,5,36)
print()


G8=graph8.Graph()
visited_counter = 0
print('The nodes of G8 are visited by depth-first-search in this order:')
dfs(G8,15,40)
print()


G9=graph9.Graph()
visited_counter = 0
print('The nodes of G9 are visited by depth-first-search in this order:')
dfs(G9,1,19)
print()


G10=graph10.Graph()
visited_counter = 0
print('The nodes of G10 are visited by depth-first-search in this order:')
dfs(G10,6,30)
print()
