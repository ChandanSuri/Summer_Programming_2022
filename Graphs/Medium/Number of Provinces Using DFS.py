class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        numCities = len(isConnected)
        visited = [0] * numCities
        numProvinces = 0

        for idx in range(numCities):
            if visited[idx] == 0:
                self.dfs(isConnected, visited, idx)
                numProvinces += 1

        return numProvinces

    def dfs(self, isConnected, visited, idx):
        numCities = len(isConnected)
        visited[idx] = 1

        for jdx in range(numCities):
            if isConnected[idx][jdx] == 1 and visited[jdx] == 0:
                self.dfs(isConnected, visited, jdx)

        return
