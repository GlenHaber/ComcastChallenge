import requests

with open('api_key.cfg') as f:
    _API_KEY = f.read().strip()


def print_weather(city, state):
    city = city.title().replace(' ', '_')
    state = state.upper()
    site = 'http://api.wunderground.com/api/'
    endpoint = '/conditions/q/{}/{}.json'.format(state, city)

    page = site + _API_KEY + endpoint

    response = requests.get(page)
    weather = response.json()
    if 'error' in weather['response']:
        print(weather['response']['error']['description'])
        return

    temperature = weather['current_observation']['temp_f']
    conditions = weather['current_observation']['weather']

    print('Weather in {}:'.format(city))
    print('{}, {}°F'.format(conditions, temperature))


if __name__ == '__main__':
    print_weather('philadelphia', 'pa')
