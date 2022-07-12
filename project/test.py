import http.client


connection = http.client.HTTPSConnection("www.journaldev.com")
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))

connection.close()
