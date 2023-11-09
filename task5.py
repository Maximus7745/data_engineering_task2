import os
import csv
import json
import pickle
import msgpack
import numpy as np

filename_in = 'Market_Sale_Ratio.csv'
filename_out = 'res5.json'
filename_data_out = 'data'


results = list()
data = list()
rows = dict()

def getStartNum(row, idx):
    if(row[idx] == ''):
        return getStartNum(row, idx + 1)
    else:
        return float(row[idx])

def getSigma(row, avg, lenght):
    sigma = 0
    for n in row:
        if(n != ''):
            num = float(n)
            sigma += (num - avg) ** 2
    sigma = np.sqrt(sigma / lenght)
    return sigma


def getParamsForNumbers(key):
    row = rows[key]
    startNum = getStartNum(row, 0)
    res = {
        'name' : key,
        'min' : startNum,
        'max' : startNum,
        'avg' : startNum,
        'sum' : startNum,
        'sigma' : 0
    }
    lenght = 0
    for n in row:
        if(n != ''):
            lenght += 1
            num = float(n)
            if(num < res['min']):
                res['min'] = num
            if(num > res['max']):
                res['max'] = num
            res['sum'] += num
    res['avg'] = res['sum'] / lenght
    res['sigma'] = getSigma(row, res['avg'], lenght)
    return res

def getParamsForStrings(key):
    row = rows[key]
    res = {
        'name' : key,
    }
    for s in row:
        if(s in res):
            res[s] += 1
        else:
            res[s] = 1
    for k in res.keys():
        if(k != 'name'):
            res[k] /= len(row)

    return res


with open(filename_in, encoding='utf-8') as f_in:
    lines = list(csv.reader(f_in, delimiter=','))
    for i in range(1,len(lines)):
        line = lines[i]
        item = {
             'X': line[0],
             'Y': line[1],
             #'OBJECTID': line[2],
             #'PIN': line[3], 
             'HOUSI_UNIT_TYPE': line[4],
             'MARKE_SALE_RATIO': line[5],
             'MARKE_VALUE': line[6],
             'ASSES_VALUE': line[7],
             'SALES_VALUE': line[8],
             #'VALID_FROM': line[9],
             #'VALID_TO': line[10],
             #'PARCE_ID': int(line[11])
        }

        data.append(item)


for key in data[0].keys():
    rows[key] = []

for item in data:
    for key in item.keys():
        rows[key].append(item[key])
    
for key in rows:
    if(key != 'HOUSI_UNIT_TYPE'):
        results.append(getParamsForNumbers(key))
    else:
        results.append(getParamsForStrings(key))



with open(filename_out, 'w') as f_out:
    f_out.write(json.dumps(results))

with open(filename_data_out + '.csv', 'w', encoding='utf-8', newline='') as f_out:
    writer = csv.writer(f_out)
    for line in data:
        writer.writerow(line.values())

with open(filename_data_out + '.json', 'w') as f_out:
    f_out.write(json.dumps(data))

with open(filename_data_out + '.pkl', "wb") as f:
    f.write(pickle.dumps(data))

with open(filename_data_out + '.msgpack', 'wb') as f_out:
    f_out.write(msgpack.dumps(data))

print(f"csv = {os.path.getsize(filename_data_out + '.csv')}") #1
print(f"json = {os.path.getsize(filename_data_out + '.json')}") #4
print(f"pkl = {os.path.getsize(filename_data_out + '.pkl')}") #2
print(f"msgpack = {os.path.getsize(filename_data_out + '.msgpack')}") #3