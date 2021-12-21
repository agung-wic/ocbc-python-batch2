# # Using Generator
# def my_generator():
#   print("Inside my generator")
#   yield 'a'
#   yield 'b'
#   yield 'c'

# my_generator()

# for char in my_generator():
#   print(char)

# def counter_generator(low, high):
#     while low <= high:
#        yield low
#        low += 1

# for i in counter_generator(5,10):
#   print(i, end=' ')
# print('')

# # First-class Object
# def say_hello(name):
#     return f"Hello {name}"

# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"

# def greet_bob(greeter_func):
#     return greeter_func("Bob")

# print(greet_bob(say_hello))
# print(greet_bob(be_awesome))

# # Inner Function
# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()

# parent()

# # Returning Functions From Functions
# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"

#     def second_child():
#         return "Call me Liam"

#     if num == 1:
#         return first_child
#     else:
#         return second_child

# first = parent(1)
# print(first())

# simple decorator
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)

# say_whee()

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

# import functools
# import time

# def timer(func):
#     """Print the runtime of the decorated function"""
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()    # 1
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()      # 2
#         run_time = end_time - start_time    # 3
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         return value
#     return wrapper_timer

# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i**2 for i in range(10000)])

# waste_some_time(999)

# different between function and generator
# def square(nums):
#     result = []
#     for num in nums:
#         result.append(num*num)
#     return result

# nums = [1,2,3,4,5]
# print(square((nums)))

# def square(nums):
#     for num in nums:
#         yield num*num   

# nums = [1,2,3,4,5]
# a = square(nums)
# print(a.__next__())
# print(a.__next__())

# # list comprehension
# num = [y * y for y in [1,2,3,4,5]]
# print(num)

# nom = [y+4 for y in range(7)]
# print(nom)

# # Make generator with expression

# num = (y*y for y in range(5))

# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))