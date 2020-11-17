'''
this file is the chess engine, it contains the information of the current game state and will be responsible for
determining the legal moves
'''

class gameState():
    def __init__(self):
        #this is the chess board, it is a list of lists
        self.board = [
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bP','bP','bP','bP','bP','bP','bP','bP'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['wP','wP','wP','wP','wP','wP','wP','wP'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR']]

        self.whitemove = True
        self.moveLog = [] #creating a list of tuples to log the moves and store them

    def makeMove(self, move):
        self.board[move.startRow][move.startColumn] = '--'
        self.board[move.endRow][move.endColumn] = move.peiceMoved
        self.moveLog.append(move)
        self.whitemove = not self.whitemove #swaps players turns

    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop() #gets last move made
            self.board[move.startRow][move.startColumn] = move.peiceMoved
            self.board[move.endRow][move.endColumn] = move.peiceCaptured
            self.whitemove = not self.whitemove #switching turns

    def getValidMoves(self):
        return self.getAllPossibleMoves()

    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0] #gives the turn (white,black or non)
                if (turn == 'w' and self.whitemove) and (turn == 'b' and not self.whitemove):
                    piece = self.board[r][c][1] #get the type of peice
                    if piece == 'P':
                        #place holder for pawn legal moves function
                        pass
                    if piece == 'R':
                        #place holder for rook legal moves function
                        pass





#creating the chess notation
class Move():
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

    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startColumn) + self.getRankFile(self.endRow,self.endColumn)


    def getRankFile(self, row, column):
        return self.colstofiles[column] + self.rowstoRanks[row]



















