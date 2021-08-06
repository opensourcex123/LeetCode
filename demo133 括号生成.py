# 作者：宁方笑
# 开发时间：2021/8/6 21:22
def generateParenthesis(n): #回溯法
    res = []

    def backtrack(S, left, right):
        if len(S) == 2 * n:
            res.append("".join(S))
        if left < n:
            S.append('(')
            backtrack(S, left + 1, right)
            S.pop()
        if right < left:    #右括号如果比左括号少
            S.append(')')
            backtrack(S, left, right + 1)
            S.pop()

    S = []
    backtrack(S, 0, 0)
    return res

n=1
print(generateParenthesis(n))