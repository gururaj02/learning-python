import json

user = {
    "name": "Gururaj",
    "age": 22
}

json_data = json.dumps(user)

print(json_data)