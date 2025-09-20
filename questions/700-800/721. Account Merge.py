

import collections
class Solution:
    def accountsMerge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans


class Solution:
    def accountsMerge(self, accounts):

        email_graph = collections.defaultdict(set)
        name = collections.defaultdict()
        # create a graph of email
        for acc in accounts:
            name[acc[1]] = acc[0]
            for email in acc[1:]:
                email_graph[acc[1]].add(email)
                email_graph[email].add(acc[1])

        res = []
        seen = set()
        for email in email_graph:
            if email not in seen:
                queue = [email]
                seen.add(email)
                search = set(email)
                current_name = name.get(email, '')
                while queue:
                    current_email = queue.pop(0)
                    for next_email in email_graph.get(current_email, []):
                        if next_email not in seen:
                            queue.append(next_email)
                            search.add(next_email)
                            seen.add(next_email)
                            if email in name:
                                current_name = name[email]
                print(search)
                res.append([current_name] + sorted(list(search)))

        return res

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

# assert Solution().accountsMerge(accounts) == [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts):

        email_graph = defaultdict(set)
        account_name = dict()

        for acc in accounts:
            name = acc[0]
            anchor_email = acc[1]
            account_name[anchor_email] = name
            for email in acc[1:]:
                email_graph[anchor_email].add(email)
                email_graph[email].add(anchor_email)

        seen = set()
        res = []
        for email in email_graph:
            if email not in seen:
                search = set([email])
                seen.add(email)
                queue = [email]
                name = account_name.get(email, "")
                while queue:
                    node = queue.pop(0)
                    for neighbor in email_graph.get(node, []):
                        if neighbor not in seen:
                            seen.add(neighbor)
                            queue.append(neighbor)
                            search.add(neighbor)
                            if neighbor in account_name:
                                name = account_name[neighbor]
                res.append([name] + sorted(list(search)))

        return res

accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]

assert Solution().accountsMerge(accounts) == [["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co"],["Ethan","Ethan0@m.co","Ethan3@m.co"],["Gabe","Gabe0@m.co","Gabe2@m.co","Gabe3@m.co","Gabe4@m.co"],["Kevin","Kevin2@m.co","Kevin4@m.co"]]