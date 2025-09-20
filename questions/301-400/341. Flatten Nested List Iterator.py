

class NestedIterator:
    def __init__(self, nestedList):
        self.flat_list = []
        self.index = 0
        self._flatten(nestedList)

    def _flatten(self, nestedList):
        for ni in nestedList:
            if ni.isInteger():
                self.flat_list.append(ni.getInteger())
            else:
                self._flatten(ni.getList())

    def next(self):
        val = self.flat_list[self.index]
        self.index += 1
        return val

    def hasNext(self):
        return self.index < len(self.flat_list)