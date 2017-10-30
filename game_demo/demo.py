import json
import sys

with open("parse_output.json") as f:
    data = json.loads(f.read())

state = "FIN"

while True:
    print(data[state]["content"])
    for opt in data[state]["options"]:
        print("-> " + opt)

    new_state = sys.stdin.readline().strip()
    if new_state in data:
        state = new_state
    elif new_state == "" and data[state]["default"] != None:
        state = data[state]["default"]
