import sys
import cowsay


start = [0,0]
cur = [0,0]
monst_coord = {}
xlen = 10
ylen = 10


def addmon(x, y, hello):
    repl = 0
    if (x, y) in monst_coord:
        repl = 1
    monst_coord[(x, y)] = hello
    print(f"Added monster to ({x}, {y}) saying {hello}")
    if repl:
        print("Replaced the old monster")


def encounter(x, y):
    print(cowsay.cowsay(monst_coord[(x,y)]))


def up():
    if cur[1] == 0:
        cur[1] = 9
    else:
        cur[1] -= 1
    print(f'Moved to {cur}')
    if (cur[0], cur[1]) in monst_coord:
        encounter(cur[0], cur[1])


def down():
    if cur[1] == 9:
        cur[1] = 0
    else:
        cur[1] += 1
    print(f'Moved to {cur}')
    if (cur[0], cur[1]) in monst_coord:
        encounter(cur[0], cur[1])


def left():
    if cur[0] == 0:
        cur[0] = 9
    else:
        cur[0] -= 1
    print(f'Moved to {cur}')
    if (cur[0], cur[1]) in monst_coord:
        encounter(cur[0], cur[1])


def right():
    if cur[0] == 9:
        cur[0] = 0
    else:
        cur[0] += 1
    print(f'Moved to {cur}')
    if (cur[0], cur[1]) in monst_coord:
        encounter(cur[0], cur[1])


def func(cmd):
    cmd = cmd.split()
    cmd = [i for i in cmd if i]
    if len(cmd) == 1:
        cmd = cmd[0]
        if cmd == 'up':
            up()
        elif cmd == 'down':
            down()
        elif cmd == 'left':
            left()
        elif cmd == 'right':
            right()
        else:
            print("Invalid command")
    elif len(cmd) == 4:
        if cmd[0] == 'addmon' and '0' <= cmd[1] <= '9' and '0' <= cmd[2] <= '9':
            addmon(int(cmd[1]), int(cmd[2]), cmd[3])
        else:
            print("Invalid arguments")
    else:
        print("Invalid command")



if len(sys.argv) != 1:
    f = open(sys.argv[2], 'r')
    lines = f.getlines()
    for line in lines:
        func(line)
else:
    while a := input():
        func(a)
