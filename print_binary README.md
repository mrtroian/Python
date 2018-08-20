# Python

print_binary program prints the binary representation of an integer.

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
There can be no '-' symbol in the binary system and the question here is - "How are negative numbers stored in binary?".
The right answer is by using two's complement technique.
To get the binary of the negative integer, you should firstly reverse all the bits and then increment it by 1.

The code for this operation:
```
~nb + 1
```
Let's initialise nb with 42, apply two's complement and try to get binary:
```
nb = 42
nb = (~nb + 1)
print(bin(nb))
# output:
# -0b101010
```
At least, we are right about two's complement.
But how to get the real binary of an integer?

This what true_bin function for:
```
0b11111000 # for -8 as input
0b11110110 # for -10 as input
0b11010110 # for -42 as input
0b10110010 # for -78 as input
```
