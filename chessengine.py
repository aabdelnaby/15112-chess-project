'''
this file is the chess engine, it contains the information of the current game state and will be responsible for
determining the legal moves
'''

import numpy as np
import chessAI
import random

class gameState():
    def __init__(self):
        #this is the chess board, it is a list of lists
        self.board = np.array([
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bP','bP','bP','bP','bP','bP','bP','bP'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['wP','wP','wP','wP','wP','wP','wP','wP'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR']])


        self.whitemove = True
        self.moveLog = [] #creating a list of tuples to log the moves and store them
        self.cMate = False
        self.sMate = False


    def whiteKingLocation(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 'wK':
                    return (r, c)

    def blackKingLocation(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 'bK':
                    return (r, c)



    def makeMove(self, move):
        #print(self.board[0])

        self.board[move.startRow][move.startColumn] = '--'
        self.board[move.endRow][move.endColumn] = move.peiceMoved
        self.moveLog.append(move)
        self.swapTurns() #swaps players turns
        self.ischeckmate()

    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop() #gets last move made
            self.board[move.startRow][move.startColumn] = move.peiceMoved
            self.board[move.endRow][move.endColumn] = move.peiceCaptured
            self.swapTurns() #switching turns

    def ischeckmate(self):
        if len(self.legalMoves) == 0:
            self.cMate = True
            self.sMate = True
            return True
        return False


    def legalMove(self):
        self.legalMoves = self.possibleMoves()
        #self.swapTurns()
        for i in range(len(self.legalMoves)-1,-1,-1):
            self.makeMove(self.legalMoves[i])
            self.swapTurns()
            if self.checkmate():
                self.legalMoves.remove(self.legalMoves[i])
            self.swapTurns()
            self.undoMove()
        return self.legalMoves


    def swapTurns(self):
        self.whitemove = not self.whitemove


    def attackable(self, row, column):
        self.swapTurns()
        OpMove = self.possibleMoves()
        self.swapTurns()
        #print('attackable reached')
        for move in OpMove:
            if move.endRow == row and move.endColumn == column:
                    return True
        return False

    def checkmate(self):
        if self.whitemove:
            return self.attackable(self.whiteKingLocation()[0], self.whiteKingLocation()[1])
        else:
            return self.attackable(self.blackKingLocation()[0], self.blackKingLocation()[1])



    def possibleMoves(self):
        self.moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0] #gives the turn (white,black or non)
                if (turn == 'w' and self.whitemove) or (turn == 'b' and not self.whitemove):
                    self.piece = self.board[r][c][1] #get the type of peice
                    if self.piece == 'P':
                        self.pawnMoves(r, c)
                    if self.piece == 'R':
                       self.rookMoves(r, c)
                    if self.piece == 'N':
                        self.knightMoves(r,c)
                    if self.piece == 'B':
                        self.bishobMoves(r,c)
                    if self.piece == 'Q':
                        self.queenMoves(r,c)
                    if self.piece == 'K':
                        self.kingMoves(r,c)
        return self.moves

    #defining pawn legal moves
    def pawnMoves(self, r, c):
        #if r <= 6 and c <= 6:
            if self.whitemove:#white pawn moves
                if self.board[r-1][c] == '--': #if one space in front of the pawn is empty then it could move to it
                    self.moves.append(move((r,c),(r-1,c),self.board))
                    if r == 6 and self.board[r-2][c] == '--': #if two spaces are empty then pawn could be moved to it
                        self.moves.append(move((r,c),(r-2,c),self.board))
                if c-1 >= 0:#captures to the left
                    if self.board[r-1][c-1][0] == 'b':
                        self.moves.append(move((r,c),(r-1,c-1),self.board))
                if c+1 <= 7: #captures right peice
                    if self.board[r - 1][c + 1][0] == 'b':
                     self.moves.append(move((r,c),(r-1,c+1),self.board))
            else:
                if self.board[r+1][c] == '--': #moves 1 or two front
                    self.moves.append(move((r,c),(r+1,c),self.board))
                    if r == 1 and self.board[r+2][c] == '--':
                        self.moves.append(move((r,c),(r+2,c),self.board))
                #captures
                if c-1 >= 0: #capture to the left
                    if self.board[r+1][c-1][0] == 'w':
                        self.moves.append(move((r,c),(r+1,c-1),self.board))
                if c+1 <= 7: #capture to the right
                    if self.board[r+1][c+1][0] == 'w':
                        self.moves.append(move((r, c), (r + 1, c + 1), self.board))



    def rookMoves(self, r, c):
        deltaxy = ((-1,0),(0,1),(1,0),(0,1))
        if self.whitemove:
            eCol = 'b'
        else:
            eCol = 'w' #to check if white or black turn
        for d in deltaxy:
            for i in range(1,8):
                endrow = r + d[0]*i
                endcol = c + d[1]*i
                if 0<= endrow <= 7 and 0 <= endcol <= 7:
                    endPiece = self.board[endrow][endcol]
                    if endPiece == '--':
                        self.moves.append(move((r,c),(endrow,endcol),self.board))
                    elif endPiece[0] == eCol:
                        self.moves.append(move((r,c),(endrow,endcol),self.board))
                        break
                    else:
                        break
                else:
                    break

    #allycolor = 'w' if self.whitemove else 'b'
    def knightMoves(self,r,c):
        deltaxy = ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)) #the moves that a knight could do in the form delta(r,c)
        if self.whitemove:
            allycolor = 'w'
        else:
            allycolor = 'b'
        for i in deltaxy:
            endrow = r + i[0]
            endcol = c + i[1]
            if 0 <= endrow < 8 and 0 <= endcol < 8:
                endpeice = self.board[endrow][endcol]
                if endpeice[0] != allycolor:
                    self.moves.append(move((r,c),(endrow,endcol),self.board))


    def bishobMoves(self, r, c):
        deltaxy = ((1,1),(1,-1),(-1,1),(-1,-1)) #possible bishb moves in the form delta(r,c)
        if self.whitemove:
            eCol = 'b'
        else:
            eCol = 'w'
        for i in deltaxy:
            for j in range(1,8): #the range of the board
                endcol = c + i[1]*j
                endrow = r + i[0]*j
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == '--':
                        self.moves.append(move((r,c),(endrow,endcol),self.board))
                    elif endpiece[0] == eCol:
                        self.moves.append(move((r,c),(endrow,endcol),self.board))
                        break
                    else: #invalid move
                        break
                else: #not on board
                    break

    def queenMoves(self, r, c):
        self.bishobMoves(r, c)
        self.rookMoves(r,c)

    def kingMoves(self, r, c):
        deltaxy = ((1,1),(1,0),(0,1),(1,-1),(-1,1),(-1,0),(0,-1),(-1,-1))
        if self.whitemove:
            eCol = 'b'
        else:
            eCol = 'w'
        for i in deltaxy:
            endrow = r + i[0]
            endcol = c + i[1]
            if 0 <= endrow < 8 and 0 <= endcol < 8: #make sure if peice on board
                endpeice = self.board[endrow][endcol]
                if endpeice[0] == eCol or endpeice == '--':
                    self.moves.append(move((r,c),(endrow,endcol), self.board))



    def countPeices(self):
        self.blackPeicesNum = 0
        self.numbR = 0
        self.numbN = 0
        self.numbB = 0
        self.numbQ = 0
        self.numbK = 0
        self.numbP = 0
        self.whitePeicesNum = 0
        self.numwR = 0
        self.numwN = 0
        self.numB = 0
        self.numbQ = 0
        self.numbK = 0
        self.numbP = 0
        for i in self.board:
            for j in self.board[i]:
                if j[0] == 'b':
                    self.blackPeicesNum += 1
                if j[0] == 'w':
                    self.whitePeicesNum += 1

################################################################

#creating the chess notation
class move():
    rankstoRows = {'1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}
    rowstoRanks = {v:k for k,v in rankstoRows.items()}
    filestocols = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    colstofiles = {v:k for k, v in filestocols.items()}


    def __init__(self,startSquare, endSquare, board):
        self.startRow = startSquare[0]
        self.startColumn = startSquare[1]
        self.endRow = endSquare[0]
        self.endColumn = endSquare[1]
        self.peiceMoved = board[self.startRow][self.startColumn]
        self.peiceCaptured = board[self.endRow][self.endColumn]
        self.Move = self.startRow*1000 + self.startColumn*100 + self.endRow*10 + self.endColumn

    def __eq__(self, other):
        if isinstance(other,move):
            return self.Move == other.Move
        return False

    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startColumn) + self.getRankFile(self.endRow,self.endColumn)

    def getRankFile(self, row, column):
        return self.colstofiles[column] + self.rowstoRanks[row]