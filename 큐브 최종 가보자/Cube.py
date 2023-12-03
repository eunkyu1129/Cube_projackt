import sys
from Cube_function import *
input = sys.stdin.readline
print('큐브가 3x3x3인가요? 아니면 2x2x2인가요 (3x3s3이면 3, 2x2x2이면 2라고 입력하시오)')
Cube_type = int(input())

#큐브 입력받기
Cube_input(Cube_type)

Cube_list = Cube_input(Cube_type)

print(Cube_list)
