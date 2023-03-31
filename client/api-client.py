import linecache
import json
import requests


start = 1
end = 100

i = start

while i <= end:
    line = linecache.getline("./data/output.txt", i)
    json_data = json.loads(line)
    response = requests.post('http://localhost:80/invoiceitem', json=json_data)
    print(response.json())
    i += 1