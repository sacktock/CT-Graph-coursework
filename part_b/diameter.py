import networkx as nx
import random as rd
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
    
def bfs_max(G,a):
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    n = len(G.nodes())
    Max = 0
    
    G.nodes[a]['label'] = 0
    G.nodes[a]['visited'] = "yes"
    visited = 1
    S = Queue()
    S.enqueue(a)

    while not S.isEmpty():
        i = S.dequeue()
        label = G.nodes[i]['label'] + 1
        for v in G.adj[i]:
            if G.nodes[v]['visited'] == 'no':
                G.nodes[v]['visited'] = "yes"
                G.nodes[v]['label'] = label
                if Max < G.nodes[v]['label']:
                    Max = G.nodes[v]['label']
                S.enqueue(v)

    return Max

def max_distance(G):
    n = len(G.nodes())
    
    Max = 0

    for i in range(1,n+1):
        m = bfs_max(G,i)
        if Max < m:
            Max = m

    return Max
    
print()
G6=graph6.Graph()
print('The diameter of G6 (i.e. the maximum distance between two vertices) is:', max_distance(G6))
print()


G7=graph7.Graph()
print('The diameter of G7 (i.e. the maximum distance between two vertices) is:', max_distance(G7))
print()


G8=graph8.Graph()
print('The diameter of G8 (i.e. the maximum distance between two vertices) is:', max_distance(G8))
print()


G9=graph9.Graph()
print('The diameter of G9 (i.e. the maximum distance between two vertices) is:', max_distance(G9))
print()


G10=graph10.Graph()
print('The diameter of G10 (i.e. the maximum distance between two vertices) is:', max_distance(G10))
print()
