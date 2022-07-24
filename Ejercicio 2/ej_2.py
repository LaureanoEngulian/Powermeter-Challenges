import json

repetidos = [1,2,3,"1","2","3",3,4,5]

r = [1,"5",2,"3"]

d_str = '{"valor":125.3,"codigo":123}'

lista_1 = print(set(repetidos))
lista_2 = print(set(repetidos).intersection(r))
str_to_dic = json.loads(d_str)
print(str_to_dic)
print(type(str_to_dic))