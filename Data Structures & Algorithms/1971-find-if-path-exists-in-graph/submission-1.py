class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # Time complexity: DFS on a graph O(V + E)
        # Space complexity: Hashmap of edges with worst case O(V * V-1) = O(V^2)
        # V is number of nodes, E is number of edges

        # Edge cases

        # Main code
        # Convert edges from list of lists to hashmap of sets for O(1) access
        edgesMap = {}
        for edge in edges:
            a, b = edge
            if a in edgesMap.keys(): edgesMap[a].add(b)
            else: edgesMap[a] = set([b])
            # Because it is bidirectional
            if b in edgesMap.keys(): edgesMap[b].add(a)
            else: edgesMap[b] = set([a])

        # Recursive function
        def recursion(node, visitedNodes):
            if node == destination: 
                # Reached node is the destination, we are done
                return True
            else: 
                # Reached node is not the destination, keep searching
                # First, mark that we reached this node so we do not visit it again
                visitedNodes.add(node)
                # Second, explore all possible nextNode from here
                for nextNode in edgesMap.get(node, []):
                    if nextNode not in visitedNodes:
                        if recursion(nextNode, visitedNodes) == True: 
                            # Backtracking part where we resurface destination is found
                            return True
            # If we end up here, the search did not lead to the destination
            return False

        # Create a structure to keep track of visited sites
        visitedNodes = set()
        # Start the search from the source 
        return recursion(source, visitedNodes)