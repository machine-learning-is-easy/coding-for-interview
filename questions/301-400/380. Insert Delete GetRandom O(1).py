

class RandomizedSet:

    def __init__(self):
        self.val_list = []

    def insert(self, val: int) -> bool:
        if val in self.val_list:
            return False
        else:
            self.val_list.append(val)
            return True

    def remove(self, val):
        if val not in self.val_list:
            return False
        else:
            index = self.val_list.index(val)
            self.val_list.pop(index)
            return True

    def getRandom(self):
        index = floor(random.random() * len(self.val_list))
        return self.val_list[index]


class RandomizedSet:

    def __init__(self):
        self.ran = set()
    def insert(self, val: int) -> bool:
        if val not in self.ran:
            self.ran.add(val)
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.ran:
            self.ran.remove(val)
            return True
        else:
            return False
    def getRandom(self) -> int:

        class RandomizedSet:
            def __init__(self):
                self.element_list = list()
                self.val2index = dict()

            def insert(self, val: int) -> bool:
                if val in self.val2index:
                    return False
                else:
                    val_index = len(self.element_list)
                    self.element_list.append(val)
                    self.val2index[val] = val_index
                    return True

            def remove(self, val: int) -> bool:
                if val in self.val2index:
                    val_index = self.val2index[val]
                    if val_index == len(self.element_list) - 1:
                        self.element_list.pop(-1)
                        del self.val2index[val]
                    else:
                        last_val = self.element_list[-1]
                        last_val_index = self.val2index[last_val]
                        self.element_list[val_index] = last_val
                        self.element_list.pop(-1)
                        self.val2index[last_val] = val_index
                        del self.val2index[val]
                    return True
                else:
                    return False

            def getRandom(self) -> int:
                return random.choice(self.element_list)