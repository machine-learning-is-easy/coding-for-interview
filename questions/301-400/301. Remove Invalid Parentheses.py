

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid(string):
            balance = 0
            for char in string:
                if char == '(': balance += 1
                if char == ')': balance -= 1
                if balance < 0: return False
            return balance == 0

        queue = deque([s])
        visited = set([s])
        valid_strings = set()
        found = False

        while queue:
            current = queue.popleft()

            if is_valid(current):
                valid_strings.add(current)
                found = True

            if found:
                continue

            for i in range(len(current)):
                if current[i] not in "()":
                    continue
                new_string = current[:i] + current[i + 1:]
                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return list(valid_strings)


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid(str):
            balance = 0
            for c in str:
                if c == "(":
                    balance += 1
                elif c == ")":
                    balance -= 1

                if balance < 0:
                    return False
            return balance == 0

        queue = [s]
        seen = set([s])
        found = False
        res = set()
        while queue and not found:
            for _ in range(len(queue)):
                cur_s = queue.pop(0)
                if is_valid(cur_s) and cur_s not in res:
                    res.add(cur_s)
                    found = True
                for idx in range(len(cur_s)):
                    if cur_s[idx] in ["(", ")"]:
                        new_s = cur_s[:idx] + cur_s[idx + 1:]
                        if new_s not in seen:
                            queue.append(new_s)
                            seen.add(new_s)
        return list(res)

# time complexity is O(2^n * n). space complexity is O(2^n*n)