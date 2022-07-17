import requests as visit
from .translate import translate
def city(city):
    print('\033[92m'+visit.get('http://api.klizi.cn/API/other/weather_1.php?&msg={}'.format(city)).text)