class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1=[]
        for i in range(0,len(nums)):
            if nums[i] not in list1:
                list1.append(nums[i])
            else:
                return True    
        return False        


              

        