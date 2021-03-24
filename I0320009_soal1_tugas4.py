# Exercise 4.1
x = 15
y = 4

# Output: x + y = 19
print('x + y =', x+y)

# Output: x - y = 11
print('x - y =', x-y)

# Output: x * y = 60
print('x * y =', x*y)

# Output: x / y = 3.75
print('x / y =', x/y)

# Output: x // y = 3
print('x // y =', x//y)

# Ouput: x ** y = 50625
print('x ** y =', x**y)


# Exercise 4.2
x = 10
y = 12

# Output: x > y is False
print('x > y is', x>y)

# Output: x < y is True
print('x < y is', x<y)

# Output: x == y is False
print('x == y is', x==y)

# Output: x != y is True
print('x != y is', x!=y)

# Output: x >= y is False
print('x >= y is', x>=y)

# Output: x <= y is True
print('x <= y is', x<=y)


# Exercise 4.3
x = True
y = False

print('x and y is', x and y)

print('x or y is', x or y)

print('not x is', not x)


# Exercise 4.4
# strings

str1 = "Hello"
str2 = "World"

# concat
result = str1 + " " + str2

# output
print(result);


# Exercise 4.5
# string
str = "HA"

# replicate
result = str * 3

# output
print(result)


# Exercise 4.6
# strings
needle = "lo"
haystack = "Hello World"

# check
if needle in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("Not found")


# Exercise 4.7
# strings
needle = "HA"
haystack = "Hello World"

# check
if needle in haystack :
    print(needle, "is present in the string", haystack)

else:
    print("Not found")


# Exercise 4.8
# string
str = "Jane Doe"

# character
ch = str[1]

# output
print(ch)   # a


# Exercise 4.9
# string
str = "Hello World"

# substring
substr = str[3:5]

# output
print(substr)   # lo


# Exercise 4.10
# string
str = "Hello World"

# skip
new_str = str[0::2]
print(new_str)


# Exercise 4.11
# string
str = "Hello World"

# reverse
result = str[::-1]

# output
print(result)