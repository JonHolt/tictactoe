#-------------------------------------------------------------------------------
# Name:        board
# Purpose:      a game board for tic tac toe
#
# Author:      jholt
#
# Created:     13/05/2016
# Copyright:   (c) jholt 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Board:

    def __init__(self):
        self.board = ['.','.','.', '.','.','.', '.','.','.']

    def get(self,x,y):
        return self.board[(y*3)+x]

    def setX(self,x,y):
        idx = (y*3) + x
        if self.board[idx] == '.':
            self.board[idx] = 'X'
            return True
        else:
            return False

    def setO(self,x,y):
        idx = (y*3) + x
        if self.board[idx] == '.':
            self.board[idx] = 'O'
            return True
        else:
            return False

    def checkWin(self, player):
        #check rows
        for y in range(0,3):
            if self.get(0,y) == player and self.get(1,y) == player and self.get(2,y) == player:
                return True
        #check columns
        for x in range(0,3):
            if self.get(x,0) == player and self.get(x,1) == player and self.get(x,2) == player:
                return True
        #check diagonals
        if self.get(0,0) == player and self.get(1,1) == player and self.get(2,2) == player:
                return True
        if self.get(0,2) == player and self.get(1,1) == player and self.get(2,0) == player:
                return True
        #no win
        return False;