import urllib.request
import json
import pprint

url = "http://api.open-notify.org/astros.json"

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    j = json.loads(response_text) # j is a dictionary
    print(j) 
    print(type(data))

# Can you print number of people in the space?
print(data['number'])

# Can you print all the names?
for person in data['people']:
    print(person['name'])
