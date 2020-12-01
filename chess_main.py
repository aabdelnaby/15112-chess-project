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
#04:30 pm    05:15 pm    11/24/2020     started implementing an opening screen, not fully operative yet
#08:13 pm    08:45 pm    11/26/2020     started implementing checkmate and stalemate
#01:30 pm    05:00 pm    11/27/2020     discovered major bug
#12:00 pm    04:00 pm    11/28/2020     fixed major bug
#06:30 am    09:00 am    11/29/2020
#12:00 pm    02:30 pm    11/30/2020
#10:00 am    09:30 pm    12/01/2020     implemented a working AI

# citations
# https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/
# https://www.youtube.com/watch?v=xSy8k6GfuqY
# https://www.youtube.com/watch?v=mM_0FasqD8c

import pygame
import chessengine
import chessAI
import math


class chessgame:
    def __init__(self):
        self.width = 512
        self.hieght = 512
        self.dimension = 8
        self.maxfps = 5
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
        self.gs = chessengine.gameState()
        self.ai = chessAI.AI()
        validMoves = self.gs.legalMove()
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
                        move = chessengine.move(playerClicks[0], playerClicks[1], self.gs.board)
                        if move in validMoves:
                            self.gs.makeMove(move)
                            moveMade = True
                            sqaureSelected = () #reset the user click after clicking
                            playerClicks = []
                        else:
                            playerClicks = [sqaureSelected]


                #keyboard events
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        self.gs.undoMove()
                        moveMade = True



            if moveMade:
                self.gs.makeMove(self.ai.minimax(self.gs,0,-math.inf,math.inf,True))
                validMoves = self.gs.legalMove()

                moveMade = False


            clock.tick(self.maxfps)
            self.drawGameState(screen,self.gs)
            pygame.display.flip()

    '''
    responsible for graphics within a game state
    '''
    def drawGameState(self,screen, gs, draw = True):
        self.drawBoard(screen)
        self.drawPieces(screen, gs.board)
        if gs.cMate:
            if gs.whitemove:
                self.writeOnScreen(screen,'Black wins by Checkmate')
            else:
                self.writeOnScreen(screen, 'White wins by Checkmate')


    def drawBoard(self,screen):
        colors = [pygame.Color('white'),pygame.Color('gray')]
        #colors = [pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)),pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))] (chess party mode)
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

    def writeOnScreen(self,screen,text):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text1 = font.render(text, False , (255,0,0))
        textLoc = text1.get_rect()
        screen.blit(text1,textLoc)

cgame = chessgame()
cgame.main()
