class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1 
            else:
                freq[i] +=1
            
        res = 0
        maxcount = 0

        for key in freq:
            if freq[key] > maxcount:
                maxcount = freq[key]
                res = key 


        return res