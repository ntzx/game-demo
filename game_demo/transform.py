import json

with open("parse_output.json") as f:
    data = json.loads(f.read())

black = {}
for k in data:
    black[k] = False

views = []
key_ids = {}

def dfs(k):
    if black[k]:
        return key_ids[k]
    black[k] = True
    key_ids[k] = len(views)
    item = data[k]
    v = {
        "description": item["content"],
        "choices": []
    }
    views.append(v)

    for c in item["options"]:
        if not c in data:
            continue
        v["choices"].append({
            "description": c,
            "target_view_id": dfs(c)
        })

    return key_ids[k]

dfs("FIN")

print(json.dumps({
    "views": views,
    "initial_view_id": 0
}))
