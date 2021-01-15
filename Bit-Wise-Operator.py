'''
Three examples of the bit-wise operator
'''
# Question 1
# How do you swap two integers, i and j, without using additional storage spaces?
# basic solution: this will using additional storage spaces
def swap_basic(i,j):
    temp = j
    j = i
    i = temp
    return i, j

# advanced solution: this will NOT using additional storage spaces
def swap_advanced(i,j):
    i = i + j
    j = i - j
    i = i - j
    return i, j

# using the bit-wise operator XOR ^
# for every digit, if they're the same, returns 0, otherwise 1
def swap_bit_wise(i,j):
    i = i ^ j
    j = j ^ i
    i = i ^ j
    return i, j
'''
for example
if  i = 1000100111 = 551
and j = 1010010011 = 659
now
i ^ j = 0010110100 = i
j ^ i = 1000100111 = j
i ^ j = 1010010011 = i
The swap is completed
'''

# test
i = 69
j = 96
print(swap_basic(i,j)) # (96, 69)
print(swap_advanced(i,j)) # (96, 69)
print(swap_bit_wise(i,j)) # (96, 69)


# Question 2
# How do you know if a number is the power of 2?
'''
any number that is the power of 2, in binary, it must be:
100000....00000 = 2**n
At the same time, (2^n - 1), it must be:
011111....11111 = 2**n -1

THEY DON'T SHARE ANY BIT!

Therefore, we use the & (the bit-wise and operator)
'''

def power_of_2(number):
    if number & (number-1) == 0:
        return True
    return False

# test
print(power_of_2(8)) # True
print(power_of_2(9)) # False
print(power_of_2(256)) # True
print(power_of_2(999)) # False

# Question 3
# How do you compute x*7 without using the multiplication * operator?
'''
Using the shift operator
for any given number, if we write it in the binary form and shift it to the left
for x digits, it will be 2**x times larger than before
for example
x      = 10010111    = 151
x << 3 = 10010111000 = 1208

to multiply any number by 7, just left shift it for 3 digits and deduct itself
'''
def multiply_by_7(number):
    return (number<<3)-number

# test
print(multiply_by_7(1)) # 7
print(multiply_by_7(5)) # 35
print(multiply_by_7(20)) # 140