# 作者：宁方笑
# 开发时间：2021/8/15 21:12
def mutiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    arr = [0] * (m + n)     # 存储结果每一位的列表
    for i in range(m - 1, -1, -1):
        x = int(num1[i])
        for j in range(n - 1, -1, -1):
            arr[i + j + 1] += x * int(num2[j])  # 计算每一位的结果，不考虑进位

    for i in range(m + n - 1, 0, -1):   # 处理进位
        arr[i - 1] += arr[i] // 10
        arr[i] = arr[i] % 10

    index = 1 if arr[0] == 0 else 0
    res = "".join(str(i) for i in arr[index:])
    return res


num1 = "7"
num2 = "8"
print(mutiply(num1, num2))