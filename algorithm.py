# The following code is an implementation of Boruvka's Algorithm
# Instructions to test the code are below the Graph Class
# Test cases are below the Graph Class

# The results of the algorithm are displayed in the terminal. The final MST Weight is printed. An array of all edges in the final MST are printed.
# The edges added to the MST at each iterations are printed to show step-by-step construction of the final MST.
# I opted to display the results like this for simplicity and efficiency given the scope of this coursework. 
# If I were to continue developing this project, I would implement graph visualisation to display the MST to provide a more intuitive understanding.

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
        
        # find an edge connected to v to initalise cheapest
        for e in self.edges:
            if (e[0] != e[1]): # ignore edges that are a loop
                if (e[0] == v) or (e[1]) == v:
                    cheapest = e

        for e in self.edges:
            # if edge connects to the vertex
            if (e[0] == v) or (e[1]) == v: 
                if (e[0] != e[1]): # ignore edges that are a loop
                    # if weight of the edge is less than cheapest, update cheapest
                    if e[2] < cheapest[2]:
                        cheapest = e

        return cheapest
    
    # recursively looks through the parent array to find the root of vertex v
    def findRoot(self,v):
        if self.parents[v] != v:  # if v is not its own parent
            self.parents[v] = self.findRoot(self.parents[v])  # recursively find and compress
        return self.parents[v]
    

    # combine two parents into same component, making vertex u the parent of vertex v
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
print("Test Case 1:")

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
print("\n\n\nTest Case 2:")

g2 = Graph(7)
g2.add_edge(0, 1, 6)
g2.add_edge(0, 2, 7)
g2.add_edge(0, 3, 5)
g2.add_edge(1, 3, 2)
g2.add_edge(2, 6, 10)
g2.add_edge(2, 5, 11)
g2.add_edge(2, 4, 9)
g2.add_edge(3, 4, 12)
g2.add_edge(3, 6, 8)
g2.add_edge(6, 5, 4)
g2.add_edge(4, 5, 3)

# Expected Final Outputs:
# Final MST Weight: 29
# Final MST Edges: [[0, 3, 5], [1, 3, 2], [0, 2, 7], [4, 5, 3], [6, 5, 4], [3, 6, 8]]
g2.boruvkas()




# Test Case 3:
print("\n\n\nTest Case 3:")

g3 = Graph(9)
g3.add_edge(0,1,4)
g3.add_edge(0,7,8)
g3.add_edge(1,2,8)
g3.add_edge(1,7,11)
g3.add_edge(7,8,7)
g3.add_edge(7,6,1)
g3.add_edge(2,3,7)
g3.add_edge(2,8,2)
g3.add_edge(2,5,4)
g3.add_edge(8,6,6)
g3.add_edge(6,5,2)
g3.add_edge(3,4,9)
g3.add_edge(3,5,14)
g3.add_edge(5,4,10)

# Expected Final Outputs:
# Final MST Weight: 37
# Final MST Edges: [[0, 1, 4], [2, 8, 2], [2, 3, 7], [3, 4, 9], [6, 5, 2], [7, 6, 1], [0, 7, 8], [2, 5, 4]]
g3.boruvkas()