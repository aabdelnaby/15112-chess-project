'''
this file contains the driver code and the GUI
'''
#start         end          date                                comment
#08:30 pm    11:00 pm    11/15/2020
#11:30 am    02:00 pm    11/16/2020     chess layout is done but moves are not working properly
#09:00 pm    10:15 pm    11/16/2020     fixed chess moves, peices could move but still no legal moves set
#09:30 am    10:40 am    11/17/2020     implemented an undo move function and put the basis for legal moves function
#06:00 pm    09:40 pm    11/17/2020     created legal moves for pawn and rook and knight
import pygame
import chessengine
width = 512
hieght = 512
dimension = 8
maxfps = 15
squareSize = hieght//dimension
images = {}

'''
initializing a global dictionary of images
'''

def loadImages():
    pieces = ['bQ','bK','bB','bN','bR','bP','wQ','wK','wB','wN','wR','wP']
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load('images/'+piece+ '.png'),(squareSize,squareSize))

def main():
    pygame.init()
    screen = pygame.display.set_mode((width,hieght))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('white'))
    gs = chessengine.gameState()
    validMoves = gs.getValidMoves()
    moveMade = False
    loadImages()
    running = True
    sqaureSelected = () #stores number of selected square
    playerClicks = [] #stores a players clicl
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #mouse events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() #gets x,y location of mouse
                mCol = location[0]//squareSize
                mRow = location[1]//squareSize
                if sqaureSelected == (mRow, mCol): #if the same square is clicked twice the move is cancelled
                    sqaureSelected = () #unselect
                    playerClicks = []
                else:
                    sqaureSelected = (mRow , mCol)
                    playerClicks.append(sqaureSelected)
                if len(playerClicks) == 2:
                    move = chessengine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqaureSelected = () #reset the user click after clicking
                    playerClicks = []
            #keyboard events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    gs.undoMove()
                    moveMade = True

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False




        clock.tick(maxfps)
        drawGameState(screen,gs)
        pygame.display.flip()

'''
responsible for graphics within a game state
'''
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors = [pygame.Color('white'),pygame.Color('gray')]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r+c)%2)]
            pygame.draw.rect(screen,color,pygame.Rect(c*squareSize, r*squareSize, squareSize, squareSize))



def drawPieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != '--':
                screen.blit(images[piece],pygame.Rect(c*squareSize,r*squareSize,squareSize,squareSize))

if __name__ == '__main__':
    main()


#66 lines of code












