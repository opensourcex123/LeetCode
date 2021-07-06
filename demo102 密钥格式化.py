# 作者：宁方笑
# 开发时间：2021/7/6 9:51
def licenseKeyFormatting(str, k):
    tmp = ''.join(str.upper().split('-'))[::-1]  # 首先将字符串大写逆序
    # print(tmp)
    tmp_new = [tmp[i:i + k] for i in range(0, len(tmp), k)]  # 然后根据k，得到切割后的列表
    res = '-'.join(tmp_new)[::-1]  # 最后逆序回来，并添加分隔符
    return res


S = "5F3Z-2e-9-w"
K = 4
print(licenseKeyFormatting(S, K))
