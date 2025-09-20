
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lv1 = version1.split('.')
        lv2 = version2.split('.')
        leng = max(len(lv1), len(lv2))

        for i in range(leng):
            v1 = int(lv1[i]) if i < len(lv1) else 0
            v2 = int(lv2[i]) if i < len(lv2) else 0
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        return 0