from fastapi_redis_cache import FastApiRedisCache
from config import Config
from fastapi import Request, Response
from .database import SupabaseDB


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