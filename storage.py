import redis
import json

REDIS_KEY = "spacex:launches"
REDIS_HOST = "localhost"
REDIS_PASSWORD = ""
REDIS_PORT = 6379
REDIS_DB = 0

def get_redis_connection():
    return redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASSWORD
    )

def store_in_redis(data, key=REDIS_KEY):
    r = get_redis_connection()
    r.set(key, json.dumps(data))
    print(f"✅ {len(data)} lancements enregistrés dans Redis sous la clé '{key}'.")

def retrieve_from_redis(key=REDIS_KEY):
    r = get_redis_connection()
    raw_data = r.get(key)
    if raw_data:
        data = json.loads(raw_data)
        print(f"📥 {len(data)} lancements récupérés depuis Redis.")
        return data
    else:
        print("❌ Aucune donnée trouvée dans Redis.")
        return []
