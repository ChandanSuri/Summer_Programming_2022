from random import random


class RandomizedSet(object):

    def __init__(self):
        self.hashedElems = {}
        self.elems = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashedElems:
            return False

        self.hashedElems[val] = len(self.elems)
        self.elems.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashedElems:
            return False

        valIdx = self.hashedElems[val]
        lastElem = self.elems[-1]
        self.elems[valIdx] = lastElem
        self.hashedElems[lastElem] = valIdx
        self.elems.pop()
        del self.hashedElems[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        randomElem = random.choice(self.elems)
        return randomElem

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
