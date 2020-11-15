'''
this file contains the driver code and the GUI
'''
#star    end      date
#8:30    11:00    11/15/2020


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
    loadImages()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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















