import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        hi, lo = max(piles), 1 
        k = max(piles)

        while lo <= hi : 

            mid = (hi + lo)//2

            total_hours = 0

            for pile in piles:
                total_hours+=math.ceil(pile / mid)

            if total_hours <= h:
                k = mid 
                hi = mid - 1
            
            else:
                lo = mid + 1

        return k

#### NOTES ####
## Time Complexity : O (log n * M)
## space complexity : O(1)
## key takeaways: we are not searching the pile. The crux is total_hours being ceil(p / k) or p//k + int( p / k) - time taken per pile
## after that, it is easy to see why the ends move the way they do. larger the h, smaller the k can be
## probelm gaurantees that there will be a splution, i.e, h > length of the piles