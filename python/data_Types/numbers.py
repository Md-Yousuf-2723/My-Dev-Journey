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
# 