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
#QUEUES#
########

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def dequeue(self):
        output = self.front.data
        self.front = self.front.after
        if self.front == None:
            self.rear = None
        return output
    def enqueue(self, data):
        if self.rear == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.after = Node(data, self.rear)
            self.rear = self.rear.after

####################################################
    
def bfs(G,a,b):
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels

    G.nodes[a]['label'] = 0
    G.nodes[a]['visited'] = "yes"
    S = Queue()
    S.enqueue(a)

    while G.nodes[b]['visited'] == 'no':
        i = S.dequeue()
        label = G.nodes[i]['label'] + 1
        for v in G.adj[i]:
            if G.nodes[v]['visited'] == 'no':
                G.nodes[v]['visited'] = "yes"
                G.nodes[v]['label'] = label
                S.enqueue(v)

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
