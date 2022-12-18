#Name:Tanishq Patil
#File: graph.py
# Student ID:1961827 
#Date:12/4/2022
#Sources:Professor L. Munishkina, Google Colab, https://colab.research.google.com/drive/1jfk6wrSwB9m7fOYWbtv4MUIqEoDvRd0f?authuser=1#scrollTo=OZuAvBYUB3zc
class Vertex:

    def __init__(self,key,val):
        self.id = key
        self.val=val
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()
    def Connection(self):
        x=[i for i in self.connectedTo]
        return x
    def getVal(self):
        return self.val
    def setVal(self,nbr):
        self.val=nbr



    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key,val=None):
        if type(key)!=type(Vertex(key,0)):
            newVertex = Vertex(key,val)
        else:
            newVertex=key
        self.numVertices = self.numVertices + 1
        self.vertList[key] = newVertex
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None


    def __contains__(self,n):
        return n in self.vertList.values()

    def addEdge(self,f,t,weight=0):
        if t not in self.vertList:
            added = self.addVertex(t)
        if f not in self.vertList:
            added = self.addVertex(f)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def breadth_first_search(self, s):
        for v in self.vertList.values():
            v.color = 'white'
        Q = []
        p = [] 
        start = self.vertList[ s]
        start.color = 'gray'
        Q.append(start)
        p.append(start.id)
        while len(Q) != 0:
            v = Q.pop(0)
            for u in v.connectedTo.keys():
                if u.color == 'white':
                    u.color = 'gray'
                    Q.append(u)
                    p.append(u.id)
            v.color = 'black'
        return p

    def depth_first_search(self):
        for v in self.vertList.values():
            v.color = 'white'
        p = [] 
        for v in self.vertList.values():
            if v.color == 'white':
                self.DFS(v.id, p)
        return p

    def DFS(self, vid, path):
        v = self.vertList[ vid]
        v.color = 'gray'
        path.append(v.id)
        for u in v.connectedTo.keys():
            if u.color == 'white':
                self.DFS(u.id, path)
        v.color = 'black'
        return path
if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
        
    g.addEdge(0,1)
    g.addEdge(0,5)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(4,0)
    g.addEdge(5,4)
    g.addEdge(5,2)
    for v in g:
        print(v)
    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False
    
    print(str(g.getVertex(0)))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'
    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'
    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]
    
    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]