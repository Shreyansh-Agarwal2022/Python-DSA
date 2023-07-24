import time

start_time = time.time()

board=[[0 for x in range(8)] for y in range(8)]
def print_board(board):
    for i in range(len(board)):
        for j in range(2*len(board[0])):
            print("-",end=" ")
        print("-")
        print("| ",end="")
        for j in range(len(board[0])):
            print(board[i][j],end=" | ")
        print()
    for j in range(2*len(board[0])):
        print("-",end=" ")
    print()

def neighbours(board, point):
    result = []
    row, col = point
    offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for dr, dc in offsets:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[0]):
            result.append((r, c))
    return result
def explore(board,initial,target):
    board[initial[0]][initial[1]]=1
    queue=[initial]
    while queue:
        point=queue.pop(0)
        print(point,neighbours(board,point))
        for (x,y) in neighbours(board,point):
            if board[x][y]==0:
                board[x][y]=1
                queue.append((x,y))
    return(board[target[0]][target[1]]!=0)
print(explore(board,(1,1),(1,2)))
print_board(board)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")