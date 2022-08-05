from collections import defaultdict
from random import random


class RandomizedCollection(object):

    def __init__(self):
        self.hashedElems = defaultdict(set)
        self.elems = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        self.hashedElems[val].add(len(self.elems))
        self.elems.append(val)

        return len(self.hashedElems[val]) == 1

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashedElems:
            return False

        valIdx = self.hashedElems[val].pop()
        lastElem = self.elems[-1]
        self.elems[valIdx] = lastElem
        self.hashedElems[lastElem].add(valIdx)
        self.hashedElems[lastElem].remove(len(self.elems) - 1)
        self.elems.pop()
        if len(self.hashedElems[val]) == 0:
            del self.hashedElems[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        randomElem = random.choice(self.elems)
        return randomElem

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
