import itertools
import re


def sort_list(data):
    #data = ['yellow','white','2','5','green','red','6','1']
    tmp_digits = []
    tmp_str = []
    for i in data:
        try:
            int(i)
            tmp_digits.append(i)
        except ValueError:
            tmp_str.append(i)

    tmp_digits.sort()
    tmp_str.sort()
    i_dig, i_str = 0, 0
    for i in range(0, len(data)):
        try:
            int(data[i])
            data[i] = tmp_digits[i_dig]
            i_dig += 1
        except ValueError:
            data[i] = tmp_str[i_str]
            i_str += 1

    return data


def find_digit_diff(digits):
    #digits = [0, 8, 2, 50, 19, 6, 34]
    odd = []
    even = []
    i = 0
    while True:
        if digits[i] % 2 == 1:
            odd.append(digits[i])
        else:
            even.append(digits[i])
        i += 1
        if i >= 2:
            if len(odd) >= 2:
                condition = 0
                break
            if len(even) >= 2:
                condition = 1
                break

    for x in digits:
        if x % 2 == condition:
            return x


def max_dig(digits):
    #dig = [70, 8, 20, 1, 13]
    #dig2 = [89, 8, 892, 1, 103]
    list_str = [str(x) for x in digits]
    lists_dec_str = itertools.permutations(list_str)
    result_str = [''.join(row) for row in lists_dec_str]
    return int(max(result_str))


def names_concatenation(names_dict):
    #names_dict = [{'name': 'John'}, {'name': 'Jack'}, {'name': 'Joe'}]
    #names_dict = [{'name': 'John'}, {'name': 'Jack'}]
    #names_dict = [{'name': 'John'}]
    names_list = [x['name'] for x in names_dict]
    result = ', '.join(x for x in names_list)
    if len(names_list) > 1:
        index = result.rfind(', ')
        substr = ' &'
        result = result[:index] + substr + result[index+1:]
    return result


def camel_case(row):
    #row = 'the_phantom_menace'
    #row = 'The-Phantom-Menace'
    #row = 'The-Phantom_Menace'
    words = re.split('-|_', row)
    for i in range(1, len(words)):
        words[i] = words[i][0].upper() + words[i][1:]
    return ''.join(words)


def count_portion(recipe,available):
    #recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    #available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    recipe_keys = recipe.keys()
    result_list = [int(available[key]/recipe[key]) for key in recipe_keys]
    return min(result_list)


# main
print('Task 1')
data = ['yellow', 'white', '2', '5', 'green', 'red', '6', '1']
print(sort_list(data))

print('\nTask 2')
digits = [0, 8, 2, 50, 13, 6, 34]
print(find_digit_diff(digits))

print('\nTask 3')
digits = [70, 8, 20, 1, 13]
print(max_dig(digits))
digits = [89, 8, 892, 1, 103]
print(max_dig(digits))

print('\nTask 4')
names_dict = [{'name': 'John'}, {'name': 'Jack'}, {'name': 'Joe'}]
print(names_concatenation(names_dict))
names_dict = [{'name': 'John'}, {'name': 'Jack'}]
print(names_concatenation(names_dict))
names_dict = [{'name': 'John'}]
print(names_concatenation(names_dict))

print('\nTask 5')
row = 'the_phantom_menace'
print(camel_case(row))
row = 'The-Phantom-Menace'
print(camel_case(row))
row = 'The-Phantom_Menace'
print(camel_case(row))

print('\nTask 6')
recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(count_portion(recipe, available))
