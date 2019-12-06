"""
    @reroes
    - uso de reduce
    -  uso de groupby
"""
from functools import reduce
from itertools import *
import pandas as pd

data = pd.read_csv("data01.csv", sep=";")
data_record = data.to_dict("records")
# print(data_record)

# lista del groupby
lista = list(map(lambda x: [x[0], list(x[1])], 
    groupby(data_record, lambda x: x['Cliente'])))

print(lista)
print("--------------------------------")
print(list(map(lambda x:[x[0], list(map(lambda x: list(x.items()), 
    x[1]))] ,lista)))
print("--------------------------------")
print(list(map(lambda x:[x[0], list(map(lambda x: list(x.items())[3][1], 
    x[1]))] ,lista)))

print("--------------------------------")
# aplicado el reduce (sumar los valores de los pedidos de los clietes
print(list(map(lambda x:[x[0], reduce(lambda a,b: a+b, 
    list(map(lambda x: list(x.items())[3][1], x[1])))] ,lista)))

