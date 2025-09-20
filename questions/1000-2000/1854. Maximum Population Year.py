

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        births = sorted([birth for birth, _ in logs])
        deaths = sorted([death for _, death in logs])

        i = j = 0
        curr_population = 0
        max_population = 0
        earliest_year = 0

        while i < len(births):
            if births[i] < deaths[j]:
                curr_population += 1
                if curr_population > max_population:
                    max_population = curr_population
                    earliest_year = births[i]
                i += 1
            else:
                curr_population -= 1
                j += 1

        return earliest_year


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = defaultdict(int)
        for birth, death in logs:
            population[birth] += 1
            population[death] -= 1

        years = sorted(list(population.keys()))
        max_y = 0
        max_p = 0
        max_year = 0
        cur_p = 0

        for year in years:
            cur_p += population[year]
            if cur_p > max_p:
                max_p = cur_p
                max_y = year
        return max_y