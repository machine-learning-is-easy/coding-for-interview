

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        l = len(digits)
        add = 0

        i = l - 1
        last_add = digits[-1] + 1
        if last_add >= 10:
            add = 1
            digits[-1] = last_add - 10
            j = l - 2
            while j >= 0:
                total = digits[j] + add
                if total >= 10:
                    add = 1
                    digits[j] = total - 10
                    j -= 1
                else:
                    digits[j] = total
                    break
            if add == 1 and j < 0:
                digits.insert(0, 1)

        else:
            add = 0
            digits[-1] = last_add

        return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if not digits:
            return [1]
        carry = 0
        for idx in range(len(digits) - 1, -1, -1):
            if idx == len(digits) - 1:
                add = digits[idx] + 1
            else:
                add = digits[idx]

            res_idx = (add + carry) % 10
            carry = (add + carry) // 10
            digits[idx] = res_idx
        if carry > 0:
            digits = [carry] + digits
        return digits