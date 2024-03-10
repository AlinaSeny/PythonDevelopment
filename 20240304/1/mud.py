import sys
import cowsay
import io


jgsbat = cowsay.read_dot_cow(io.StringIO('''
$the_cow = <<EOC;
         $thoughts
          $thoughts
    ,_                    _,
    ) '-._  ,_    _,  _.-' (
    )  _.-'.|\\--//|.'-._  (
     )'   .'\/o\/o\/'.   `(
      ) .' . \====/ . '. (
       )  / <<    >> \  (
        '-._/``  ``\_.-'
  jgs     __\\'--'//__
         (((""`  `"")))
EOC
'''))


start = [0, 0]
cur = [0, 0]
mon_coord = {}
custom_mon = {'jgsbat' : jgsbat}
xlen = 10
ylen = 10


def addmon(name, x, y, hello):
    if name not in cowsay.list_cows() and name not in custom_mon:
        print("Cannot add unknown monster")
        return
    repl = 0
    if (x, y) in mon_coord:
        repl = 1
    mon_coord[(x, y)] = [name, hello]
    print(f"Added monster {name} to ({x}, {y}) saying {hello}")
    if repl:
        print("Replaced the old monster")


def encounter(x, y):
    if mon_coord[(x,y)][0] in cowsay.list_cows():
        print(cowsay.cowsay(mon_coord[(x, y)][1], cow=mon_coord[(x, y)][0]))
    elif mon_coord[(x,y)][0] in custom_mon:
        print(cowsay.cowsay(mon_coord[(x, y)][1], cowfile=custom_mon[mon_coord[(x, y)][0]]))


def up():
    if cur[1] == 0:
        cur[1] = 9
    else:
        cur[1] -= 1
    print(f'Moved to {cur}')
    if (cur[0], cur[1]) in mon_coord:
        encounter(cur[0], cur[1])


def down():
    if cur[1] == 9:
        cur[1] = 0
    else:
        cur[1] += 1
    print(f'Moved to {cur}')
    if (cur[0], cur[1]) in mon_coord:
        encounter(cur[0], cur[1])


def left():
    if cur[0] == 0:
        cur[0] = 9
    else:
        cur[0] -= 1
    print(f'Moved to {cur}')
    if (cur[0], cur[1]) in mon_coord:
        encounter(cur[0], cur[1])


def right():
    if cur[0] == 9:
        cur[0] = 0
    else:
        cur[0] += 1
    print(f'Moved to {cur}')
    if (cur[0], cur[1]) in mon_coord:
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
    elif len(cmd) == 5:
        if cmd[0] == 'addmon' and '0' <= cmd[2] <= '9' and '0' <= cmd[3] <= '9':
            addmon(cmd[1], int(cmd[2]), int(cmd[3]), cmd[4])
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
