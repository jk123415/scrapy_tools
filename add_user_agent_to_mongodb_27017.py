import pymongo
from datetime import datetime


if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['scrapy_crawl_data']
    col = db['user_agents']
    with open('user_agents', encoding='utf-8') as f:
        all_user_agents = f.read().splitlines()
        phone_index = all_user_agents.index('#phone')
        pc_user_agents = all_user_agents[0:phone_index]
        try:
            col.insert_one({
                '_id': 1,
                'pc_user_agents': pc_user_agents,
                'time': datetime.now()
            })
            phone_user_agents = all_user_agents[phone_index + 1:]
            col.insert_one({
                '_id': 2,
                'phone_user_agents': phone_user_agents,
                'time': datetime.now()
            })
            all_user_agents.remove('#phone')
            all_user_agents = all_user_agents
            col.insert_one({
                '_id': 3,
                'all_user_agents': all_user_agents,
                'time': datetime.now()
            })
        except Exception as e:
            print(e)
        finally:
            print([x for x in col.find({'_id':1})])
            client.close()
