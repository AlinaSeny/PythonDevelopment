import cmd

class Echoer(cmd.Cmd):
	'''Dumb echo command REPL'''
	propmpt = ':->'

	def do_echo(self, args):
		print(args)

	def do_EOF(self, args):
		return True


if __name__ == '__main__':
	Echoer().cmdloop()

