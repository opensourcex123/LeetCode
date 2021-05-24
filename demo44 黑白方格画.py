# 作者：宁方笑
# 开发时间：2021/5/8 16:19
def paintingPlan(n, k):
    if k in (0,n*n):
        return 1
    def combination(n,a):   #计算组合数
        res=1
        for i in range(n,n-a,-1):   #还是左闭右开区间
            res*=i
        for j in range(1,a+1):
            res//=j
        return res
    count=0
    for i in range(0,n):
        for j in range(0,n):
            if n*(i+j)-(i*j)==k:
                count=count+combination(n,i)*combination(n,j)   #选择行列乘起来一共多少种方法
    return count

n = 3
k = 8
print(paintingPlan(n,k))