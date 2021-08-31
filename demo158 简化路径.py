# 作者：宁方笑
# 开发时间：2021/8/31 20:58
def simplifyPath(path):
    source = path.split("/")
    res = []
    for i in range(len(source)):
        if source[i] == "..":
            if res:
                res.pop()
        elif source[i] == "." or source[i] == "":
            continue
        else:
            res.append(source[i])
    return "/" + "/".join(res)


path = "/a/./b/../../c/"
print(simplifyPath(path))