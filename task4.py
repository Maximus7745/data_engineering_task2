import json
import pickle

with open("products_24.pkl", "rb") as f_out:
    products = pickle.load(f_out)
print(products)
with open("price_info_24.json") as f_out:
    price_info = json.load(f_out)

price_info_dict = dict()

for info in price_info:
    price_info_dict[info['name']] = {
        'param' : info['param'],
        'method' : info['method']
    }

def update_price(product):
    name = product['name']
    info = price_info_dict[name] 
    method = info["method"]
    if method == "sum":
        product["price"] += info["param"]
    elif method == "sub":
        product["price"] -= info["param"]
    elif method == "percent+":
        product["price"] *= (1 + info["param"])
    elif method == "percent-":
        product["price"] *= (1 - info["param"])
    product["price"] = round(product["price"], 2)

for product in products:
    update_price(product)
    
print(products)

with open("products_updated.pkl", "wb") as f:
    f.write(pickle.dumps(products))