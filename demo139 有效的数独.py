# 作者：宁方笑
# 开发时间：2021/8/12 21:22
def isValidSudoku(board):
    row = [{} for i in range(9)]
    col = [{} for i in range(9)]
    box = [{} for i in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                num = int(num)
                box_index = (i // 3) * 3 + j // 3

                row[i][num] = row[i].get(num, 0) + 1 #第二个参数是默认值，即所找的键不存在时，返回默认值
                col[j][num] = col[j].get(num, 0) + 1
                box[box_index][num] = box[box_index].get(num, 0) + 1

                if row[i][num] > 1 or col[j][num] > 1 or box[box_index][num] > 1:
                    return False
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))