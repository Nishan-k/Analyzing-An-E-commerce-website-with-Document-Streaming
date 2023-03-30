
import json
<<<<<<< HEAD
import linecache
import requests
# with open("./data/output.txt") as f:
#     count = 0
#     for line in f:
#         try:
#             json.loads(line)
#             count+=1
#         except json.JSONDecodeError:
#             pass
start = 1
end = 100
=======

with open("./data/output.txt") as f:
    count = 0
    for line in f:
        try:
            json.loads(line)
            count+=1
        except json.JSONDecodeError:
            pass
>>>>>>> parent of e79e96f (changes)

print(f"Json has: {count}")