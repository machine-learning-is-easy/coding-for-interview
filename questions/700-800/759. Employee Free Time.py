
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # flatten schedule
        events = []
        for employee in schedule:
            for event in employee:
                events.append(event)

        # sort events by start
        events.sort(key=operator.attrgetter('start'))

        # collect result
        res = []
        iterator = iter(events)
        prev_end = next(iterator).end
        for event in iterator:
            if event.start > prev_end:
                res.append(Interval(prev_end, event.start))
            prev_end = max(prev_end, event.end)
        return res