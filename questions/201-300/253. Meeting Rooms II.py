

class Solution:
    def minMeetingRooms(self, intervals) -> int:

        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        rooms = 0
        max_room = 0
        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])

        start_pointer = 0
        end_pointer = 0

        while start_pointer < len(intervals):
            rooms += 1
            while start_timings[start_pointer] >= end_timings[end_pointer]:
                rooms -= 1
                end_pointer += 1

            start_pointer += 1
            max_room = max(max_room, rooms)

        return max_room


'''
The meeting timings given to us define a chronological order of events throughout the day. We are given the start and end timings for the meetings which can help us define this ordering.

Arranging the meetings according to their start times helps us know the natural order of meetings throughout the day. However, simply knowing when a meeting starts doesn't tell us much about its duration.

We also need the meetings sorted by their ending times because an ending event essentially tells us that there must have been a corresponding starting event and more importantly, an ending event tell us that a previously occupied room has now become free.

A meeting is defined by its start and end times. However, for this specific algorithm, we need to treat the start and end times individually. This might not make sense right away because a meeting is defined by its start and end times. If we separate the two and treat them individually, then the identity of a meeting goes away. This is fine because:

When we encounter an ending event, that means that some meeting that started earlier has ended now. We are not really concerned with which meeting has ended. All we need is that some meeting ended thus making a room available.

Let us consider the same example as we did in the last approach. We have the following meetings to be scheduled: (1, 10), (2, 7), (3, 19), (8, 12), (10, 20), (11, 30). As before, the first diagram show us that the first three meetings are colliding with each other and they have to be allocated separate rooms.
'''


# algorithm 2:
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start_time = sorted([interval[0] for interval in intervals])
        end_time = sorted([interval[1] for interval in intervals])

        start_ind = 0
        end_ind = 0
        rooms = 0
        max_room = 0

        while start_ind < len(intervals):

            if start_time[start_ind] < end_time[end_ind]:
                rooms += 1
                start_ind += 1
            else:
                rooms -= 1
                end_ind += 1

            max_room = max(max_room, rooms)

        return max_room
"""

"""
meetings = [[26,29],[19,26],[19,28],[4,19],[4,25]]
assert Solution().minMeetingRooms(meetings) == 3