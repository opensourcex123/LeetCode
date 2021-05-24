# 作者：宁方笑
# 开发时间：2021/4/7 10:09
class Solution:
    def countAndSay(self,n):
        res='1'
        if n==1:
            return res
        cnt=2
        while cnt<=n:
            res=self.count(res)
            cnt+=1
        return res

    def count(self,s):
        freq=1
        res=''
        pre=s[0]
        for i in range(1,len(s)):
            if s[i]!=pre:
                res+=str(freq)+pre
                pre=s[i]
                freq=1
            else:
                freq+=1
        res+=str(freq)+pre
        return res

obj=Solution()
print(obj.countAndSay(20))