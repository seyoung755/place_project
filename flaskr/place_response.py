from kakao_local import kakao_local_api
from pprint import pprint

import heapq



# Front-end로부터 현재 x, y값 전달받음 -> 해당 지역의 날씨정보를 호출
# 날씨 정보에 맞는 키워드들을 넣어서 검색 -> 사용자 디스플레이 내에 있는 장소를 거리별로 전달
def place_response(x, y, radius):
    request = kakao_local_api()
    # weather = weather.api(x,y)
    # keyword = get_keywords(weather)

    keyword = '라면'

    result = request.search_keyword(keyword, x=x, y=y, radius=radius, page=2, size=10)
    result = result['documents']
    result = sorted(result, key=lambda x: int(x['distance']))
    # pprint(result)


    return result
print("=========result==========")
pprint(place_response(127, 37.5, 2000))



# print(request)
