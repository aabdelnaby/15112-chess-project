import numpy
import math
#i am going to use piece square tables

class AI:
    def __init__(self):
        self.wpawnScore = numpy.array([
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
        [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
        [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ])

        self.bpawnScore = self.wpawnScore[::-1]

        self.wknightScore = numpy.array([
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
        [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
        [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
        [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
        [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
        [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
    ])
        self.bknightScore = self.wknightScore[::-1]

        self.wbishopScore = numpy.array([
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
])

        self.bbishopScore = self.wbishopScore[::-1]

        self.wbrookScore = numpy.array([
    [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
])
        self.bbrookScore = self.wbrookScore[::-1]

        self.wqueenScore = numpy.array([
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
])

        self.bqueenScore = self.wqueenScore[::-1]

        self.wkingScore = numpy.array([
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
])
        self.bkingScore = self.wkingScore[::-1]


    def value(self,gs):
        biggestboard = 0
        bcurrentboard = 0
        wcurrentboard = 0
        smallestcurrentboard = 0
        bestMove = 0
        legMov = gs.legalMove()
        for move in legMov:
            gs.makeMove(move)
            for i in range(len(gs.board)):
                for j in range(len(gs.board[i])):
                    if gs.board[i][j][1] == 'P':
                        bcurrentboard += 10 + self.bpawnScore[i][j]
                    if gs.board[i][j][1] == 'N':
                        bcurrentboard += 30 + self.bknightScore[i][j]
                    if gs.board[i][j][1] == 'R':
                        bcurrentboard +=  50 + self.bbrookScore[i][j]
                    if gs.board[i][j][1] == 'B':
                        bcurrentboard += 30 + self.bbishopScore[i][j]
                    if gs.board[i][j][1] == 'Q':
                        bcurrentboard += 90 + self.bqueenScore[i][j]
                    if gs.board[i][j][1] == 'K':
                        bcurrentboard += 900 + self.bkingScore[i][j]
            if bcurrentboard > biggestboard:
                biggestboard = bcurrentboard
                gs.undoMove()


        return biggestboard


    def minimax(self,gs,depth, alpha,beta, ismax ):
        value = self.value(gs)
        if gs.cMate or depth > 1:
            return value
        if ismax:
            possiblemoves = gs.legalMove()
            maxiVal = -math.inf
            for move in possiblemoves:
                gs.makeMove(move)
                eval = self.minimax(gs,depth +1 , alpha,beta,ismax= False)
                gs.undoMove()
                if eval > maxiVal:
                    maxiVal = eval
                    bestmove = move
                alpha = max(alpha,eval)
                if beta <= alpha:
                    break
            if depth == 0:
                return bestmove
            return maxiVal
        else:
            possiblemoves = gs.legalMove()
            minEval = math.inf
            for move in possiblemoves:
                gs.makeMove(move)
                eval  = self.minimax(gs,depth+1 , alpha,beta, ismax= True)
                gs.undoMove()
                minEval = min(eval,minEval)
                beta = min(eval,beta)
                if beta <= alpha:
                    break
            return minEval
