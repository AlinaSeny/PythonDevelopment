import cowsay
import sys


if sys.argv[2] in cowsay.list_cows():
	print(cowsay.cowsay(sys.argv[2], sys.argv[2]))
else:
	with open(sys.argv[1]) as f:
	cow = cowsay.read_dot_cow(f)
	pribt(cowsay.cowsay(sys.argv[2], sys.argv[1], cowfile=cow))
