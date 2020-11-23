'''
this file contains the driver code and the GUI
'''
#Abdelrahman Abdelnaby
#aaabdeln

#start         end          date                                comment
#08:30 pm    11:00 pm    11/15/2020
#11:30 am    02:00 pm    11/16/2020     chess layout is done but moves are not working properly
#09:00 pm    10:15 pm    11/16/2020     fixed chess moves, peices could move but still no legal moves set
#09:30 am    10:40 am    11/17/2020     implemented an undo move function and put the basis for legal moves function
#06:00 pm    09:40 pm    11/17/2020     created legal moves for pawn and rook and knight
#05:00 pm    10:25 pm    11/22/2020     finished legal moves for all peices
#06:30 pm    08:52 pm    11/23/2020     fixed some errors in the engine, tried to make an opening screen, doesnt work yet
import pygame
import chessengine


class chessgame:
    def __init__(self):
        self.width = 512
        self.hieght = 512
        self.dimension = 8
        self.maxfps = 15
        self.squareSize = self.hieght // self.dimension
        self.images = {}


    def loadImages(self):
        pieces = ['bQ','bK','bB','bN','bR','bP','wQ','wK','wB','wN','wR','wP']
        for piece in pieces:
            self.images[piece] = pygame.transform.scale(pygame.image.load('images/'+piece+ '.png'),(self.squareSize,self.squareSize))

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width,self.hieght))
        clock = pygame.time.Clock()
        screen.fill(pygame.Color('white'))
        gs = chessengine.gameState()
        validMoves = gs.getValidMoves()
        moveMade = False
        self.loadImages()
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
                    mCol = location[0]//self.squareSize
                    mRow = location[1]//self.squareSize
                    if sqaureSelected == (mRow, mCol): #if the same square is clicked twice the move is cancelled
                        sqaureSelected = () #unselect
                        playerClicks = []
                    else:
                        sqaureSelected = (mRow , mCol)
                        playerClicks.append(sqaureSelected)
                    if len(playerClicks) == 2:
                        move = chessengine.Move(playerClicks[0], playerClicks[1], gs.board)
                        #print(move.getChessNotation())
                        if move in validMoves:
                            gs.makeMove(move)
                            moveMade = True
                            sqaureSelected = () #reset the user click after clicking
                            playerClicks = []
                        else:
                            playerClicks = [sqaureSelected]
                #keyboard events
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        gs.undoMove()
                        moveMade = True
            if moveMade:
                validMoves = gs.getValidMoves()
                moveMade = False
            clock.tick(self.maxfps)
            self.drawGameState(screen,gs)
            pygame.display.flip()

    '''
    responsible for graphics within a game state
    '''
    def drawGameState(self,screen, gs):
        self.drawBoard(screen)
        self.drawPieces(screen, gs.board)

    def drawBoard(self,screen):
        colors = [pygame.Color('white'),pygame.Color('gray')]
        for r in range(self.dimension):
            for c in range(self.dimension):
                color = colors[((r+c)%2)]
                pygame.draw.rect(screen,color,pygame.Rect(c*self.squareSize, r*self.squareSize, self.squareSize, self.squareSize))



    def drawPieces(self,screen, board):
        for r in range(self.dimension):
            for c in range(self.dimension):
                piece = board[r][c]
                if piece != '--':
                    screen.blit(self.images[piece],pygame.Rect(c*self.squareSize,r*self.squareSize,self.squareSize,self.squareSize))



class openingScreen():

    def __init__(self):
        self.width = 512
        self.height = 512

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode((cgame.width, cgame.hieght))
        screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()


                # if the mouse is clicked on the
                # button the game is terminated
                    if cgame.width / 2 <= mouse[0] <= self.width / 2 + 140 and self.height / 2 <= mouse[1] <= self.height / 2 + 40:
                        cgame.main()

                    # fills the screen with a color


            # stores the (x,y) coordinates into
            # the variable as a tuple


            # if mouse is hovered on a button it
            # changes to lighter shade
                    if cgame.width / 2 <= mouse[0] <= cgame.width / 2 + 140 and self.height / 2 <= mouse[1] <= self.height / 2 + 40:
                        pygame.draw.rect(screen, (0,0,255), [self.width / 2, self.height / 2, 140, 40])

                    else:
                        pygame.draw.rect(screen, (0,0,0), [self.width / 2, self.height / 2, 140, 40])

                        # superimposing the text onto our button
                    screen.blit('play 1v1', (self.width / 2 + 50, self.height / 2))

            # updates the frames of the game
            pygame.display.update()




cgame = chessgame()
opensc = openingScreen()
#cgame.main()

opensc.main()












