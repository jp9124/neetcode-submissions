class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for x in tokens:
            print(res)
            res.append(x)
            ans = ""
            if res[-1] == "+":
                ans = int(res[-3]) + int(res[-2])
                res.pop()
                res.pop()
                res.pop()
            
            elif res[-1] == "-":
                ans = int(res[-3]) - int(res[-2])
                res.pop()
                res.pop()
                res.pop()
            elif res[-1] == "*":
                ans = int(res[-3]) * int(res[-2])
                res.pop()
                res.pop()
                res.pop()
            elif res[-1] == "/":
                ans = math.trunc(int(res[-3]) / int(res[-2]))
                res.pop()
                res.pop()
                res.pop()
            if ans != "":
                res.append(f"{ans}")
        return int(res[0])