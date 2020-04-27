import json

a = {
    'name' : "Manoj",
    "age" : 24,
    "city" : "Delhi",
    "items" : ["mobile", "laptop", "headphone"]
}

file = json.dumps(a, indent=4)

with open("demo.json", "w")as fh:
    fh.write(file)