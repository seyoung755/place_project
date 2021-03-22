import requests

url = 'https://openapi.gg.go.kr/Genrestrtcate'
# result = requests.get(url)

service_key = "7f9474925e55434eb3ac376b10bf04bc"

params = {
    'pSize' : 10,
    'pIndex' : 1,
    'KEY' : service_key,
    'Type' : 'json',
    'SIGUN_CD' : 41110,
    'SIGUN_NM' : "수원시",
    # 'BSN_STATE_NM' : "영업"

}
res = requests.get(url=url, params=params)
# print(res.status_code, type(res.text), res.url)

from pprint import pprint
data = res.json()
id = 1

data = data['Genrestrtcate'][1]['row']
pprint(data)
# print(res.text)