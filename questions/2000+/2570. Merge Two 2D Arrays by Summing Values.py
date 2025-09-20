

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged = {}

        for id_, val in nums1:
            merged[id_] = merged.get(id_, 0) + val

        for id_, val in nums2:
            merged[id_] = merged.get(id_, 0) + val

        return sorted([[id_, val] for id_, val in merged.items()])


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        merged = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] < nums2[j][0]:
                merged.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                merged.append(nums2[j])
                j += 1
            else:
                merged.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        return merged

