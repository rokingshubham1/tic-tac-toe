import random, os

board = [['-' for _ in range(3)] for _ in range(3)]
scores = {
    'X' : -1,
    'O' : 1,
    'tie' : 0
}

#shubham jaishwal tic tac toe game 

# --------------------------------------------- #
def whoHasWon():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return str(board[i][0])    
        if board[0][i] == board[1][i] == board[2][i]:
            return str(board[0][i])   

    if board[0][0] == board[1][1] == board[2][2] :
        return str(board[0][0])   
    elif board[2][0] == board[1][1] == board[0][2] :
        return str(board[2][0])   
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-' :
                    return '-'  
    return 'tie'

def checkIfGameOver():
    # print board
    os.system('cls')
    for i in range(3):
        for j in range(3):
            print(board[i][j],end="\t")
        print()
        
    # check if game is over
    gameover = 'tie'
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            gameover = str(board[i][0])    
        if board[0][i] == board[1][i] == board[2][i]:
            gameover = str(board[0][i])   
    if gameover == 'tie':
        if board[0][0] == board[1][1] == board[2][2] :
            gameover = str(board[0][0])   
        elif board[2][0] == board[1][1] == board[0][2] :
            gameover = str(board[2][0])   
        else:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '-' :
                        gameover = '-'  
    if gameover == 'tie':
        print("tie")
        exit()
    elif gameover == '-':
        pass
    else:
        print(gameover thanks +" wins!!")
        exit()
# --------------------------------------------- #


#  *********************************************** #
def placeAiMove():
    bestScore = -99999
    bestMove = [ 0,0 ]
    for i in range(3):
        for j in range(3):
            # is spot available???
            if board[i][j] == '-':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = '-'
                if score > bestScore :
                    bestScore = score
                    bestMove[0] = i
                    bestMove[1] = j
    return bestMove[0], bestMove[1]


def minimax(board, depth, isMax):
    result = whoHasWon()
    if result != '-':
        return scores[str(result)]

    if isMax:
        bestScore = -99999
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score = minimax(board, depth+1, False)
                    board[i][j] = '-'
                    bestScore = max( score, bestScore )
        return bestScore
    else:
        bestScore = 99999
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score = minimax(board, depth+1, True)
                    board[i][j] = '-'
                    bestScore = min( score, bestScore )
        return bestScore





#  *********************************************** #




# Loop for the turns
# --------------------------------------------- #
while True:
    # ---------
    checkIfGameOver()
    # ---------

    print("x, y : ",end="")
    x, y = [int(x) for x in input().split()]
    board[x-1][y-1] = 'X'

    # ---------
    checkIfGameOver()
    # ---------
    
    placex, placey = placeAiMove()
    board[placex][placey] = 'O'

# --------------------------------------------- #
    



