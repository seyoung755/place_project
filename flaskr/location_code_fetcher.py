import math
NX = 149            ## X축 격자점 수
NY = 253            ## Y축 격자점 수

Re = 6371.00877     ##  지도반경
grid = 5.0          ##  격자간격 (km)
slat1 = 30.0        ##  표준위도 1
slat2 = 60.0        ##  표준위도 2
olon = 126.0        ##  기준점 경도
olat = 38.0         ##  기준점 위도
xo = 210 / grid     ##  기준점 X좌표
yo = 675 / grid     ##  기준점 Y좌표
first = 0

if first == 0:
    PI = math.asin(1.0) * 2.0
    DEGRAD = PI/ 180.0
    RADDEG = 180.0 / PI


    re = Re / grid
    slat1 = slat1 * DEGRAD
    slat2 = slat2 * DEGRAD
    olon = olon * DEGRAD
    olat = olat * DEGRAD

    sn = math.tan(PI * 0.25 + slat2 * 0.5) / math.tan(PI * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(PI * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(PI * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn)
    first = 1

def mapToGrid(lat, lon, code = 0 ):
    ra = math.tan(PI * 0.25 + lat * DEGRAD * 0.5)
    ra = re * sf / pow(ra, sn)
    theta = lon * DEGRAD - olon
    if theta > PI :
        theta -= 2.0 * PI
    if theta < -PI :
        theta += 2.0 * PI
    theta *= sn
    x = (ra * math.sin(theta)) + xo
    y = (ro - ra * math.cos(theta)) + yo
    x = int(x + 1.5)
    y = int(y + 1.5)
    return x, y

# print(mapToGrid(37.579871128849334, 126.98935225645432))
# print(mapToGrid(35.101148844565955, 129.02478725562108))
# print(mapToGrid(33.500946412305076, 126.54663058817043))



# import json
# import requests
# import math
#
# class location_code_fetcher:
#     def __init__(self):
#         # kakao = kakao_local.kakao_local_api()
#         # kakao.
#         # Url = "http://www.kma.go.kr/DFSROOT/POINT/DATA/"
#         # self.top = Url + "top.json.txt"
#         self.RE = 6371.00877 # 지구 반경(km)
#         self.GRID = 5.0 # 격자 간격(km)
#         self.SLAT1 = 30.0 # 투영 위도1(degree)
#         self.SLAT2 = 60.0 # 투영 위도2(degree)
#         self.OLON = 126.0 # 기준점 경도(degree)
#         self.OLAT = 38.0 # 기준점 위도(degree)
#         self.XO = 210 / self.GRID # 기준점 X좌표(GRID 좌표)
#         self.YO = 675 / self.GRID # 기준점 Y좌표(GRID 좌표)
#
#     def location_code_fetcher(self, lat: float, lon: float, mode='toXY',):
#         # rad <-> deg 변환을 위한 변수 설정
#         PI = math.asin(1.0) * 2.0
#         DEGRAD = PI / 180.0
#         RADDEG = 180.0 / PI
#
#         # DEG 값들을 RAD으로 변환
#         re = self.RE / self.GRID
#         slat1 = self.SLAT1 * DEGRAD
#         slat2 = self.SLAT2 * DEGRAD
#         olon = self.OLON * DEGRAD
#         olat = self.OLAT * DEGRAD
#
#         sn = math.tan(PI * 0.25 + slat2 * 0.5) / \
#              math.tan(PI * 0.25 + slat1 * 0.5)
#         sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
#         sf = math.tan(math.pi * 0.25 + slat1 * 0.5)
#         sf = math.pow(sf, sn) * math.cos(slat1) / sn
#         ro = math.tan(math.pi * 0.25 + olat * 0.5)
#         ro = re * sf / math.pow(ro, sn)
#         rs = {}
#         if mode == "toXY":
#             rs['lat'] = lat
#             rs['lng'] = lon
#             ra = math.tan(math.pi * 0.25 + lat * DEGRAD * 0.5)
#             re = re * sf / math.pow(ra, sn)
#             theta = lon * DEGRAD - olon
#             if theta > math.pi:
#                 theta -= 2.0 * math.pi
#             if theta < -math.pi:
#                 theta += 2.0 * math.pi
#             theta *= sn
#             rs['x'] = math.floor(ra * math.sin(theta) + self.XO + 0.5)
#             rs['y'] = math.floor(ro - ra * math.cos(theta) + self.YO + 0.5)
#
#         return rs
#
#
#
#
#         # res = requests.get(self.top)
#         # res.encoding=None
#         # documents = json.loads(res.text)
#         # json.dumps(documents, ensure_ascii=False).encode('utf8')
#         #
#         # for docu in documents:
#         #     if '서울' in docu['value']:
#         #         print(docu['code'])
#         #     elif '경기' in docu['value']:
#         #         print(docu['code'])
#         #
#         #     elif '충%남%' in docu['value']:
#         #         print(docu['code'])
#         # return documents[0]
#         return sn
#
#
# location = location_code_fetcher()
# print(location.location_code_fetcher(36.4, 127.1))