# import urllib, json
from urllib import request
import json

url = "https://transparency-in-coverage.uhc.com/"
response = request.urlopen(url)
print(response.read())
# data = json.loads(response.read())
# print (data)