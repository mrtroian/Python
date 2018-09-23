from sys import argv

def true_bin(in_nb):
	'''
Return the binary representation of an integer.
Unlike standard bin function, true_bin handles negative numbers.
'''
	neg = False
	str = ['0', 'b']
	nb = int(in_nb)
	n = 0x80

	if nb < 0:
		nb = -nb
		neg = True
	elif nb is 0:
		return '0b0'

	while nb > n:
		n <<= 1
	nb = (~nb + 1) if neg else nb

	while True:
		if (nb & n) | (nb == n):
			break
		n >>= 1

	while n is not 0:
		str.append('1' if (n & nb) else '0')
		n >>= 1

	return (''.join(str))

print(true_bin(argv[1]))