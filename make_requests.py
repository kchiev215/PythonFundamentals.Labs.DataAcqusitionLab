import urllib.request
import json

offset_counter = 1
file = 0

while file < 39:
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&' + 'offset=' + str(offset_counter)
    req = urllib.request.Request(url, headers={'TOKEN': 'BwEQHKXofzVilsfljZDVTimCdklIiGLh'})
    file_name = 'location_' + str(file) + '.json'
    with urllib.request.urlopen(req) as f:
        data = json.load(f)
    with open(file_name, 'w') as w:
        json.dump(data, w)
    file += 1
    offset_counter += 1000

