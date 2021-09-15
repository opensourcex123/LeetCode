# 作者：宁方笑
# 开发时间：2021/9/15 21:13
def restoreIpAddresses(s):
    SEG_COUNT = 4
    res = list()
    segments = [0] * SEG_COUNT

    def dfs(segId, segStart):
        if segId == SEG_COUNT:
            if segStart == len(s):
                ipAddr = '.'.join(str(seg) for seg in segments)
                res.append(ipAddr)
            return

        if segStart == len(s):
            return

        if s[segStart] == "0":
            segments[segId] = 0
            dfs(segId + 1, segStart + 1)

        addr = 0
        for segEnd in range(segStart, len(s)):
            addr = addr * 10 + (ord(s[segEnd])) - ord("0")
            if 0 < addr <= 0xFF:
                segments[segId] = addr
                dfs(segId + 1, segEnd + 1)
            else:
                break

    dfs(0, 0)
    return res