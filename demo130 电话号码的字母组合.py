# 作者：宁方笑
# 开发时间：2021/8/3 20:51
def letterCombinations(digits):
    if not digits:
        return list()
    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(index):   #回溯法
        if index==len(digits):
            combinations.append("".join(combination))
        else:
            digit=digits[index]
            for letter in phoneMap[digit]:
                combination.append(letter)
                backtrack(index+1)
                combination.pop()
    combinations=list()
    combination=list()
    backtrack(0)
    return combinations

digits = "23"
print(letterCombinations(digits))