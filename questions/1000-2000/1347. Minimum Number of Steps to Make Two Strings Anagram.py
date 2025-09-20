

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        # using dict to finish the convertion

        def convert_dict(s):
            str_dict = {}
            for ind, s in enumerate(s):
                if s in str_dict:
                    str_dict[s] += 1
                else:
                    str_dict[s] = 1
            return str_dict

        s_dict = convert_dict(s)
        t_dict = convert_dict(t)

        steps = 0

        keys = list(set(list(s_dict) + list(t_dict)))
        for key in keys:
            if key in t_dict and key in s_dict:
                steps += abs(t_dict[key] - s_dict[key])
            elif key in t_dict:
                steps += t_dict[key]
            elif key in s_dict:
                steps += s_dict[key]

        return steps / 2