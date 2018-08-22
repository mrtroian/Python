from sys import argv

def ft_cat(fn):
	'''
Reproduction of the cat function, without extra options.
'''
	with open(fn, 'r') as fd:
		print(fd.read(), end = '')

if len(argv) != 1:
	argv.pop(0)
	for file in argv:
		ft_cat(file)
