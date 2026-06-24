class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for x in s:
            if x in s_dict:
                s_dict[x] +=1
            else:
                s_dict[x] = 1
        for x in t:
            if x in t_dict:
                t_dict[x] +=1
            else:
                t_dict[x] = 1
        for x in s_dict:
            print(x)
            if x not in t_dict or s_dict[x] != t_dict[x]:
                return False
        return True
        