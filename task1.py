import numpy as np
import json

address_in = 'matrix_24.npy'
address_out = 'res1.json'

matrix = np.load(address_in)

print(matrix)

result = { 
    'sum': 0,  
    'avr': 0,  
    'sumMD': 0, 
    'avrMD': 0,  
    'sumSD': 0, 
    'avrSD': 0,  
    'max': matrix[0][0],   
    'min': matrix[0][0]   
}
size = len(matrix)
for i in range(size):
    for j in range(size):
        elem = matrix[i][j]
        result['sum'] += elem
        if(i == j):
            result['sumMD'] += elem
        if(i + j == len(matrix) - 1):
            result['sumSD'] += elem
        if(elem > result['max']):
            result['max'] = elem
        if(elem < result['min']):
            result['min'] = elem
        
result['avr'] = result['sum'] / (size * size)
result['avrMD'] = result['sumMD'] / size
result['avrSD'] = result['sumSD'] / size

for key in result.keys():
    result[key] = float(result[key])

with open(address_out, 'w') as f_out:
    f_out.write(json.dumps(result))


norm_matrix = np.ndarray((size,size),dtype = float)


for i in range(size):
    for j in range(size):
        norm_matrix[i][j] = matrix[i][j] / result['sum']

np.save('norm_matrix.npy', norm_matrix)