# 作者：宁方笑
# 开发时间：2021/7/28 21:08
def maxArea(height):
    #双指针
    i=0
    j=len(height)-1

    res=0
    while i!=j:
        area=min(height[i],height[j])*abs(i-j)
        res=max(res,area)
        if height[i]<=height[j]:
            i+=1
        else:
            j-=1
    return res

height=[1,2,1]
print(maxArea(height))