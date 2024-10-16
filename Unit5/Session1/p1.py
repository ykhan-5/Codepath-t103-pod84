#U
#M - queue, array, upper/lower bound
#P -
#I
#R
#E

class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        #append to the array
        self.counter.append(t)

        #use num to set upper and the lower bound
        upper = t
        lower = t - 3000

        count = 0

        for element in self.counter:
            if element <= upper and element >= lower:
                count += 1

        #cound elements in array, in bounds
        return count
        

# RecentCounter recentCounter = new RecentCounter()
recentCounter = RecentCounter()
recentCounter.ping(1);     #// requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   
recentCounter.ping(3001);  #// requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  #// requests = [1, 100, 3001, 3002], range is [2,3002], return 3

    