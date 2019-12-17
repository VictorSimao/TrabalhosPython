# isintance(object, type) retorna True se o objeto for do type apresentado, pode colocar mais de um type

# x = isinstance('Hello', (float,int,str,list,dict,tuple))

# print(x)

# l = [1,2,3,'a','b','c',4,5,6]

# def filter_list(l):
#     return [i for i in l if not isinstance(i, str)]

# lista = filter_list(l)

# print(max(lista),min(lista))

# maxmin = (f'{max(lista)} {min(lista)}')

# print(maxmin)

numbers = ("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")

list_numbers = numbers.split(" ")

print(list_numbers)

numbers = str(max(list_numbers, key=int))

print(numbers)

numbers += " "

numbers += str(min(list_numbers, key=int))

print(numbers)

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

print(high_and_low(numbers))