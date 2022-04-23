# IF ELSE statement
from unittest import result


def condition(nilai):
    print('Condition function')
    if nilai > 65:
        print('Lulus')
    else:
        print('Tidak Lulus')

def comp_condition(value):
    return value - 5 if value >10 else value / 0

# For loop Statement
def looping1(n=5):
    for x in range(n):
        if x > 6:
            x += 2
        print(x)

# List
def list1():
    value = [1,3,'4',5.0,6,3,5, False, None]
    print('list type')
    print(value, 'type', type(value))
    print('item type')
    for v in value:
        print(v, 'type', type(v))


# Tuple
def multi_value():
    return 10, 20, True

# Dictionary
def dictionary_1():
    data = {
        'name': 'Rudi', 
        'nilai': 75,
        'alamat': 'jakarta'
    }
    return data

def dictionary_2():
    data = {
        'name': 'Lisa', 
        'nilai': 90,
        'alamat': 'jakarta',
        'semester': 4
    }
    return data

# Equation
def data_list(value_list):
    n = 0
    for value in value_list:
        print('n=', n)
        print('x=', value)
        n += 1 

def equation_1(value_list):
    n = 0
    item_res_list = []
    for value in value_list:
        item_res = (n-1)**2 * value**n
        item_res_list.append(item_res)
        n += 1
    return sum(item_res_list)

def equation_2(value_list):
    return sum([
        (n-1)**2 * x**n
        for n, x in enumerate(value_list)
    ])

def equation_3(value_list):
    return sum([
        1/(x**2-x**3)
        for x in value_list
    ])