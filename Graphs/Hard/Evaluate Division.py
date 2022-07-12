class Solution(object):
    # This is a O(mn) time and O(n) space solution.
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        graph = defaultdict(defaultdict)

        # Creating a graph from the equations
        for (startNode, endNode), value in zip(equations, values):
            graph[startNode][endNode] = value
            graph[endNode][startNode] = 1.0 / value

        results = list()
        # Going over each and every query
        for (startNode, endNode) in queries:
            # If one of the variables is not present in the graph formed
            if startNode not in graph or endNode not in graph:
                currRetValue = -1.0
            # If both the nodes or variables are the same
            elif startNode == endNode:
                currRetValue = 1.0
            else:
                visited = set()
                currRetValue = self.calcQuery(graph, startNode, endNode, 1, visited)
            results.append(currRetValue)

        return results

    def calcQuery(self, graph, currNode, nextNode, accValue, visited):
        neighbors = graph[currNode]
        visited.add(currNode)
        retValue = -1.0

        if nextNode in neighbors:
            retValue = accValue * neighbors[nextNode]
        else:
            for neighborNode, neighborValue in neighbors.items():
                if neighborNode in visited:
                    continue
                retValue = self.calcQuery(graph, neighborNode, nextNode, accValue * neighborValue, visited)
                if retValue != -1.0:
                    break

        visited.remove(currNode)
        return retValue
