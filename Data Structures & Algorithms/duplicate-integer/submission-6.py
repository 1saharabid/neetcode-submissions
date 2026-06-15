class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #create set, add each element in list to set
        #if set size == list size, return true
        #else return false 

        mySet = set()

        for num in nums:
            mySet.add(num)
        
        if len(mySet) == len(nums):
            return False
        else:
            return True 