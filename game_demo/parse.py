import json

raw = ""
with open("data_2.txt") as f:
    raw = f.read()

parts = raw.split("link:")

content = parts[0].strip()
result = {}

for i in range(1, len(parts)):
    new_parts = parts[i].split("\n")
    options = new_parts[0].split(',')
    default = None

    for i in range(len(options)):
        opt = options[i]
        if len(opt) > 0 and opt[0] == ':':
            default = opt[1:]
            del options[i]

    del new_parts[0]

    ent = content.split(".")[0]

    result[ent] = {
        "content": content,
        "options": options,
        "default": default
    }

    content = '\n'.join(new_parts).strip()

print(json.dumps(result))
