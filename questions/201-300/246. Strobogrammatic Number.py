
# pay attention to the even and odd length.
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapper = {
            "0":"0",
            "6": "9",
            "8": "8",
            "9": "6",
            "1":"1"
        }

        l, r = 0, len(num) - 1
        while l < r:
            if num[l] in mapper:
                if mapper[num[l]] != num[r]:
                    return False
            else:
                return False
            l += 1
            r -= 1
        if l == r: # odd length, check the middle element.
            if num[l] not in ["0", '8', "1"]:
                return False
        return True