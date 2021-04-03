import requests
import json
import datetime

def today_weather(nx, ny):
    vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?"

    service_key = "OkRN8rYsASq%2BwUfM1uAN9ivXmEoBhbGwJo21q10NG9m%2BXOKjjuiUiNfgzA0ww72nACoKpXdjHZSMLKmEqLWEzg%3D%3D"

    today = datetime.datetime.today()

    base_date = today.strftime("%Y%m%d") # "기준 날짜 ex.20151201
    # print(type(base_date))
    base_time = "0800" # 날씨 값 ex.0600는 6시를 말함.


    payload = "serviceKey=" + service_key + "&dataType=json&base_date=" + base_date + "&base_time=" + base_time + "&nx=" + nx + "&ny=" + ny

    # 값 요청
    res = requests.get(vilage_weather_url + payload)
    res.json()
    try:
        items = res.json().get('response').get('body').get('items').get('item')
    except Exception as e:
        return "맑음"


    data = dict()
    data['date'] = base_date

    weather_data = dict()
    for item in items:

        # weather_state 기상상태 : 기상상태 코드를 '비/눈/소나기/없음' 중 1개로 출력

        if item['category'] == 'PTY':

            weather_code = item['fcstValue']

            if weather_code == '1':
                weather_state = '비'
            elif weather_code == '2':
                weather_state = '눈'
            elif weather_code == '3':
                weather_state = '눈'
            elif weather_code == '4':
                weather_state = '소나기'
            elif weather_code == '5':
                weather_state = '비'
            elif weather_code == '6':
                weather_state = '비'
            elif weather_code == '7':
                weather_state = '눈'
            else:
                weather_state = '없음'

        # weather_rainny 장마 구분 : weather_state == '비' 경우 강수량에 따라 장마로 구분

        if item['category'] == 'R06':

            weather_rain = item['fcstValue']

            if float(weather_rain) > 20:
                weather_rainny = '장마'
            else:
                weather_rainny = '비'

        # weather_cloud 맑음/흐림 구분  : weather_state == '없음' 일 경우 '맑음' 혹은 '흐림'으로 나눔

        if item['category'] == 'SKY':
            weather_sky = item['fcstValue']

            if weather_sky == '1':
                weather_cloud = '맑음'
            elif weather_sky == '3':
                weather_cloud = '흐림'
            elif weather_sky == '4':
                weather_cloud = '흐림'

        # weather_tmp 기온 : weather_cloud == '맑음'일 경우 기온으로 '추움' '맑음' '더움' 구분
        if item['category'] == 'T3H':
            weather_tmp = item['fcstValue']

            if int(weather_tmp) < 10:
                weather_today = '추움'
            elif int(weather_tmp) > 25:
                weather_today = '더움'
            else:
                weather_today = '맑음'

    weather_data['state'] = weather_state
    weather_data['cloud'] = weather_cloud
    weather_data['rainny'] = weather_rainny
    weather_data['today'] = weather_today

    # print(weather_data)

    # 키'state'값이 '눈/소나기/비/없음' 로 나뉠때
    # 키 'state' 값이 '비' 경우 키 'rainny'값에 따라 장마와 비로 구분
    # 키'state'값이 '없음' 일 경우 키'cloud'의 값 중 '맑음' 혹은 '흐림'으로 나눔
    # 키'cloud'의 값이 '맑음'일 경우 키'today'값으로 '추움' '맑음' '더움' 구분

    if weather_data['state'] == '눈':
        result = '눈'

    if weather_data['state'] == '소나기':
        result = '소나기'

    if weather_data['state'] == '비' and weather_data['rainny'] == '장마':
        result = '장마'
    else:
        result = '비'

    if weather_data['state'] == '없음' and weather_data['cloud'] == '흐림':
        result = '흐림'
    elif weather_data['state'] == '없음' and weather_data['cloud'] == '맑음':
        result = '맑음'

    if result == '맑음':
        if weather_data['today'] == '추움':
            result = '추움'
        elif weather_data['today'] == '더움':
            result = '더움'
        else:
            result = '맑음'

    return result


# print(today_weather("60", "80"))