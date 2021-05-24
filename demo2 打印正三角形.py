# 作者：宁方笑
# 开发时间：2021/3/2 11:55
n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for k in range(1,2*i):
        print("*",end="")
    print(end="\n")