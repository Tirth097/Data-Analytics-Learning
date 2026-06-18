import json

json_str = '{"name":"tirth","isStudent":null}' #small t for javscript formate, null 
py_obj = json.loads(json_str)
print(type(py_obj),py_obj)

python_obj = {
    "name":"tirth",
    "is_student":True, # -> goes to true in javascript
    "id":None # -> goes to null 
}
json_obj = json.dumps(python_obj)
print(type(json_obj),json_obj)