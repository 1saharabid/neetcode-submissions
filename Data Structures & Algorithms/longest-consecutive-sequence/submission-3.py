class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(nums)
        recur = 1
        maxFreq = 1
        if len(sort) == 0:
            return 0

        # count length of numbers reoccurring in for loop, save highest number
        for i in range(len(sort) - 1):
            firstNum = sort[i]
            numNext = sort[i + 1]
            if firstNum + 1 == numNext:
                recur += 1
            elif firstNum == numNext:
                 continue
            else:
                maxFreq = max(recur, maxFreq)
                recur = 1

        maxFreq = max(recur, maxFreq)
        return maxFreq