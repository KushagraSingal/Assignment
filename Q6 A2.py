Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = int (input('Enter the value of a: '))
Enter the value of a: 2
b = int(input('Enter the value of b: '))
Enter the value of b: 6
num = a^b
Count_flipped_bit = 0
while (num != 0):
    num = num & (num - 1)
    Count_flipped_bit += 1

    
print("Number of bits needed to be flipped to convert a to b is:", Count_flipped_bit)
Number of bits needed to be flipped to convert a to b is: 1
