# supabase client
from config import Config
from .database import SupabaseDB

# fast api wrappers for redis and methods
# for res/rep lifecycles. 
from fastapi import Request, Response
from fastapi_redis_cache import FastApiRedisCache

class SupafastCache(FastApiRedisCache):
    """
    Class instance for redis environment
    
    :rtype: None
    :constructor: cache instance from fastapi wrapper. 
    """
    
    def __init__(self): 
        self.redis_cache = self.init(
            host_url=Config.REDIS_URL,
            prefix="supafast-cache",
            response_header="X-Supafast-Cache",
            ignore_arg_types=[Request, Response, SupabaseDB.supabase]
        )