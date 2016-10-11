# Insert 'multiplication table' to represent the 'title'
# By using '\n' to distinguish output line from the command line
print('\n Multiplication table\n')
# Using 'int' to specify the type of data, 'integer' and using 'input' to enter an integer
num = int(input(' 구구단 : '))
# By using the 'for' loop and the built-in function 'range', muliply input integer by 1 to 9
for i in range(1, 10):
# Insert marginal spacing to make it more readable
    print('', num, ' x ', i, ' = ', num * i)