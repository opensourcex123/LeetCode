# 作者：宁方笑
# 开发时间：2021/7/31 21:12
class Solution:
    VALUE_SYMBOLS=[ #表是从大到小排序的
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    def intToRoman(self,num):
        res=[]
        for value,symbol in Solution.VALUE_SYMBOLS:
            while num>=value:   #每次挑表中最大的即可
                num-=value
                res.append(symbol)
            if num<=0:
                break
        return "".join(res)

sol=Solution()
nums=58
print(sol.intToRoman(nums))