


class Solution:
    def minSwapsCouples(self, row) -> int:
        # Creating the hashmap for the each element with values of its index in the nums list,
        # so that we can find the index of any element in O(1)
        idxmap = {x: i for i, x in enumerate(row)}
        n = len(row)
        count = 0

        for i in range(0, n, 2):
            # Partner element can be found out by taking the 1 xor of the current element
            # Pair are in the order (even, odd)
            # if current element is odd (assume 5) -> then its partner will be (current XOR 1) (which will be 4)
            # if current element is even (assume 8) -> then its partner will be (current XOR 1) (which will be 9)
            a = row[i]
            # it's patterner is XOR 1
            b = a ^ 1

            # If next element is partner element then move forward
            if row[i + 1] == b:
                continue

            # Otherwise swap the next element with the partner element using the index map
            # Finding the index of b
            idx_b = idxmap[b]

            # Updating the index of next element and b
            idxmap[row[i + 1]] = idx_b
            idxmap[b] = i + 1

            # Swaping the next element and b
            row[idx_b], row[i + 1] = row[i + 1], row[idx_b]

            # Incrementing the count
            count += 1

        return count

row = [0,2,1,3]

assert Solution().minSwapsCouples(row) == 1