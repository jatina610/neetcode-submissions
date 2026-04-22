class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict1={}
        i=0
        for j in nums:
            compliment=target-j
            if compliment in dict1:
                return [dict1[compliment],i]
            dict1[j]=i
            i=i+1    



            

            


        