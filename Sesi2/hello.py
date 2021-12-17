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

# # One-line while loops
# n = 5
# while n > 0:n -= 1;print(n)

# # the python for loop
# a = ['foo', 'bar', 'baz']
# for i in a:
#     print(i)

# # the range() function
# x=range(5)
# for n in x:
#     print(n)

# alternating for loop behavior
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)