import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient(f'mongodb connection url')

db = client['apidb']
collection = db['token']


class AuthDb:
    @staticmethod
    # Test 
    async def do_insert():
        document = {'token': 'aasfdgfahdsfsdf1q231'}
        result = await collection.insert_one(document)
        print('result %s' % repr(result.inserted_id))

    @staticmethod
    async def fetch_data(tok):
        result = await collection.find_one({"encoded": tok})
        return result

