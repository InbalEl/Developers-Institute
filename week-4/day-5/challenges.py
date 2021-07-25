print('-----EX1------')

l = ['a', 'b', 'c', 'd']
l[3] = 'D'

print(l)

print('-----EX2------')

my_str = 'Hello. My name is Inigo Montoya. You killed my father. Prepare to die.'

print(my_str)
print(my_str.count(' '))

print('-----EX3------')

print(sum(1 for letter in my_str if letter.isupper()))

print('-----EX4------')

def my_sum(array: list):
    ttl = 0
    for item in array:
        ttl += item

    return ttl


print(my_sum([1,2,3,4,5]))

print('-----EX5------')

def find_max(arr: list):
    return sorted(arr)[-1:]

print(find_max([4,8,2,33,5,86]))

print('-----EX6------')

def factorial(num: int):
    ttl = 1
    for number in range(1, num+1):
        ttl *= number
    return ttl

print(factorial(5))

print('-----EX7------')

def list_count(l: list, elem):
    ttl = 0
    for item in l:
        if elem == item:
            ttl += 1
    return ttl

print(f"list_count(['H','e','l','l','o'], 'l'): {list_count(['H','e','l','l','o'], 'l')}")

print('-----EX8------')
import math
#square root of the sum of squares
def norm(l: list):
    return math.sqrt(sum(num**2 for num in l))

print(norm([1,2,3]))

print('-----EX9------')

def is_mono(l: list):
    sorted_l = sorted(l)
    return l == sorted_l or l == sorted_l.reverse()

print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))

print('-----EX10------')

def longest_word(l):
    l.sort(key=len)
    return l[-1]

print(longest_word(['Hello','my','name','is']))

print('-----EX11------')

def split_list(l):
    print(l)
    str_l = [elem for elem in l if isinstance(elem, str)]
    int_l = [elem for elem in l if isinstance(elem, int)]
    print(str_l)
    print(int_l)

split_list(['Hello', 2, 'World', 7])

print('-----EX12------')

def is_pal(string):
    return string == string[::-1]

print(is_pal('abcba'))
print(is_pal('abba'))
print(is_pal('abcd'))

print('-----EX13------')

def count_words_by_len(string, length):
    words = string.split()
    return sum(1 for word in words if len(word) > length)

print(count_words_by_len('Hello. My name is Inigo Montoya. You killed my father. Prepare to die.', 3))

print('-----EX14------')

def avg_val(d: dict):
    values = d.values()
    return sum(values) / len(values)

print(avg_val({'a': 1,'b':2,'c':8,'d': 1}))

print('-----EX15------')

def com_div(num1, num2):
    com_dividors = []

    for number in range(2, min(num1, num2) + 1):
        if num1%number == num2%number == 0:
            com_dividors.append(number)
    return com_dividors

print(com_div(10,20))

print('-----EX16------')

def is_prime(num):
    return (com_div(num, num) == [num])

print(is_prime(11))

print('-----EX17------')

def weird_print(l):
    res = []
    for index, elem in enumerate(l):
        print(index, elem)
        if index%2 == elem%2 == 0:
            res.append(elem)
    return res

print(weird_print([1,2,2,3,4,5]))

print('-----EX18------')

def type_count(**kwargs):
    values = kwargs.values()
    print(values)

    str_l = [val for val in values if type(val) is str]
    int_l = [val for val in values if type(val) is int]
    bool_l = [val for val in values if type(val) is bool]
    float_l = [val for val in values if type(val) is float]

    print(str_l)
    print(int_l)
    print(bool_l)
    print(float_l)

    res = {
        'int': len(int_l),
        'str': len(str_l),
        'bool': len(bool_l),
        'float': len(float_l)
    }

    return res

print(type_count(a=1,b='string',c=1.0,d=True,e=False))

print('-----EX19------')

def my_split(s, sep = ' '):

    print(s)
    res = []
    next_sep_i = s.find(sep)
    print(next_sep_i)
    while(next_sep_i != -1):
        word = s[:next_sep_i]
        print(word)

        res.append(s[:next_sep_i])
        s = s[next_sep_i + len(sep):]
        next_sep_i = s.find(sep)

    res.append(s[:next_sep_i])
    return res

print(my_split('Hello. My name is Inigo Montoya. You killed my father. Prepare to die.'))

print('-----EX20------')

def convert_to_pass(s):
    return '*'*len(s)

print(convert_to_pass("mypassword"))