class Graph:
    def __init__(self, numOfNodes):
        self.v = numOfNodes
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    # when given a vertex, find the cheapest edge that it connects to
    def find(self, v):
        cheapest = []
        
        # find an edge to initalise cheapest with a value
        for e in self.edges:
            if (e[0] == v) or (e[1]) == v:
                cheapest = e

        # cycle through all edges
        for e in self.edges:
            # if the edge contains the vertex
            if (e[0] == v) or (e[1]) == v:
                # if the weight of the edge is less than cheapest, update cheapest
                if e[2] < cheapest[2]:
                    cheapest = e

        return cheapest
    
    # combine two parents into the same component, making u the parent of v
    def union(self, u, v):
        self.parents.remove(v)

        # add v to u's children
        for c in self.children:
            if c[0] == u:
                c.append(v)
                break
        else: 
            self.children.append([u, v]) # if u doesn't have any children, create one

        tempChildren = []

        # look for v's children and add to u's children
        for c in self.children:
            if c[0] == v:
                tempChildren = c[1:]

                for c in self.children:
                    if c[0] == u:
                        c.append(tempChildren)

                    break
            break


    def boruvkas(self):
        self.parents = []
        self.children = [] # first value in the sub array is the parent

        # add all the nodes as individual parents
        for node in range(self.v):
            self.parents.append(node)

        

        # while the number of parents is not 1
        while (len(self.parents) != 1):
            tempParents = self.parents # used to temporarly cycle through all the parents
            for p in tempParents:
                cheapest = self.find(p)
                print(p)
                self.union(cheapest[0], cheapest[1])
            break

        # print(self.parents)
        # print(self.children)

        # need to look up how the algorithm works on each step


g = Graph(5)
g.add_edge(0,1,1)
g.add_edge(0,2,2)
g.add_edge(1,2,3)
g.add_edge(1,3,4)
g.add_edge(2,4,5)
g.add_edge(3,4,6)
g.boruvkas()