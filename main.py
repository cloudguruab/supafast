# factory method for intializing your fast api app.
from fastapi import FastAPI

# database cursor to supabase
from data.database import SupabaseDB

# redis related imports
from data.rcache import SupafastCache
from fastapi_redis_cache import cache

# application factory
app = FastAPI(title="Supafast Tutorial", debug=True)


@app.on_event("startup")
def onStart():
    """
    Helper function for on event handler in FastAPI. The event
    passed in as a param checks for the startup event for the 
    current application. This then triggers our connection to our
    redis cache via <SupafastCache> instance.
    
    :rtype: Cache instance for application.     
    """
    
    server_start = SupafastCache()
    return {"result": server_start}


@app.get("/")
def index(): 
    """
    Initial view or endpoint when visiting localhost:8000/
    
    :rtype: Welcome and instruction for walkthrough via readme or localhost:8000/docs
    """
    
    return {"👋 Hello": "Please refer to the readme\
 documentation for more or visit https://localhost/8000/docs"}


@app.get("/getResult")
def query():
    """
    Endpoing for testing data to be pulled from your supabase instance.
    
    :rtype: 1st row of consumer credit data. 
    :endpoint: {
        "data": [
            {
                "clientid": 1,
                "income": 66155.9251,
                "age": 59,
                "loan": 8106.532131,
                "default": "0"
            }
        ],
    }
    """
    
    data = SupabaseDB.supabase.table('credit_data').select('*').limit(1).execute()
    return data


@app.get("/cachedResults")
@cache(expire=604800)
async def get_defaults():
    """
    asynchronous function call for grabbing load default specific data
    by the first 100 rows of data from your supabase instance.
    
    :rtype: Loan defaults for individuals by a certain age or older.
    :endpoint: {
        
    }
    """
    
    lst = list
    count = 0
    data = SupabaseDB.supabase.table('credit_data').select('*').limit(100).execute()
    
    for i in data:
        if count >= len(i[1]):
            break
        
        count += 1
        lst.append(i[1][count]['age'])

    return lst
    # return {"message": f'Currently there are {len(arr)} adults 45 older with credit defaults out of 100 individuals.'}