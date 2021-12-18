# # Introduction to the if Statement
# x = 0
# y = 5

# if x < y:
#     print('yes')

# if y < x:
#     print('yes')

# if x:
#     print('yes')

# if y:
#     print('yes')

# if 'aul' in 'grault':
#     print('yes')

# if 'quux' in ['foo', 'bar', 'baz']:
#     print('yes')

# # Grouping Statements: Indentation and Blocks
# if 'foo' in ['bar', 'baz', 'qux']:
#     print('Expression was true')
#     print('Executing statement in suite')
#     print('...')
#     print('Done.')
    
# print('After conditional')

# # More complex grouping Does line execute?                        Yes    No
# #                                           ---    --
# if 'foo' in ['foo', 'bar', 'baz']:        #  x
#     print('Outer condition is true')      #  x

#     if 10 > 20:                           #  x
#         print('Inner condition 1')        #        x

#     print('Between inner conditions')     #  x

#     if 10 < 20:                           #  x
#         print('Inner condition 2')        #  x

#     print('End of outer condition')       #  x
# print('After outer condition')            #  x

# # logic operator
# x = 13
# sunny = False
# if x >= 10 or x<=15 and not sunny:
#     print(x)

# # The else and elif Clauses
# hargaBuku = 20000
# hargaMajalah = 5000
# uang = 2000

# if uang > hargaBuku:
#     print("beli buku")
# elif uang > hargaMajalah:
#     print("beli majalah")
# else:
#     print("uang tidak cukup")

# # One-Line if Statements
# if 'f' in 'foo': print('1'); print('2'); print('3')

# # Conditional Expressions (Python’s Ternary Operator)
# raining = True
# print("Let's go to the", 'beach' if not raining else 'library')
# print('yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no')

# # The break and continue statements
# n = 5
# while n>0:
#     n-=1
#     if n==2:
#         continue
#     print(n)
# print('Loop End')

# # Nested while loops
# a = ['foo', 'bar']
# while len(a):
#     print(a.pop(0))
#     b = ['baz', 'qux']

#     while len(b):
#         print('>', b.pop(0))

# One-line while loops
n = 5
while n > 0:n -= 1;print(n)

# # the python for loop
# a = ['foo', 'bar', 'baz']
# for i in a:
#     print(i)

# # the range() function
# x=range(5)
# for n in x:
#     print(n)

# # alternating for loop behavior
# for i in ['foo', 'bar', 'baz', 'qux']:
#     if 'b' in i:
#         break
#     print(i)

# for i in ['foo', 'bar', 'baz', 'qux']:
#     if 'b' in i:
#         continue
#     print(i)
