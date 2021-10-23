# 1.1 INTEGER TYPE CONVERSION
# we use the in-built function int()
pi = 3.14  # float
print(type(pi))
# converting float  to  integer
num = int(pi)
print(pi, "As an integer : pi =", num)
# casting boolean value to an integer
bool_true = True
bool_false = False
print(type(bool_false))
num1 = int(bool_true)
num2 = int(bool_false)
# converting boolean to integer
print(bool_true, "As an integer is :", num1)
print(bool_false, "As an Integer is :", num2)
# casting a string an an integer
string_num = "225"
print(type(string_num))
# convert str to integer
# When converting string type to int type, a string must contain integral value only and should be base-10.
string_int = int(string_num)
print(string_num, "as an integer is :", string_int)
# 1.2 FLOAT TYPE CONVERSION
# we use the in built function float()
num3 = 123
print(type(num3))
# converting integer to float
num_float = float(num3)
print(num3, " As an integer is :", num_float)
# converting boolean to float using last boolean bool_true and his pal
bool_true_float = float(bool_true)
bool_false_float = float(bool_false)
print(bool_true, "and", bool_false, "as float values are : ", bool_true_float, " and ", bool_false_float, " respectively" )

# Casting integer type to complex type
r_num = 150
print(type(r_num)) # class 'int'

# converting int to complex(x)
c_num = complex(r_num)

print("Complex number:", c_num)
print(type(c_num))

# converting int to complex(x, y)
r_num, i_num2 = 150, 235
c_num = complex(r_num, i_num2)

print("Complex number:", c_num)
print(type(c_num))  # class 'complex'
