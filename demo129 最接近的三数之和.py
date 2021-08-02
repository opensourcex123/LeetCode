# 作者：宁方笑
# 开发时间：2021/8/2 21:08

def threeSumClosed(nums, target):
    n = len(nums)
    nums.sort()
    best = 10 ** 7

    def update(cur):
        nonlocal best
        if abs(cur - target) < abs(best - target):
            best = cur

    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        second, third = first + 1, n - 1
        while second < third:
            s = nums[first] + nums[second] + nums[third]
            if s == target:
                return target
            update(s)
            if s > target:
                third0 = third - 1
                while second < third0 and nums[third0] == nums[third]:
                    third0 -= 1
                third = third0
            else:
                second0 = second + 1
                while second0 < third and nums[second0] == nums[second]:
                    second0 += 1
                second = second0
    return best


nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosed(nums, target))
