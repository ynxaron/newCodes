import json
rawjson = '{"name":"John", "age":30, "city":"NYC"}'

thisjson = json.loads(rawjson)
print(thisjson["age"])
