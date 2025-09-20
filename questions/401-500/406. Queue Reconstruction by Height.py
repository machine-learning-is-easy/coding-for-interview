

class Solution:
    def reconstructQueue(self, people):
        N = len(people)
        people.sort(key=lambda x: (x[0], -x[1]))
        # need to process the higher index then the lower index, otherwise the higher index will have out of index error
        # people.sort(key=lambda x: x[0])
        position = list(range(N))  # record the all the index of people is not processed

        res = [None] * len(people)
        for i in range(len(people)):
            # the second value of the people should be the index of res not including processed element.
            res[position[people[i][1]]] = people[i]
            position.pop(people[i][1])  # remove the people[i][1], as it is already processed.

        return res

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

assert Solution().reconstructQueue((people)) == [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]