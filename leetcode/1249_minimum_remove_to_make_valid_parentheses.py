class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        count = 0

        i = 0
        for c in s:
            if c == "(":
                stack.append((c,i))
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    continue
            elif c != "(" and c != ")":
                count += 1
            res.append(c)
            i += 1

        
        while stack:
            curr = stack.pop()
            res[curr[1]] = ""


        return "".join(res)


        
