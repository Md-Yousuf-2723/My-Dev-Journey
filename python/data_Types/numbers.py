num1 = 23 # int
num2 = 23.33 # float 
num3 = 42.567

sum = num1 + num2 + num3 # also print(num1 + num2 + num3) is valid
sub = num3 - num1 # also print(num3 - num1) is valid\
mult = num1 * num2 * num3
div = num3 / num1
reminder = 5 % 2 # % --> mode operator
# python can handle x = 4.23 + 5 but it's not a good practise and in code review in compaines or industries it will be rejected. So, x = (int)4.23 + 5 is a good pactice
complex_num1 = 5 + 7j
complex_num2 = 6 - 9j
sum_of_complex_num = complex_num1 + complex_num2
sub_of_complex_num = complex_num1 - complex_num2
mult_of_complex_num = complex_num1 * complex_num2
div_of_complex_num = complex_num1 / complex_num2
# Complex number important concept : 
# com_num = 5 + 3/2j this will output 5 - 1.5j cause it is treated as 5 + 3/(2j)
# So to make it write, it can be written as
# 5 + (3/2)*1j --> 1 is necessary or it will show a error
# or, 5 + 3j/2

div_with_pricision = 5 // 2 # gives the floor value
# Floor --> The lowest value
# tranc --> Toward 0 value
# celing --> the upper value
import math
floor_val = math.floor(3.5) # 3
neg_floor_val = math.floor(-3.5) # 4 is lower than -3.5
tranc_val = math.trunc(3.5) # 3 : near toward 0
neg_tranc_val = math.trunc(-3.5) # 3 : near toward 0
ceil_val = math.ceil(3.4) # 4
neg_ceil_val = math.ceil(-3.4) # 3 : -3 is greater that -3.4

flag1 = True # boolean - 1 is decimal value of true
flag2 = False # boolean - 0 is decimal value of False

# some conditions 
con1 = 1 == 2 # check value, False - 0
con2 = 2 > 1 # geaterthan, True - 1
con3 = 3 < 4 # lessthan, True - 1
con4 = 2 != 4 # not equal, True - 1
con5 = 4 >= 4 # greater equal, True - 1
con6 = 6 <= 5 # less equal, False - 0

# Operations can be done in Tuples and by default it prints in tuples
x = 2
y = 3
z = 4
print(x,y,z) # (2,3,4) printed with () means it is treated as tuples
print(x * 2, y + 4, z / 2) # (4, 7, 2)

# Python can handle numbers really well and with more digit of precisions
# ** --> means power 2**100 means : 2^100
print(2**1000) # can give the acurate value

# var1 = x + y * z -->  This is not a industry oriented practise also not a good code. It will be rejected in code review. We know y * z will be done firstly then added with x but giving paranthesis is necessary for code readability
var1 = (x + y) * z # This should be done

# python can handle : 'chai' + 'code', the + operator is automatically overloaded and understands from the values that, the output is chaicode
str1 = 'chai' + 'code' # chaicode
# But it is not a good practise

# Number bases : 
oct_dig = 0o20 # 0o --> Octal : oct to deci
hex_dig = 0xFF # 0x --> hexadecimal : hex to deci 
bin_dig = 0b0110 # 0b --> binary : bin to deci
oct_dig2 = int('20',8) # Another method to convert to deci
hex_dig2 = int('FF',16) # Another method to convert to deci
bin_dig2 = int('0110',2) # Another method to convert to deci
deci_to_oct = oct(20) 
deci_to_hex = hex(64) 
deci_to_bin = bin(12)
# Bitwise operator
# binary of 4 = 0010
# so left shitf of 4 = 0100 which is 8
# left shift means shift one but to left 
# same 12 = 1100
# left shift = 00011000 which is 24 
# so, 12 << 1 --> 12 is left shift by 1 bit which gives = 24
# same goes for right shift 
# 12 = 1100
# right shift by 1 bit 0110 which 6 so, 12 >> 1
left = 14 << 2 # left shift by 2 bits
# 14 = 1110 - 14 << 2 = 00111000 - 56
right = 14 >> 2 # Right shift by 2 bits
# 14 = 1110 - 14 >> 2 = 0111 - 3

import random
random.random() # Generates a random num between 0 to 1
list1 = ["chai",3.15,"coffee",4]
random.choice(list1) # randomly chooses one from the list1
random.shuffle(list1) # Shuffles the list1 randomly
# Shuffle 1 : ['coffee', 3.15, 4, 'chai'] - output of random.shuffle
# Shuffle 2 : ['chai', 3.15, 4, 'coffee'] - output of random.shuffle
sum_x = 0.1 + 0.1 + 0.1 # 0.30000000000000004
# This is problem of precision in py
from decimal import Decimal # To solve the problem this module is imported
sum_y = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
# 0.3 
# Fractions can also be handled by module import
import fractions
frac1 = fractions.Fraction(2 , 7) # means 2 / 7
# Another way to import the specific 
from fractions import Fraction
