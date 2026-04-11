import json

data = '{"name": "Gururaj", "age": 23}'

parsed = json.loads(data);

print(parsed)
print(parsed["name"])