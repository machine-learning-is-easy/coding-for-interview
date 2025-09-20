

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(s,p,i) for i,(s,p) in enumerate(tasks)])
        tasks = tasks+[(float('inf'),0,0)]
        res, queue = [], []
        cpu_time = 0 # record what is the current cpu time
        for start, process, i in tasks:
            if start > cpu_time: # if the start time > far, the cup need to run to start time,
                if queue: # still have some process to do
                    # the heap process start time is < start, because of sorting task
                    while queue and start > cpu_time:
                        tmp_process, tmp_ind = heappop(queue)
                        res.append(tmp_ind)
                        cpu_time += tmp_process
                cpu_time = max(cpu_time, start) # after process all process in heap or the cpu time is up to date

            heappush(queue, (process, i))
        return res