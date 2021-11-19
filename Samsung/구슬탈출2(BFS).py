# https://www.acmicpc.net/problem/13460


N= 5
M = 5

board = '####### #...RB# #.##### #.....# #####.# #O....# #######'

from sys import stdin
from collections import deque

input = stdin.readline()

n, m  = map(int, input.split())
a = [list(input.strip()) for _ in range(n)]

check
