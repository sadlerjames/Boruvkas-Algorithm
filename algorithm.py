class Graph:
    def __init__(self, numOfNodes):
        self.nodes = numOfNodes
        self.edges = [] # all edges of the graph
        self.cheapest = [] # cheapest edge for each node

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    # when given a vertex, find the cheapest edge that it connects to
    def findCheapest(self, v):
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
    
    # recursively looks through the parent array to find the root
    def findRoot(self,v):
        if self.parents[v] != v:  # If v is not its own parent
            self.parents[v] = self.findRoot(self.parents[v])  # Recursively find and compress
        return self.parents[v]
    

    
    # combine two parents into the same component, making u the parent of v
    def union(self, u, v):
        rootU = self.findRoot(u)
        rootV = self.findRoot(v)

        if rootU != rootV:
            self.parents[rootV] = rootU # make rootU the parent of rootV


    def boruvkas(self):
        self.parents = []
        self.children = [] # first value in the sub array is the parent
        mstWeight = 0
        mstEdges = []

        # add all the nodes as individual parents
        for node in range(self.nodes):
            self.parents.append(node)

        # find the cheapest edge for each node and store
        for p in self.parents:
            nodeCheapest = [p]
            nodeCheapest.append(self.findCheapest(p))
            self.cheapest.append(nodeCheapest)


        # while there is more than one root in the list        
        while len(set(self.findRoot(i) for i in range(self.nodes))) > 1:
            cheapestEdge = [None] * self.nodes 

            # Find the cheapest edge for each component
            for u, v, w in self.edges:
                rootU = self.findRoot(u)
                rootV = self.findRoot(v)

                # If u and v belong to different components
                if rootU != rootV:
                    # Check and update the cheapest edge for component of u
                    if cheapestEdge[rootU] is None or w < cheapestEdge[rootU][2]:
                        cheapestEdge[rootU] = [u, v, w]

                    # Check and update the cheapest edge for component of v
                    if cheapestEdge[rootV] is None or w < cheapestEdge[rootV][2]:
                        cheapestEdge[rootV] = [u, v, w]

            for i in range(self.nodes):
                if cheapestEdge[i] is not None:  # If there's a valid cheapest edge
                    u, v, w = cheapestEdge[i]
                    rootU = self.findRoot(u)
                    rootV = self.findRoot(v)

                    # If the edge connects different components, add it to the MST
                    if rootU != rootV:
                        mstWeight += w
                        mstEdges.append([u, v, w])
                        self.union(rootU, rootV)

            # Output the MST weight and edges
            print("\nFinal MST Weight:", mstWeight)
            print("Final MST Edges:", mstEdges)
        

g = Graph(9)
g.add_edge(0,1,4)
g.add_edge(0,7,8)
g.add_edge(1,2,8)
g.add_edge(1,7,11)
g.add_edge(7,8,7)
g.add_edge(7,6,1)
g.add_edge(2,3,7)
g.add_edge(2,8,2)
g.add_edge(2,5,4)
g.add_edge(2,3,7)
g.add_edge(8,6,6)
g.add_edge(6,5,2)
g.add_edge(3,4,9)
g.add_edge(3,5,14)
g.add_edge(5,4,10)
g.boruvkas()