import json

raw = ""
with open("data.txt") as f:
    raw = f.read()

parts = raw.split("link:")

content = parts[0].strip()
result = {}

for i in range(1, len(parts)):
    new_parts = parts[i].split("\n")
    options = new_parts[0].split(',')
    del new_parts[0]

    ent = content.split(".")[0]

    result[ent] = {
        "content": content,
        "options": options
    }

    content = '\n'.join(new_parts).strip()

print(json.dumps(result))
