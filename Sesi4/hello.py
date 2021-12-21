# f = open('hello.txt', 'r', encoding='utf-8')
# print(f.read(8))
# print(f.tell())
# f.seek(0)
# print('')
# print(f.read())
# f.close()

# f = open('hello.txt', 'r', encoding='utf-8')
# f.seek(0)
# for line in f:
#     print(line, end='')
# print('')

# f = open('hello.txt', 'r', encoding='utf-8')
# print(f.readline())
# fileRows = f.readlines()
# print(fileRows[1])

# with open('hello.txt', 'a', encoding='utf-8') as f:
#     f.write('\nsaya lulusan')
#     f.write('\nInstitut Teknologi Sepuluh Nopember Surabaya')
#     f.write('\nDepartemen Teknik Komputer')
#     f.write('\nFakultas Teknologi Elektro dan Informatika Cerdas')
#     f.close()

# try:
#     f = open('hello.txt', 'r', encoding='utf-8')
# finally:
#     f.close()

# with open('sample.txt', 'w', encoding='utf-8') as f:
#     f.write("hallo")
#     f.write("dunia")
#     f.write("saya")
#     f.write("agung")
#     f.close()

# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# import sys
# assert ('linux' in sys.platform), "This code runs on Linux only."
# assert ('windows' in sys.platform), "This code runs on Windows only."

# x=22
# assert x==20, "x harus 20"

# x=22
# assert(x == 20), "berbeda"

# import sys

# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('windows' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

# try:
#     os_interaction()
# except:
#     print('Windows function was not executed')

# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
#     print('The os_interaction() function was not executed')

# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Could not open file.log')

# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)

# import sys

# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     # assert ('windows' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     print('Executing the else clause.')

import sys

def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    # assert ('windows' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)

try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')