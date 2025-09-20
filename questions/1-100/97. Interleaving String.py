


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def matching_string(s1, s2, long_str):
            # this is a typical recursive function in string matching
            if not s1 and not s2 and not long_str:
                return True
            elif long_str:
                if s1 and s2:
                    # one letter can comes from s1 or comes from s2
                    return (s1[0] == long_str[0] and matching_string(s1[1:], s2, long_str[1:])) or (
                                s2[0] == long_str[0] and matching_string(s1, s2[1:], long_str[1:]))
                elif s1:
                    return s1[0] == long_str[0] and matching_string(s1[1:], s2, long_str[1:])
                elif s2:
                    return s2[0] == long_str[0] and matching_string(s1, s2[1:], long_str[1:])
                else:
                    return False

            else:
                return False

        return matching_string(s1, s2, s3) or matching_string(s2, s1, s3)


# this solution is exactly The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# actually the question is not exactly require one by one. can be two consecutive letters comes from a
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def matching_string(s1, s2, long_str):
            if not s1 and not s2 and not long_str:
                return True
            elif long_str:
                if s1 and s1[0] == long_str[0]:
                    return matching_string(s2, s1[1:], long_str[1:])
                else:
                    return False

        return matching_string(s1, s2, s3) or matching_string(s2, s1, s3)

assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") == True