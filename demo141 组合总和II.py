# 作者：宁方笑
# 开发时间：2021/8/14 21:07
import collections

def combinationSum2(candidates, target):
    def dfs(pos, rest):
        nonlocal sequence
        if rest == 0:
            ans.append(sequence[:])
            return
        if pos == len(freq) or rest < freq[pos][0]:
            return

        dfs(pos + 1, rest)

        most = min(rest // freq[pos][0], freq[pos][1])
        for i in range(1, most + 1):
            sequence.append(freq[pos][0])
            dfs(pos + 1, rest - i * freq[pos][0])
        sequence = sequence[: -most]
    freq = sorted(collections.Counter(candidates).items())
    ans = []
    sequence = []
    dfs(0, target)
    return ans


candidates = [2,5,1,6,7,10,1]
target = 8
print(combinationSum2(candidates, target))