class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        
        i=0
        j=1
        while(j<len(nums)):
            if nums[i]==nums[j]:

                return True
            else:
                i=i+1
                j=j+1
                

        return False  




        """flag=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]!=nums[j]:
                    flag=0
                else:
                    flag=1
        if flag==0:
            return False
        else:
            return True"""                    

                    
                        
         