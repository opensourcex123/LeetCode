# 作者：宁方笑
# 开发时间：2021/6/26 11:03
def thirdMax(num):
    set_num=list(set(num))  #集合保证了元素的唯一性
    set_num.sort()
    return set_num[-1] if len(set_num)<3 else set_num[-3]


num=[2, 2, 3, 1]
print(thirdMax(num))

