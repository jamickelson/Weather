import urllib.request as request
import json

key = "8b5513298582ac4a"
zip_code = input('For which ZIP code would you like to see the weather?')
filename = "http://api.wunderground.com/api/" + key + "/geolookup/forcast/q/PA/" + zip_code + ".json"
f = request.urlopen(filename)
json_string = f.read().decode('utf-8')
parsed_json = json.loads(json_string)

for day in parsed_json['forecast']['simpleforecast']['forecastday']:
	print (day['date']['weekday'] + ":")
	print ("Conditions: ",day['conditions'])
	print ("High: ",day['high']['celsius'] + "C","Low",day['low']['celsius'] + "C")

print("Current temperature in %s is: %s" % (location, temp_f))
