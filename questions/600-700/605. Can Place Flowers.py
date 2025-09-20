

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # think about the out of index error of all the list

        total_flowers = 0
        if not flowerbed:
            return False

        for ind, fb in enumerate(flowerbed):
            if flowerbed[ind] == 0:
                if ind - 1 >= 0 and ind + 1 <= len(flowerbed) - 1:
                    if flowerbed[ind - 1] == 0 and flowerbed[ind + 1] == 0:
                        total_flowers += 1
                        flowerbed[ind] = 1
                elif ind - 1 < 0 and ind + 1 < len(flowerbed):
                    if flowerbed[ind + 1] == 0:
                        total_flowers += 1
                        flowerbed[ind] = 1
                else:
                    if flowerbed[ind - 1] == 0:
                        total_flowers += 1
                        flowerbed[ind] = 1

        if total_flowers >= n:
            return True
        else:
            return False

# another versio of counting zeros.
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        zeros = 1
        for ind, v in enumerate(flowerbed):
            if v == 1:
                zeros = 0
            else:
                if zeros == 1:
                    # try to place flowers
                    if ind + 1 < len(flowerbed):
                        if flowerbed[ind + 1] == 0:
                            n -= 1
                            if n == 0:
                                return True
                            zeros = 0
                        else:
                            zeros = 0
                    else:
                        n -= 1
                        if n == 0:
                            return True
                        else:
                            return False

                else:
                    zeros += 1

        return False

# more concise version of the above code.
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        idx = 0
        count = 0
        while idx < len(flowerbed):
            if flowerbed[idx] == 0:
                zero = 0
                if idx - 1 < 0 or flowerbed[idx - 1] == 0:
                    zero += 1
                if idx + 1 >= len(flowerbed) or flowerbed[idx + 1] == 0:
                    zero += 1

                if zero == 2:
                    count += 1
                    flowerbed[idx] = 1
            idx += 1
        return count >= n