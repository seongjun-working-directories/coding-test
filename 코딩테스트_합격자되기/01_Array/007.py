'''
[문제 007] - https://school.programmers.co.kr/learn/courses/30/lessons/49994
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

U: 위쪽으로 한 칸 가기
D: 아래쪽으로 한 칸 가기
R: 오른쪽으로 한 칸 가기
L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다.
좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.

우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다.
예를 들어, "ULURRDLLU"로 명령했다면, 게임 캐릭터가 움직인 길이는 9이지만,
캐릭터가 처음 걸어본 길의 길이는 7이 됩니다. (8, 9번 명령어에서 움직인 길은 2, 3번 명령어에서 이미 거쳐 간 길입니다.)

단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.
예를 들어, "LULLLLLLU"로 명령했다면,
1번 명령어부터 6번 명령어대로 움직인 후, 7, 8번 명령어는 무시합니다. 다시 9번 명령어대로 움직입니다.

명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.

[제약조건]
- dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
- dirs의 길이는 500 이하의 자연수입니다.

[입출력 예]
dirs	        answer
"ULURRDLLU"	    7
"LULLLLLLU"	    7
'''
from copy import deepcopy

def solution(dirs):
    paths = []
    previous_xy = []
    current_xy = [0, 0]

    for i in dirs:
        tmp_xy = ""
        previous_xy = deepcopy(current_xy)
        
        if i == 'U':
            if (current_xy[1] < 5):
                current_xy[1] += 1
                tmp_xy += str(sorted([previous_xy[0], current_xy[0]]))
                tmp_xy += str(sorted([previous_xy[1], current_xy[1]]))
                paths.append(tmp_xy)
        elif i == 'D':
            if (current_xy[1] > -5):
                current_xy[1] -= 1
                tmp_xy += str(sorted([previous_xy[0], current_xy[0]]))
                tmp_xy += str(sorted([previous_xy[1], current_xy[1]]))
                paths.append(tmp_xy)
        elif i == 'L':
            if (current_xy[0] > -5):
                current_xy[0] -= 1
                tmp_xy += str(sorted([previous_xy[0], current_xy[0]]))
                tmp_xy += str(sorted([previous_xy[1], current_xy[1]]))
                paths.append(tmp_xy)
        elif i == 'R':
            if (current_xy[0] < 5):
                current_xy[0] += 1
                tmp_xy += str(sorted([previous_xy[0], current_xy[0]]))
                tmp_xy += str(sorted([previous_xy[1], current_xy[1]]))
                paths.append(tmp_xy)
    
    paths = set(paths)
    return len(paths)

def is_valid_move(nx, ny):
    return 0 <= nx < 11 and 0 <= ny < 11

def update_location(x, y, dir):
    if dir == 'U':
        nx, ny = x, y+1
    elif dir == 'D':
        nx, ny = x, y-1
    elif dir == 'L':
        nx, ny = x-1, y
    elif dir == 'R':
        nx, ny = x+1, y
    return nx, ny

def solution(dirs):
    x, y = 5, 5
    answer = set()

    for dir in dirs:
        nx, ny = update_location(x, y, dir)
        if not is_valid_move(nx, ny):
            continue
        
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        x, y = nx, ny
    
    return len(answer)/2
