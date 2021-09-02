# 作者：宁方笑
# 开发时间：2021/9/2 20:27
def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (right - left) // 2 + left
        x = matrix[mid // n][mid % n]   # 二维矩阵映射一维公式
        if x > target:
            right = mid - 1
        elif x < target:
            left = mid + 1
        else:
            return True
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))