class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # want to acomplish in one forloop, so it's O(n), use dict
        # in loop, subtract list[i] from target, see if that val
        # in dict. if yes, return indiced. if not, add list[i] to 
        # dict and move on to next list item until end 
        # edge cases, negative ints  

        dictionary = {}
        diff = 0;
        indices = []
        for i in range(len(nums)):
            #if nums[i] >= 0:
                diff = target - nums[i]
                if diff in dictionary:
                    # return indices
                    indices.append(dictionary[diff]) # found first
                    indices.append(i) # found second
                    return indices
                else:
                    # add to dictionary
                    # key: nums[i], value: i
                    dictionary[nums[i]] = i

           # if nums[i] < 0:

                

            

        