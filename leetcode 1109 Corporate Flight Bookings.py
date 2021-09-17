class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output = [0] * (n + 1)
        for s, e, count in bookings:
            output[s-1] += count
            output[e] -= count

        for i in range(1, len(output)):
            output[i] += output[i-1]

        return output[:-1] 
