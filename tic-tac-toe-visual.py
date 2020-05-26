import pygame, random
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Ariel', 200)

board = [['-' for _ in range(3)] for _ in range(3)]
scores = {
    'X' : -1,
    'O' : 1,
    'tie' : 0
}



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
        text = font.render('Tie', 1, (255,0,0))
        screen.blit(text, ( 200, 200 ))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        pygame.quit()
    elif gameover == '-':
        pass
    else:
        text = font.render(str(gameover)+" wins!!", 1, (255,0,0))
        screen.blit(text, ( 20, 200 ))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        pygame.quit()
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







# PYGAME STUFF ----------------------------------------------------- #

def drawboard():
    for i in range(3):
        pygame.draw.line(screen, (0,0,0), ((i+1)*(600/3), 0), ((i+1)*(600/3), 600), 1)
    for i in range(3):
        pygame.draw.line(screen, (0,0,0), (0, (i+1)*(600/3)), (600, (i+1)*(600/3)), 1)


def redraw():
    screen.fill((255,255,255))
    drawboard()
    for i in range(3):
        for j in range(3):
            if board[i][j] != '-':
                text = font.render(str(board[i][j]), 1, (0,0,0))
                screen.blit(text, (j*200 + 50, i*200 + 50 ))
    pygame.display.update()


redraw()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    

    if event.type == pygame.MOUSEBUTTONDOWN:
        # ---------
        checkIfGameOver()
        # ---------

        y,x = pygame.mouse.get_pos()
        x = int(x//(200))
        y = int(y//(200))
        if board[x][y] == '-':
            board[x][y] = 'X'
            redraw()

            # ---------
            checkIfGameOver()
            # ---------
    
            placex, placey = placeAiMove()
            board[placex][placey] = 'O'
            redraw()

# --------------------------------------------- #