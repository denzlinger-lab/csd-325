# Abram Denzlinger
# November 17, 2025
# 7.2 - Test Cases

# accepts city and country, formats city and country,
# and returns as a formatted string.
def format_city_country(city, country, population='', language=''):
    formatted_str = f'{city.strip().lower().title()}, {country.strip().lower().title()}'
    if population:
        formatted_str += f' - Population {population}'
    if language:
        formatted_str += f', {language.strip().lower().title()}'
    return formatted_str



print(format_city_country('houston', 'united states'))
print(format_city_country('salt lake city', 'united states', '70000'))
print(format_city_country('san paulo', 'brazil', '90000', 'portuguese'))
