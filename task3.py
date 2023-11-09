import json
import os
import msgpack

address_in = 'products_24.json'

with open(address_in, 'r') as f_in:
    products = json.load(f_in)

dict_result = dict()

for product in products:
    name = product['name']
    price = product['price']
    if(name in dict_result):
        dict_result[name]['count'] += 1
        dict_result[name]['avg'] += price
        if(dict_result[name]['max'] < price):
            dict_result[name]['max'] = price
        if(dict_result[name]['min'] > price):
            dict_result[name]['min'] = price
    else:
        dict_result[name] = {
            'name' : name,
            'max' : price,
            'min' : price,
            'avg' : price,
            'count' : 1
        }

result = list()
for key in dict_result:
    elem = dict_result[key]
    elem['avg'] /= elem.pop('count')
    result.append(elem)


with open('product_result.json', 'w') as f_out:
    f_out.write(json.dumps(result))

with open('product_result.msgpack', 'wb') as f_out:
    f_out.write(msgpack.dumps(result))

print(f"json = {os.path.getsize('product_result.json')}")
print(f"msgpack = {os.path.getsize('product_result.msgpack')}")