class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = [0]*len(prices)
        min_index = 0
        for i in range(1, len(prices), 1):
            if prices[i-1]<=prices[min_index]:
                min_index = i-1
            arr[i] = prices[i]-prices[min_index]
        max=0
        for n in arr:
            if n>=max:
                max = n
        return max