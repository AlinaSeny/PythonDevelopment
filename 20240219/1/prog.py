import sys
import os
import zlib


if len(sys.argv) == 1:
	print("Expected 1 or 2 arguments")
	sys.exit(1)
else:
	path = sys.argv[1]
	if len(sys.argv) == 2:
		branches = os.listdir(path + '/.git/refs/heads')
		for branch in branches:
			print(branch)
	elif len(sys.argv) == 3:
		branch = sys.argv[2]
		if branch not in os.listdir(path + '/.git/refs/heads'):
			print(f"Branch {branch} doesn't exist")
			sys.exit(1)
		else:
			f = open(path + '/.git/refs/heads/' + branch, 'r')
			last_com = f.readline().strip()
			f.close()
			f = open(path + '/.git/objects/' + last_com[:2] + '/' + last_com[2:], 'rb')
			header, _, body = zlib.decompress(f.read()).partition(b'\00')
			print(body.decode())
			f.close()
