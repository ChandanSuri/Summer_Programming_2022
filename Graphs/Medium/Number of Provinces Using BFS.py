class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        numCities = len(isConnected)
        visited = [0] * numCities
        numProvinces = 0
        queue = list()

        for idx in range(numCities):
            if visited[idx] != 0:
                continue
            queue.append(idx)
            while len(queue) != 0:
                currCity = queue.pop(0)
                visited[currCity] = 1

                for jdx in range(numCities):
                    if isConnected[currCity][jdx] == 1 and visited[jdx] == 0:
                        queue.append(jdx)
            numProvinces += 1

        return numProvinces
