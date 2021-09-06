# 作者：宁方笑
# 开发时间：2021/9/6 21:05
def exist(board, word): # 回溯法
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def check(i, j, k):
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        visited.add((i, j))
        res = False
        for di, dj in directions:
            newi, newj = i + di, j + dj
            if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                if (newi, newj) not in visited:
                    if check(newi, newj, k + 1):
                        res = True
                        break
        visited.remove((i, j))
        return res

    h, w = len(board), len(board[0])
    visited = set()
    for i in range(h):
        for j in range(w):
            if check(i, j, 0):
                return True
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))