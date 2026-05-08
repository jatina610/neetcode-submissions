class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        list1=[]
        for i in range(0,len(nums)):
            prod=1
            for j in range(0,len(nums)):
                if i!=j:
                    prod=prod*nums[j]
            list1.append(prod)

        return list1            
                    







                


            



        