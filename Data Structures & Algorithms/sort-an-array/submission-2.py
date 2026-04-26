class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        n=len(arr)
        
        for i in range(0,n):
            min_index=i
            for j in range(i+1,n):
                if arr[min_index]>arr[j]:
                    min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]  
        return arr      








        