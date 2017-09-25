import requests


def print_weather(city, state):
    city = city.title().replace(' ', '_')
    state = state.upper()
    site = 'http://api.wunderground.com/api/'
    endpoint = '/conditions/q/{}/{}.json'.format(state, city)
    key = '4b787f11700ab380'

    page = site + key + endpoint

    response = requests.get(page)
    weather = response.json()

    temperature = weather['current_observation']['temp_f']
    conditions = weather['current_observation']['weather']

    print('Weather in {}:'.format(city))
    print('{}, {}°F'.format(conditions, temperature))


if __name__ == '__main__':
    print_weather('philadelphia', 'pa')
