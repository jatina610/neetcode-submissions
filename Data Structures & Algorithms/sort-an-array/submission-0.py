class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        n=len(arr)
        temp=0
        


        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    # swap
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr






        