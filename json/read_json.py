import json

with open("states.json") as f:
    data = json.load(f)

    for state in data['states']:
        print(state)

with open("new_states.json", "w")as f:
    json.dump(data, f, indent=4)