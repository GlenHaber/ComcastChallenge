"""
Description of code challenge:

Write a Python script that uses a module, that you create, to interface with the
Weather Underground API (https://www.wunderground.com/weather/api) to query the
current temperature and conditions in Philadelphia, PA. The results should be
printed to the screen as text. The module should be reusable.
"""
import requests

with open('api_key.cfg') as f:
    _API_KEY = f.read().strip()


def print_weather(city, state):
    """ Print the temperature and current conditions for the given city

    :param city: the full name of the city to check
    :param state: the 2-letter abbreviation for the state that the city is in
    """
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
