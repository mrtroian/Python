# Python

print_binary program prints the binary representation of an integer.

The idea of this program is to correctly print a binary represantation of an integer as it is stored in memory.

Example of standard bin function output:
```
0b1000 # for 8 as input
0b1010 # for 10 as input
0b101010 # for 42 as input
0b1001110 # for 78 as input
```
If a negative integer passed:
```
-0b1000 # for -8 as input
-0b1010 # for -10 as input
-0b101010 # for -42 as input
-0b1001110 # for -78 as input
```
This behaviour is incorrect, because there can be no hyphene in the binary code.
To get the binary of a negative integer, you should firstly reverse all the bits in the positive integer and then increment it by 1. This method is called two's complement.
https://en.wikipedia.org/wiki/Two's_complement

The code for this operation:
```
~nb + 1
```
Let's initialise nb with 42, apply two's complement and try again:
```
nb = 42
nb = (~nb + 1)
print(bin(nb))
# output:
# -0b101010
```
As we see, nb is treated just as negative number.

Example of true_bin:
```
0b11111000 # for -8 as input
0b11110110 # for -10 as input
0b11010110 # for -42 as input
0b10110010 # for -78 as input
```
