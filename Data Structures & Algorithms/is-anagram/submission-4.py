class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for j in t:
            if j in dict1:
                dict1[j]-=1

        for k in dict1:
            if dict1[k]>0:
                return False
        return True        

                        
        