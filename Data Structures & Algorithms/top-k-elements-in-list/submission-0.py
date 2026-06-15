class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create dict to hold freuency of values and array to 
        #hold values with largest frequencies
        freq = {} 
        result = []

        #iterates through nums and adds values as keys and frequency as value
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num]= 1
        
        #variable declaration
        i = 0
        max_key = 0

        #checks for max value in freq, and adds key to result, 
        #and then deletes from freq
        while i < k:
            max_key = max(freq, key = freq.get)
            result.append(max_key)
            del freq[max_key]
            i += 1


        return result
        