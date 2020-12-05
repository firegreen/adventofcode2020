import sys
from toboggan_trajectory_input import input

map = []
for i, line in enumerate(input.split("\n")):
    map.append([1 if char == '#' else 0 for char in line])


rows = len(map)
columns = len(map[0])
for i in range(rows):
    print(''.join(('#' if map[i][j] else ' ' for j in range(columns))))

x, y = 0, 0
result = 1
for inc_x, inc_y in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    sub_result=0
    x=0
    for y in range(inc_y, rows, inc_y):
        x += inc_x
        if map[y][x%columns]:
            sub_result += 1
    print(sub_result)
    result = result*sub_result

print(result)