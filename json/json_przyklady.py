import json


lista=[1,3,4,'a','b']

json_list=(json.dumps(lista))

print(type(json_list))


napis='{"1":"a", "2":"b"}'
ds_napis=json.loads(napis)
print(ds_napis)
#print(type(ds_napis))


#dumps do stringów
#dump do plików
#loads i load tak samo

with open("napis.json", 'w') as fp:
    json.dump(ds_napis, fp)

with open ("napis.json") as fp:
    ob=json.load(fp)
    print(type(ob))