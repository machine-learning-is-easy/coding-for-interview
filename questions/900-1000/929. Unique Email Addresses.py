

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        emails_list = []
        for email in emails:
            s_list = email.split("@")
            s = ''
            for c in s_list[0]:
                if c == "+":
                    break
                elif c == '.':
                    pass
                else:
                    s += c
            m = s + '@' + s_list[1]

            if m not in emails_list:
                emails_list.append(m)

        return len(emails_list)
