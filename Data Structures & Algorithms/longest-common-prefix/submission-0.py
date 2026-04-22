class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini=100000000
        mini_str=""
        ans=""
        for i in strs:
            if len(i)<mini:
                mini=len(i)
                mini_str=i

        for i in range(0,len(mini_str)):
            char=mini_str[i]
            
            for s in strs:
                if s[i] !=char:
                    return mini_str[:i]
        return mini_str            

            
              





            

        