from sys import argv

def ft_cat(fn):
	with open(argv[1], 'r') as fd:
		print(fd.read(), end = '')

ft_cat(argv[1])