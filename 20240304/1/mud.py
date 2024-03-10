import sys
import cowsay
import shlex
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
    cmd = shlex.split(cmd)
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
    elif len(cmd) == 9 and cmd[0] == 'addmon':
        name = cmd[1]
        hello = False
        hp = False
        x = False
        y = False
        par = cmd[2:]
        for i in len(par):
            if par[i] == 'hello':
                i += 1
                hello = par[i]
            elif par[i] == 'hp':
                i += 1
                if par[i].isdigit() and int(par[i]) > 0:
                    hp = par[i]
                else:
                    break
            elif par[i] == 'coords':
                if (par[i + 1].isdigit() and int(par[i + 1]) >= 0 and int(par[i + 1]) <= 9
                        and par[i + 2].isdigit() and int(par[i + 2]) >= 0 and int(par[i + 2]) <= 9):
                    hp = par[i]
                    x = par[i + 1]
                    y = par[i + 2]
                    i += 2
                else:
                    break
            else:
                break
        if not (hello and hp and x and y):
            print("Invalid arguments")
    else:
        print("Invalid command")


print("<<< Welcome to Python-MUD 0.1 >>>")
if len(sys.argv) != 1:
    f = open(sys.argv[2], 'r')
    lines = f.getlines()
    for line in lines:
        func(line)
else:
    while a := input():
        func(a)
