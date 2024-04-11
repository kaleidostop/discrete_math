from abc import ABC, abstractmethod
from sys import maxsize

INF = maxsize

class GraphABC(ABC):
    @abstractmethod
    def add_edge(self, x, y, w): pass

    def __init__(self):
        self.vertices = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
              'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'z': 20}
        self.n = len(self.vertices)

    def create(self):
        self.add_edge('a', 'b', 2)
        self.add_edge('a', 'c', 4)
        self.add_edge('a', 'd', 1)

        self.add_edge('b', 'c', 3)
        self.add_edge('b', 'e', 1)

        self.add_edge('c', 'e', 2)
        self.add_edge('c', 'f', 2)

        self.add_edge('d', 'g', 4)
        self.add_edge('d', 'f', 5)

        self.add_edge('e', 'h', 3)

        self.add_edge('f', 'h', 3)
        self.add_edge('f', 'i', 2)
        self.add_edge('f', 'j', 4)
        self.add_edge('f', 'g', 3)

        self.add_edge('g', 'k', 2)

        self.add_edge('h', 'o', 8)
        self.add_edge('h', 'l', 1)

        self.add_edge('i', 'l', 3)
        self.add_edge('i', 'm', 2)
        self.add_edge('i', 'j', 3)

        self.add_edge('j', 'm', 6)
        self.add_edge('j', 'n', 3)
        self.add_edge('j', 'k', 6)

        self.add_edge('k', 'n', 4)
        self.add_edge('k', 'r', 2)

        self.add_edge('l', 'o', 6)
        self.add_edge('l', 'm', 3)

        self.add_edge('m', 'o', 4)
        self.add_edge('m', 'p', 2)
        self.add_edge('m', 'n', 5)

        self.add_edge('n', 'q', 2)
        self.add_edge('n', 'r', 1)

        self.add_edge('o', 'p', 2)
        self.add_edge('o', 's', 6)

        self.add_edge('p', 's', 2)
        self.add_edge('p', 't', 1)
        self.add_edge('p', 'q', 1)

        self.add_edge('q', 't', 3)
        self.add_edge('q', 'r', 8)

        self.add_edge('r', 't', 5)

        self.add_edge('s', 'z', 2)

        self.add_edge('t', 'z', 8)


class Graph3(GraphABC):
    def __init__(self):
        super(Graph3, self).__init__()
        self.w = [[INF for _ in range(self.n)] for _ in range(self.n)]
        self.adj = [[] for _ in range(self.n)]
        super(Graph3, self).create()

    def add_edge(self, x, y, w):
        i = self.vertices[x]
        j = self.vertices[y]
        self.w[i][j] = w
        self.w[j][i] = w
        self.adj[i].append(j)
        self.adj[j].append(i)

    def Dijkstra(self, start, end):
        s = self.vertices[start]
        f = self.vertices[end]
        d = [INF for _ in range(self.n)]
        prev = [-1 for _ in range(self.n)]
        used = [False for _ in range(self.n)]
        d[s] = 0
        for i in range(self.n):
            v = -1
            for j in range(self.n):
                if (not used[j]) and (v == -1 or d[j] < d[v]):
                    v = j
            if d[v] == INF:
                break
            used[v] = True
            for u in self.adj[v]:
                if d[u] + self.w[v][u] < d[u] or d[u] == INF:
                    d[u] = d[v] + self.w[v][u]
                    prev[u] = v

        print("Dijkstra")
        if d[f] == INF:
            print("dist = ", -1)

        print("dist =", d[f])

        vs = list(self.vertices.keys())
        path = [vs[f]]
        v = f
        while(v != s):
            v = prev[v]
            path.append(vs[v])
        path.reverse()
        print("path:", *path)


class Graph6(GraphABC):
    def __init__(self):
        super(Graph6, self).__init__()
        self.w = [[INF for _ in range(self.n)] for _ in range(self.n)]
        self.adj = [[] for _ in range(self.n)]
        super(Graph6, self).create()

    def add_edge(self, x, y, w):
        i = self.vertices[x]
        j = self.vertices[y]
        self.w[i][j] = w
        self.w[j][i] = w
        self.adj[i].append(j)
        self.adj[j].append(i)

    def Floyd(self, start, end):
        d = [[self.w[i][j] for j in range(self.n)] for i in range(self.n)]
        prev = [[-1 for _ in range(self.n)] for _ in range(self.n)]

        for i in range(self.n):
            prev[i][i] = i
            for j in self.adj[i]:
                prev[i][j] = i

        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    if d[j][i] + d[i][k] < d[j][k]:
                        d[j][k] = d[j][i] + d[i][k]
                        prev[j][k] = prev[i][k]

        s = self.vertices[start]
        f = self.vertices[end]

        print("Floyd")
        print("dist", d[s][f])
        vs = list(self.vertices.keys())
        path = [vs[f]]
        v = f
        while (v != s):
            v = prev[s][v]
            path.append(vs[v])
        path.reverse()
        print("path:", *path)




class Graph10(GraphABC):
    def __init__(self):
        super(Graph10, self).__init__()
        self.edges = []
        super(Graph10, self).create()
        self.m = len(self.edges)

    def add_edge(self, x, y, w):
        i = self.vertices[x]
        j = self.vertices[y]
        self.edges.append([i, j, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x = self.find(parent, x)
        y = self.find(parent, y)
        if (x != y):
            if (rank[x] < rank[y]):
                x, y = y, x
            parent[y] = x
            rank[x] = rank[x] + rank[y]

    def Boruvka(self):
        parent = []
        rank = []
        min_edge = []
        num_trees = self.n
        MST = []
        vs = list(self.vertices.keys())

        for node in range(self.n):
            parent.append(node)
            rank.append(0)
            min_edge.append([-1, -1, -1])

        while num_trees > 1:
            for edge in range(self.m):
                u, v, w = self.edges[edge]
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                if set1 != set2:
                    if min_edge[set1][0] == -1 or min_edge[set1][2] > w:
                        min_edge[set1] = [u, v, w]
                    if min_edge[set2][0] == -1 or min_edge[set2][2] > w:
                        min_edge[set2] = [u, v, w]

            for node in range(self.n):
                if min_edge[node][0] != -1:
                    u, v, w = min_edge[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)

                    if set1 != set2:
                        MST.append([vs[u], vs[v], w])
                        self.union(parent, rank, set1, set2)
                        num_trees -= 1

            min_edge = [[-1, -1, -1]] * self.n

        print("MST:", MST)


g3 = Graph3()

g3.Dijkstra('a', 'z')

g6 = Graph6()

g6.Floyd('a', 'z')

g10 = Graph10()

g10.Boruvka()
