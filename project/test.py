import http.client, urllib.parse
import json

conn = http.client.HTTPConnection('geocode.xyz')

params = urllib.parse.urlencode({
    'auth': '156997931047459624760x95680',
    'locate': 'chintal ',
    'region': 'IN',
    'json': 1,
    })

conn.request('GET', '/?{}'.format(params))

res = conn.getresponse()
data = res.read()
json_data = json.loads(data)
print(json_data["longt"])
print(json_data["latt"])

print(data)