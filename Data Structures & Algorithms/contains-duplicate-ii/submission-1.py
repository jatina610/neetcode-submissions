class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        
        n=len(nums)
        while(i<n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and j-i<=k:
                    return True
            i=i+1        
        return False        
            
                

                
                
        