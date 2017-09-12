import urllib.request, json
from urllib.request import urlopen
from django.views import View

# response = urllib.request.urlopen('https://www.reddit.com/.json')
# content = response.read().decode('utf-8')
# json_content = json.loads(content)
#
# data_list = json_content['data']['children']
#
# ups_sum = 0
#
# for data in data_list:
#     ups_sum += int(data['data']['ups'])
#
# requested_json = '{"as":"AS14907 Wikimedia Foundation, Inc.",' \
#                     '"city":"San Francisco",' \
#                     '"country":"United States",' \
#                     '"countryCode":"US",' \
#                     '"isp":"Wikimedia Foundation, Inc.",' \
#                     '"lat":37.7898,' \
#                     '"lon":-122.3942,' \
#                     '"org":"Wikimedia Foundation, Inc.",' \
#                     '"query":"208.80.152.201",' \
#                     '"region":"CA",' \
#                     '"regionName":"California",' \
#                     '"status":"success",' \
#                     '"timezone":"America/Los_Angeles",' \
#                     '"zip":"94105"}'
# def get_coords(json_data):
#     json_content = json.loads(json_data)
#     json_lat = json_content['lat']
#     json_lon = json_content['lon']
#     return json_lat,json_lon
#
# print(get_coords(requested_json))

def getcoords(ip):
    response = (urllib.request.urlopen('http://ip-api.com/json/'+ ip)).read().decode()
    json_content = json.loads(response)

    return json_content['lat'], json_content['lon']
print (getcoords('93.185.19.116'))