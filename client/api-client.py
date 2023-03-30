
import json

with open("./data/output.txt") as f:
    count = 0
    for line in f:
        try:
            json.loads(line)
            count+=1
        except json.JSONDecodeError:
            pass

print(f"Json has: {count}")