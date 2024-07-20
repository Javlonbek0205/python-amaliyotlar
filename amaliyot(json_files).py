import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

malumot_json = json.dumps(data)
print(malumot_json[1])

print(type(malumot_json))

malumot = json.loads(malumot_json)
print(malumot)
print(type(malumot))