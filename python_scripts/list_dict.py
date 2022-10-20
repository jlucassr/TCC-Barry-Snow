from typing import Dict, List


lista: List = []
dictionary: Dict[str, int] = {}

list_dict_variable: int = 1

lista.append(list_dict_variable)
dictionary['list_dict'] = list_dict_variable

print('List %s' % lista)
print('Dict %s' % dictionary)
