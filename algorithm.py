class Graph:
    def __init__(self, numOfNodes):
        self.nodes = numOfNodes
        self.edges = [] # all edges of the graph
        self.cheapest = [] # cheapest edge for each node

    # appends passed in edge to Graph
    # u = source vertex, v = desination vertex, w = weight of the edge
    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    # find cheapest edge that passed in vertex (v) connects to
    def findCheapest(self, v):
        cheapest = []
        
        # find an edge to initalise cheapest with a value
        for e in self.edges:
            if (e[0] == v) or (e[1]) == v:
                cheapest = e

        for e in self.edges:
            # if edge connects to the vertex
            if (e[0] == v) or (e[1]) == v:
                # if weight of the edge is less than cheapest, update cheapest
                if e[2] < cheapest[2]:
                    cheapest = e

        return cheapest
    
    # recursively looks through the parent array to find the root
    def findRoot(self,v):
        if self.parents[v] != v:  # if v is not its own parent
            self.parents[v] = self.findRoot(self.parents[v])  # recursively find and compress
        return self.parents[v]
    

    # combine two parents into same component, making u the parent of v
    def union(self, u, v):
        rootU = self.findRoot(u)
        rootV = self.findRoot(v)

        # make rootU the parent of rootV
        if rootU != rootV:
            self.parents[rootV] = rootU 

    # calculates the MST of the graph
    def boruvkas(self):
        self.parents = []
        mstWeight = 0
        mstEdges = []
        iteration = 1

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

            # find the cheapest edge for each component
            for u, v, w in self.edges:
                rootU = self.findRoot(u)
                rootV = self.findRoot(v)

                # if u and v belong to different components
                if rootU != rootV:
                    # check and update the cheapest edge for component of u
                    if cheapestEdge[rootU] is None or w < cheapestEdge[rootU][2]:
                        cheapestEdge[rootU] = [u, v, w]

                    # check and update the cheapest edge for component of v
                    if cheapestEdge[rootV] is None or w < cheapestEdge[rootV][2]:
                        cheapestEdge[rootV] = [u, v, w]

            for i in range(self.nodes):
                # if there's a valid cheapest edge
                if cheapestEdge[i] is not None:  
                    u, v, w = cheapestEdge[i]
                    rootU = self.findRoot(u)
                    rootV = self.findRoot(v)

                    # if edge connects different components, add it to the MST
                    if rootU != rootV:
                        mstWeight += w
                        mstEdges.append([u, v, w])
                        self.union(rootU, rootV)

            print("\nIteration:", iteration, "- MST Weight:", mstWeight)
            print("Iteration:", iteration, "- MST Edges:", mstEdges)
            iteration += 1

        print("\nFinal MST Weight:", mstWeight)
        print("Final MST Edges:", mstEdges)
        

# To test the code:
# 1. Initalise a new instance of the class, Graph, with the required number of vertices of the graph you are testing
# 2. Add all edges of your graph to the instance via the add_edge function 
# 3. Call the boruvkas function on the instance of the Graph class
# 4. Repeat for different graphs


# Test Case 1:

g1 = Graph(9)
g1.add_edge(0, 1, 4)
g1.add_edge(0, 6, 7)
g1.add_edge(1, 2, 9)
g1.add_edge(1, 6, 11)
g1.add_edge(1, 7, 20)
g1.add_edge(6, 7, 1)
g1.add_edge(2, 3, 6)
g1.add_edge(2, 4, 2)
g1.add_edge(4, 3, 10)
g1.add_edge(4, 5, 15)
g1.add_edge(4, 7, 1)
g1.add_edge(4, 8, 5)
g1.add_edge(7, 8, 3)
g1.add_edge(3, 5, 5)
g1.add_edge(8, 5, 12)

# Expected Final Outputs:
# Final MST Weight: 29
# Final MSt Edges: [[0, 1, 4], [2, 4, 2], [3, 5, 5], [4, 7, 1], [6, 7, 1], [7, 8, 3], [0, 6, 7], [2, 3, 6]]
g1.boruvkas()


# Test Case 2:




# g = Graph(9)
# g.add_edge(0,1,4)
# g.add_edge(0,7,8)
# g.add_edge(1,2,8)
# g.add_edge(1,7,11)
# g.add_edge(7,8,7)
# g.add_edge(7,6,1)
# g.add_edge(2,3,7)
# g.add_edge(2,8,2)
# g.add_edge(2,5,4)
# g.add_edge(2,3,7)
# g.add_edge(8,6,6)
# g.add_edge(6,5,2)
# g.add_edge(3,4,9)
# g.add_edge(3,5,14)
# g.add_edge(5,4,10)
# g.boruvkas()