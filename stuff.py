import requests as r
import os
import sqlite3
from datetime import datetime
from jinja2 import Template

def git_search(query, language='python'):
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': query,
        'l': language
    }
    res = r.get(url, params=params).json()
    message = ''
    for repo in res['items'][:5]:
        message += f'<a href="{repo["svn_url"]}">{repo["name"]}</a>\n'
    return message


def send_image():
    content = r.get('https://random.dog/woof.json').json()
    img_url = content['url']
    return img_url


def get_forecast(lat, lon):
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {
        'lat': lat,
        'lon': lon,
        'appid': os.environ.get('WEATHER_APP'),
        'units': 'metric',
        'lang': 'ru',
    }
    resp = r.get(url, params=params).json()
    text = '<strong>{}</strong> <i>{}</i>: \n{}ºC, {}\n\n'
    res = ''

    for data in resp['list']:
        date = datetime.fromtimestamp(data['dt'])  # превращаем timestamp в нормальную дату
        date_res = date.strftime('%d.%m.%Y')  # формат отображения даты в виде дд.мм.гггг
        temp = data['main']['temp']
        weather = data['weather'][0]['description']

        if date.hour == 15:
            daytime = 'днём'
            res += text.format(date_res, daytime, temp, weather)
        elif date.hour == 21:
            daytime = 'вечером'
            res += text.format(date_res, daytime, temp, weather)
    return resp


def connect_db():
    con = sqlite3.connect('bot_db.sqlite')
    return con


def add_user(f_name, l_name, tg_id, phone, connection):
    sql = f'''INSERT INTO users (first_name, last_name, tg_id, phone_number)
              VALUES ("{f_name}", "{l_name}", "{tg_id}", "{phone}") '''
    try:
        curs = connection.cursor()  # пытаемся получить курсор для БД
        curs.execute(sql)
        return 0
    except:
        return None

def make_template(filename):
        with open(filename, 'r') as f:
            text = f.read()
        template = Template(text)
        return template
