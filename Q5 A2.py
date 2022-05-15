Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = int(input('Enter First Side(in integers): '))
Enter First Side(in integers): 2
y = int(input('Enter Second Side(in integers): '))
Enter Second Side(in integers): 5
z = int(input('Enter Third Side(in integers): '))
Enter Third Side(in integers): 8
Condition = (x+y>z) and (y+z>x) and (x+z>y)
Condition and print('Yes (Triangle possible)')
False
Condition or print('No (Triangle not possible)')
No (Triangle not possible)
