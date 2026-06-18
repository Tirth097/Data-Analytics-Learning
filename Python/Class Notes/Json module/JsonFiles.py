import json

# with open ("E:\Material\Coding\Python\Json module\data.json","r") as f:
#     py_obj = json.load(f)
#     print(type(py_obj),py_obj)
    
data = {
    "new data " : True,
    "name":"tirth"
}

with open ("E:\Material\Coding\Python\Json module\data.json","w") as f:
    json.dump(data,f,indent=4,sort_keys=True)
    