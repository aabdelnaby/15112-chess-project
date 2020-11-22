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
                if (turn == 'w' and self.whitemove) or (turn == 'b' and not self.whitemove):
                    piece = self.board[r][c][1] #get the type of peice
                    if piece == 'P':
                        self.PawnMoves(r, c, moves)
                    if piece == 'R':
                       self.RookMoves(r, c, moves)
                    if piece == 'N':
                        self.KnightMoves(r,c,moves)
                    if piece == 'B':
                        self.BishobMoves(r,c,moves)
                    if piece == 'Q':
                        self.QueenMoves(r,c,moves)
                    if piece == 'K':
                        self.KingMoves(r,c,moves)
        return moves

    #defining pawn legal moves
    def PawnMoves(self, r, c, moves):
        if self.whitemove:#white pawn moves
            if self.board[r-1][c] == '--': #if one space in front of the pawn is empty then it could move to it
                moves.append(Move((r,c),(r-1,c),self.board))
                if r == 6 and self.board[r-2][c] == '--': #if two spaces are empty then pawn could be moved to it
                    moves.append(Move((r,c),(r-2,c),self.board))
            if c-1 >= 0:#captures to the left
                if self.board[r-1][c-1][0] == 'b':
                    moves.append(Move((r,c),(r-1,c-1),self.board))
            if c+1 <= 7: #captures right peice
                moves.append(Move((r,c),(r-1,c+1),self.board))
        else:
            if self.board[r+1][c] == '--': #moves 1 or two front
                moves.append(Move((r,c),(r+1,c),self.board))
                if r == 1 and self.board[r+2][c] == '--':
                    moves.append(Move((r,c),(r+2,c),self.board))
            #captures
            if c-1 >= 0: #capture to the left
                if self.board[r+1][c-1][0] == 'w':
                    moves.append(Move((r,c),(r+1,c-1),self.board))
            if c+1 <= 7: #capture to the right
                if self.board[r+1][c+1][0] == 'w':
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))



    def RookMoves(self, r, c, moves):
        rooklist = ((-1,0),(0,1),(1,0),(0,1))
        enemyColor = 'b' if self.whitemove else 'w' #to check if white or black turn
        for d in rooklist:
            for i in range(1,8):
                endrow = r + d[0]*i
                endcol = c + d[1]*i
                if 0<= endrow < 8 and 0 <= endcol < 8:
                    endPiece = self.board[endrow][endcol]
                    if endPiece == '--':
                        moves.append(Move((r,c),(endrow,endcol),self.board))
                    elif endPiece[0] == enemyColor:
                        moves.append(Move((r,c),(endrow,endcol),self.board))
                        break
                    else:
                        break
                else:
                    break

    def KnightMoves(self,r,c,moves):
        knightlist = ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)) #the moves that a knight could do in the form delta(r,c)
        allycolor = 'w' if self.whitemove else 'b' #deciding which peice's turn
        for m in knightlist:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < 8 and 0 <= endcol < 8:
                endpeice = self.board[endrow][endcol]
                if endpeice[0] != allycolor:
                    moves.append(Move((r,c),(endrow,endcol),self.board))


    def BishobMoves(self, r, c, moves):
        bishoplist = ((1,1),(1,-1),(-1,1),(-1,-1)) #possible bishb moves in the form delta(r,c)
        if self.whitemove:
            eCol = 'b'
        else:
            eCol = 'w'
        for i in bishoplist:
            for j in range(1,8): #the range of the board
                endcol = c + i[1]*j
                endrow = r + i[0]*j
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == '--':
                        moves.append(Move((r,c),(endrow,endcol),self.board))
                    elif endpiece[0] == eCol:
                        moves.append(Move((r,c),(endrow,endcol),self.board))
                        break
                    else: #invalid move
                        break
                else: #not on board
                    break

    def QueenMoves(self, r, c, moves):
        self.BishobMoves(r, c, moves)
        self.RookMoves(r,c,moves)

    def KingMoves(self, r, c, moves):
        kinglist = ((1,1),(1,0),(0,1),(1,-1),(-1,1),(-1,0),(0,-1),(-1,-1))
        if not self.whitemove:
            eCol = 'b'
        else:
            eCol = 'w'
        for i in range(8):
            endrow = r + kinglist[i][0]
            endcol = c + kinglist[i][1]
            if 0 <= endrow < 8 and 0 <= endcol < 8: #make sure if peice on board
                endpeice = self.board[endrow][endcol]
                if endpeice[0] == eCol or endpeice == '--':
                    moves.append(Move((r,c),(endrow,endcol), self.board))





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
        self.MoveID = self.startRow*1000 + self.startColumn*100 + self.endRow*10 + self.endColumn

    def __eq__(self, other):
        if isinstance(other,Move):
            return self.MoveID == other.MoveID
        return False

    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startColumn) + self.getRankFile(self.endRow,self.endColumn)


    def getRankFile(self, row, column):
        return self.colstofiles[column] + self.rowstoRanks[row]

















