import sys
import os


if len(sys.argv) == 1:
	print("Expected 1 or 2 arguments")
	sys.exit(1)
else:
	path = sys.argv[1]
	if len(sys.argv) == 2:
		branches = os.listdir(path + '/.git/refs/heads')
		for branch in branches:
			print(branch)
