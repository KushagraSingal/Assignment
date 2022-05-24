Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = int(input('Enter first no.: '))
Enter first no.: 34
b = int(input('Enter second no.: '))
Enter second no.: 12
print('No. of bits to be flipped =', bin(a^b).count('1'))
No. of bits to be flipped = 4
