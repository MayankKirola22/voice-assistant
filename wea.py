import requests
from pprint import pprint
def whe(query='bhimtal'):

    try:
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+query+'&APPID=c062c4bb0764f1e1e05bc9461742c819&units=metric');
        result=res.json()
        temp=str(result['main']['temp'])
        wind=str(result['wind']['speed'])
        desc=result['weather'][0]['description']
        n='right now the current temperature in '+query+' is '+temp+' degree celcius with '+desc+' and wind speed is '+wind+' meter per second'
    except:
        n='city not found'
    return n
