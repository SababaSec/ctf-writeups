#!/usr/bin/env python3
maze = []


def getNumber(start, direction):
    number = ''
    while getChar(start).isdigit():
        number += getChar(start)
        start = (start[0] + direction[0], start[1] + direction[1])
    return int(number)


def getChar(pos):
    return maze[pos[0]][pos[1]]


def solvePath(start):
    pos = (start[0] + 1, start[1])
    stack = []
    flag = ''

    char = getChar(pos)
    while char != '#':
        if char == '@':
            return flag
        elif char == '(':
            flag = stack.pop() + flag
            jump = getNumber((pos[0], pos[1] + 1), (0, 1))
            pos = (pos[0], pos[1] - jump)
        elif char == ')':
            flag += stack.pop()
            jump = getNumber((pos[0], pos[1] - 1), (0, -1))
            pos = (pos[0], pos[1] + jump)
        elif char == '-':
            flag = flag[1:]
            jump = getNumber((pos[0] + 1, pos[1]), (1, 0))
            pos = (pos[0] - jump, pos[1])
        elif char == '+':
            flag = flag[:-1]
            jump = getNumber((pos[0] - 1, pos[1]), (-1, 0))
            pos = (pos[0] + jump, pos[1])
        elif char == '%':
            flag = flag[::-1]
            pos = (pos[0] + 1, pos[1])
        elif char == '[':
            stack.append(getChar((pos[0], pos[1] + 1)))
            pos = (pos[0], pos[1] + 2)
        elif char == ']':
            stack.append(getChar((pos[0], pos[1] - 1)))
            pos = (pos[0], pos[1] - 2)
        elif char == '*':
            stack.append(getChar((pos[0] - 1, pos[1])))
            pos = (pos[0] - 2, pos[1])
        elif char == '.':
            stack.append(getChar((pos[0] + 1, pos[1])))
            pos = (pos[0] + 2, pos[1])
        elif char == '<':
            jump = getNumber((pos[0], pos[1] + 1), (0, 1))
            pos = (pos[0], pos[1] - jump)
        elif char == '>':
            jump = getNumber((pos[0], pos[1] - 1), (0, -1))
            pos = (pos[0], pos[1] + jump)
        elif char == '^':
            jump = getNumber((pos[0] + 1, pos[1]), (1, 0))
            pos = (pos[0] - jump, pos[1])
        elif char == 'v':
            jump = getNumber((pos[0] - 1, pos[1]), (-1, 0))
            pos = (pos[0] + jump, pos[1])
        char = getChar(pos)

    return ''


with open('maze.txt', 'r') as f:
    lines = f.readlines()
    starts = []

    # Find starting position:
    i = 0
    for line in lines:
        maze.append(line)
        j = 0
        for char in line:
            if char == '$':
                starts.append((i, j))
            j += 1
        i += 1

    for start in starts:
        flag = solvePath(start)
        if '{FLG:' in flag:
            print(flag)
