

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        mp = collections.defaultdict(int)
        for ind, num in enumerate(nums):
            if num in mp:
                if abs(ind - mp[num]) <= k:
                    return True
                else:
                    mp[num] = ind  # don't need to add to the map if need two indeices >= k
            else:
                mp[num] = ind

        return False