import urllib.request as request
import json

key = "8b5513298582ac4a"
zip_code = input('For which ZIP code would you like to see the weather?')
filename = "http://api.wunderground.com/api/" + key + "/geolookup/conditions/q/PA/" + zip_code + ".json"
f = request.urlopen(filename)
json_string = f.read().decode('utf-8')
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print("Current temperature in %s is: %s" % (location, temp_f))
