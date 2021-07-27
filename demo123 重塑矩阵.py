# 作者：宁方笑
# 开发时间：2021/7/27 21:25
def matrixReshape(mat,r,c):
    r0=len(mat)
    c0=len(mat[0])
    if r*c>r0*c0:
        return mat
    res=[[0]*c]*r

    for x in range(r0*c0):
        res[x//c][x%c]=mat[x//c0][x%c0] #矩阵之间的对应关系，对应一维矩阵
    return res

nums=[[1,2],
 [3,4]]
r = 1
c = 4
print(matrixReshape(nums,r,c))