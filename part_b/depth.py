import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10

#####################################################

class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

########
#STACKS#
########

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

####################################################
    
def bfs(G,a,b):
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels

    G.nodes[a]['label'] = 0
    G.nodes[a]['visited'] = "yes"
    S = Stack()
    S.push(a)

    while G.nodes[b]['visited'] == 'no':
        i = S.pop()
        print(i)
        label = G.nodes[i]['label'] + 1
        for v in G.adj[i]:
            if G.nodes[v]['visited'] == 'no':
                G.nodes[v]['visited'] = "yes"
                G.nodes[v]['label'] = label
                S.push(v)

    return G.nodes[b]['label']
        
G6=graph6.Graph()
a=12
b=40
print('Graph G6:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G6,a,b))
print()


G7=graph7.Graph()
a=5
b=36
print('Graph G7:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G7,a,b))
print()


G8=graph8.Graph()
a=15
b=35
print('Graph G8:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G8,a,b))
print()


G9=graph9.Graph()
a=1
b=19
print('Graph G9:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G9,a,b))
print()


G10=graph10.Graph()
a=6
b=30
print('Graph G10:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G10,a,b))
print()
