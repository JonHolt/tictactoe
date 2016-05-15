#-------------------------------------------------------------------------------
# Name:        ai
# Purpose:      to find the next move a given player should make
#
# Author:      Jonathan
#
# Created:     15/05/2016
# Copyright:   (c) Jonathan 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from board import Board

def try_move(state, move, player):
    result = state.copy()
    if player == 'X':
        can_do = result.setX(*move)
    elif player == 'O':
        can_do = result.setO(*move)
    return can_do, result


def next_turn(state, player):
    #vars to store best found so far
    best_score = -5
    best_move = (-1,-1)
    if player == 'X':
        opponent = 'O'
    elif player == 'O':
        opponent = 'X'

    #try every move, store any that are better than the best
    for y in range(0,3):
        for x in range(0,3):
            can_move, result = try_move(state, (x,y), player)
            if can_move:
                if result.checkWin(player):
                    return (x,y)
                score = min(result,opponent)
                if score > best_score:
                    best_score = score
                    best_move = (x,y)

    return best_move


def min(state, opponent):
    #setup
    best_score = 5
    if opponent == 'X':
        player = 'O'
    elif opponent == 'O':
        player = 'X'

    #check if terminating state
    if state.checkWin(opponent):
        return -1
    if state.checkWin(player):
        return 1
    if state.checkDraw():
        return 0

    #try every move, return the one with the lowest score
    for y in range(0,3):
        for x in range(0,3):
            can_move, result = try_move(state, (x,y), opponent)
            if can_move:
                score = max(result,player)
                if score < best_score:
                    best_score = score

    return best_score


def max(state, player):
    #setup
    best_score = -5
    if player == 'X':
        opponent = 'O'
    elif player == 'O':
        opponent = 'X'

    #check if terminating state
    if state.checkWin(opponent):
        return -1
    if state.checkWin(player):
        return 1
    if state.checkDraw():
        return 0

    #try every move, return the one with the lowest score
    for y in range(0,3):
        for x in range(0,3):
            can_move, result = try_move(state, (x,y), player)
            if can_move:
                score = min(result, opponent)
                if score > best_score:
                    best_score = score

    return best_score