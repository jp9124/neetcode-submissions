class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for x in s:
            arr.append(x)
            if len(arr) >=2 and ((arr[-1] == "]" and arr[-2] == "[") or  (arr[-1] == "}" and arr[-2] == "{") or (arr[-1] == ")" and arr[-2] == "(")):
                arr.pop()
                arr.pop()
        return arr == []