import requests

site = 'http://api.wunderground.com/api/'
endpoint = '/conditions/q/PA/Philadelphia.json'
key = '4b787f11700ab380'

page = site + key + endpoint

response = requests.get(page)
weather = response.json()

temperature = weather['current_observation']['temp_f']
conditions = weather['current_observation']['weather']

print('Weather in Philadelphia:')
print('{}, {}°F'.format(conditions, temperature))