

class Solution:
    def addOperators(self, num: str, target: int):
        res = []
        ln = len(num)
        def dfs(i, path, cur_num, prevNum):
            if i == ln:
                if cur_num == target:
                    res.append(path)
                return

            for j in range(i, ln):
                # starting with zero?
                if j > i and num[i] == '0':
                    # need to process current number and break.
                    break
                sub_num = int(num[i:j + 1])

                # if cur index is 0 then simple add that number
                if i == 0:
                    dfs(j + 1, path + str(sub_num), cur_num + sub_num, sub_num)
                else:
                    dfs(j + 1, path + "+" + str(sub_num), cur_num + sub_num, sub_num)
                    dfs(j + 1, path + "-" + str(sub_num), cur_num - sub_num, - sub_num)
                    # need to keep the last multiply result.
                    dfs(j + 1, path + "*" + str(sub_num), cur_num - prevNum + prevNum * sub_num, prevNum * sub_num)

        dfs(0, "", 0, 0)
        return res

# time complexity is O(N * 3^N) where N is the length of the string num
# another version of the solution.
# using stack to keep track of the current number, and the previous number to handle the multiply operation.
class Solution:
    def addOperators(self, num: str, target: int):
        res = []
        ln = len(num)
        def dfs(i, path, stack):
            if i == ln:
                if sum(stack) == target:
                    res.append(path)
                return

            for j in range(i, ln):
                # starting with zero?
                if j > i and num[i] == '0':
                    # need to process current number and break.
                    break
                sub_num = int(num[i:j + 1])

                # if cur index is 0 then simple add that number
                if i == 0:
                    stack.append(sub_num)
                    dfs(j + 1, str(sub_num), stack)
                    stack.pop(-1)
                else:
                    stack.append(sub_num)
                    dfs(j + 1, path + "+" + str(sub_num), stack)
                    stack.pop(-1)

                    stack.append(-sub_num)
                    dfs(j + 1, path + "-" + str(sub_num), stack)
                    stack.pop(-1)

                    prev_value = stack.pop(-1)
                    stack.append(prev_value * sub_num)
                    dfs(j + 1, path + "*" + str(sub_num), stack)
                    stack.pop(-1)
                    stack.append(prev_value) # need to add them back to the stack. otherwise the next iteration will lose the previous value.

        dfs(0, "", [])
        return res

# time complexity is O(N * 3^N) where N is the length of the string num
# explain the time complexity and space complexity
# add the space complexity
# add the time complex

num = "105"
target = 5
assert Solution().addOperators(num, target) == ["1*0+5","10-5"]
