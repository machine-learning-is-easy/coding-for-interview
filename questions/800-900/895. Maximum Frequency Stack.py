

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.groups = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.maxFreq: self.maxFreq = self.freq[val]
        self.groups[self.freq[val]].append(val)

    def pop(self) -> int:
        first = self.groups[self.maxFreq].pop(-1)
        self.freq[first] -= 1
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1

        return first