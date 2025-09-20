

from collections import OrderedDict, defaultdict

class LFUCache:
    
     def __init__(self, capacity: int):
         self.key2value_freq = {}
         self.freq_bins = defaultdict(OrderedDict)  # {freq: {key:value}}
         self.capacity = capacity
         self.min_freq = 0
    
     def get(self, key: int, new_value=None) -> int:
         if key in self.key2value_freq:
             value, freq = self.key2value_freq.pop(key)
             if new_value:
                 value = new_value
             self.freq_bins[freq].pop(key)
             self.freq_bins[freq + 1][key] = value
             self.key2value_freq[key] = [value, freq + 1]
             while not self.freq_bins.get(self.min_freq):
                self.min_freq += 1
             return value
         else:
             return -1
    
     def put(self, key: int, value: int) -> None:
         if not self.capacity:
             return
    
         if key in self.key2value_freq:
             self.get(key, value)
         else:
             if len(self.key2value_freq) == self.capacity:
                 pop_key, pop_value = self.freq_bins[self.min_freq].popitem(last=False)
                 del self.key2value_freq[pop_key]
    
             self.key2value_freq[key] = [value, 1]
             self.freq_bins[1][key] = value
             self.min_freq = 1
             
lfu = LFUCache(2)
lfu.put(1, 1);   # cache=[1,_], cnt(1)=1
lfu.put(2, 2);   # cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      # return 1
                 # cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 # cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      # return -1 (not found)
lfu.get(3);      # return 3
                 # cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 # cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      # return -1 (not found)
lfu.get(3);      # return 3
                 # cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      # return 4
                 # cache=[4,3], cnt(4)=2, cnt(3)=3