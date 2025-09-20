

class Solution:
    def carPooling(self, trips, capacity: int) -> bool:

        take = []
        drop = []

        for n, f, t in trips:
            take.append((f, n))
            drop.append((t, n))

        take.sort()
        drop.sort()

        t_ind = 0
        d_ind = 0
        n_passenger = 0

        while t_ind < len(take) or d_ind < len(drop):
            if t_ind < len(take):
                t_time = take[t_ind][0]
            else:
                t_time = float("inf")

            if d_ind < len(take):
                d_time = drop[d_ind][0]
            else:
                d_time = float("inf")

            if t_time < d_time:
                n_passenger += take[t_ind][1]
                t_ind += 1
            else:
                n_passenger -= drop[d_ind][1]
                d_ind += 1

            if n_passenger > capacity:
                return False

        return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        take = []
        drop = []

        for passengers, start, end in trips:
            take.append((start, passengers))
            drop.append((end, passengers))
        take.sort()
        drop.sort()

        trip_passengers = 0
        take_ind = 0
        drop_ind = 0
        while take_ind < len(take) and drop_ind < len(drop):
            if take[take_ind][0] < drop[drop_ind][0]:
                trip_passengers += take[take_ind][1]
                take_ind += 1
            else: # drop first, if the drop time and take time are the same, drop first. then take.
                trip_passengers -= drop[drop_ind][1]
                drop_ind += 1

            if trip_passengers > capacity:
                return False

        return True


trips = [[9,3,4],[9,1,7],[4,2,4],[7,4,5]]
capacity = 23

assert Solution().carPooling(trips, capacity) == True
