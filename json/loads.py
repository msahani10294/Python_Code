import json

a = '''{
    "name": "Manoj",
    "age": 24,
    "city": "Delhi",
    "items": [
        "mobile",
        "laptop",
        "headphone"
    ]
}'''

contant = json.loads(a)
# contant = json.dumps(a)

