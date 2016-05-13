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

    def get(x,y):
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