#pip install pymongo
from pymongo import MongoClient
from pymongo.cursor import CursorType

host = "192.168.0.14"
port = "27017"
conn = MongoClient(host, int(port))
db = conn.get_database('neon')

# 아래 조회 방법은 예시입니다.
"""
match = 줄리안이 jul_date고 년도가 x년부터 y년까지
group = 그중에서 그룹을 묶는데 GEOID와 TYPE이 같고 그걸 avg 해서 내어 달라

result = coll.aggregate([
        {'$match':
             {'JULIAN': int(jul_date), 'YEAR': {'$gte': int(db_year)-10 , '$lte': int(db_year)-1}}
         },
        {'$group':
             {'_id': {'geoid': '$GEOID', 'type': '$TYPE'},
              'avg': {'$avg': '$MEAN'}}
         },
        {'$sort': {'_id': 1}}
    ])
    
    
#추출 방법

    for i in result:
        print('result1',i)
        kk += 1
        if i['_id']['type'] == 'evi':
            geoid_tmp_dict['evi'] = i['avg']
            
            
"""

# 예시 2번
"""
줄리안데이가 x고 년도가 y인데 정렬 기준은 GEOID 순으로
result2 = coll.find({'JULIAN': int(jul_date), 'YEAR': int(db_year)}).sort("GEOID")

데이터 프레인으로 추출
df_result2 = pd.DataFrame(list(result2))
"""