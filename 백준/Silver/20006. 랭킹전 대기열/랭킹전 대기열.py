import sys

p,m = map(int, sys.stdin.readline().split(" "))
rooms = []
level, name = sys.stdin.readline().rstrip().split(" ")
level = int(level)
rooms.append([[level, name]])

for i in range(p - 1):
    level, name = sys.stdin.readline().rstrip().split(" ")
    level = int(level)
    check = False
    for room in rooms:
        if abs(level - room[0][0]) <= 10 and len(room) < m:
            room.append([level,name])
            check = True
            break
    if not check:
        rooms.append([[level, name]])

for room in rooms:
    room.sort(key=lambda x:x[1])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for i in room:
        print(i[0],i[1])

