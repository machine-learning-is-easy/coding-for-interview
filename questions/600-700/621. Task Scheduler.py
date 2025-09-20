

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task = Counter(tasks)
        cpu_time = 0
        idle_time = dict()
        sorted_keys = sorted(task.items(), key=operator.itemgetter(1), reverse=True)
        sorted_keys = [key for key, _ in sorted_keys]

        while task:
            for key in list(sorted_keys):
                if key in idle_time:
                    if cpu_time >= idle_time.get(key):
                        cpu_time += 1
                    else:
                        cpu_time = idle_time.get(key)
                        cpu_time += 1
                else:
                    cpu_time += 1

                idle_time[key] = cpu_time + n

                task[key] -= 1
                if task[key] == 0:
                    del task[key]
                    sorted_keys.remove(key)

        return cpu_time


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        max_heap = [(-cnt, task) for task, cnt in freq.items()]
        heapq.heapify(max_heap)

        queue = deque()  # stores (available_time, -count, task)
        time = 0

        while max_heap or queue:
            time += 1

            if max_heap:
                cnt, task = heapq.heappop(max_heap)
                cnt += 1  # since cnt is negative
                if cnt != 0:
                    queue.append((time + n, cnt, task))  # cool down

            if queue and queue[0][0] == time:
                _, cnt, task = queue.popleft()
                heapq.heappush(max_heap, (cnt, task))

        return time