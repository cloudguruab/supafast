from typing import Optional
from fastapi import FastAPI

# database cursor to supabase
from data.database import SupabaseDB

app = FastAPI()


@app.get("/")
def index(): 
    return {"Hello": "World"}

@app.get("/getResult")
def query():
    data = SupabaseDB.supabase.table('credit_data').select('loan').limit(1).execute()
    return {"result": data}