

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # tricky ****
        s_list = S.split("-")
        if all([len(s) == K for ind, s in enumerate(s_list)]):
            return str.upper(S)
        else:
            # reverse string first, counting letters from the end to start
            reverse_string = S[::-1]
            s_list = reverse_string.split("-")
            ind = 0
            while ind < len(s_list):
                if s_list[ind] == '':
                    ind += 1
                else:
                    if len(s_list[ind]) < K and ind < len(s_list) - 1:
                        sub_ind = ind + 1
                        while sub_ind < len(s_list) and K != len(s_list[sub_ind]):
                            d = K - len(s_list[ind])
                            s_list[ind] = s_list[ind] + s_list[sub_ind][0:d]
                            s_list[sub_ind] = s_list[sub_ind][d:]
                            sub_ind += 1
                        ind += 1
                    elif len(s_list[ind]) > K:
                        tmp = s_list[ind]
                        s_list[ind] = tmp[:K]
                        s_list.insert(ind + 1, tmp[K:])
                    else:
                        ind += 1
            s = "-".join([str.upper(c) for c in s_list if c != ''])
            return s[::-1]

