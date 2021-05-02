from bs4 import BeautifulSoup
import requests

url = 'https://yandex.kz/pogoda/almaty/month/june?via=cnav'



def get_data(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    return soup

def foo():
  soup = get_data(url)
  climate_calendar = soup.find('div', {'class': 'climate-calendar'})

  days = []
  for row in soup.find_all('div', {'class': 'climate-calendar__row'}):
    for index, cell in enumerate(row.find_all('div', {'class': 'climate-calendar-day'})):
      day_info = {}
      day = cell.find('div', {'class': 'climate-calendar-day__day'}).text
      # print(f'day: {day}')
      day_info['day'] = day

      temp_day = cell.find('div', {'class': 'temp climate-calendar-day__temp-day'}).text
      # print(f'temp day: {temp_day}')
      day_info['temp_day'] = temp_day

      temp_night = cell.find('div', {'class': 'temp climate-calendar-day__temp-night'}).text
      # print(f'temp night: {temp_night}')
      day_info['temp_night'] = temp_night

      # additional tab
      additional = cell.find('div', {'class': 'climate-calendar-day__detailed-container climate-calendar-day__detailed-container_day_{}'.format(index)})
      
      full_date = additional.find('h6', {'class': 'climate-calendar-day__detailed-day'}).text
      # print(f'full date: {full_date}')
      day_info['full_date'] = full_date

      feels_like = additional.find('div', {'class': 'climate-calendar-day__detailed-feels-like'}).text[-3:]
      # print(f'feels like: {feels_like}')
      day_info['feels_like'] = feels_like

      pressure = additional.find('td', {'class': 'climate-calendar-day__detailed-data-table-cell climate-calendar-day__detailed-data-table-cell_value_yes'}).text
      # print(f'pressure: {pressure}')
      day_info['pressure'] = pressure
      
      # table data
      table_data = additional.find('table', {'class': 'climate-calendar-day__detailed-data-table'}).text[14:].split('%')
      
      humidity = table_data[0] + '%'
      # print(f'humidity: {humidity}')
      day_info['humidity'] = humidity
      
      wind_info = table_data[1]
      # print(f'wind info: {wind_info}')
      day_info['wind_info'] = wind_info
      
      days.append(day_info)
      
  return days