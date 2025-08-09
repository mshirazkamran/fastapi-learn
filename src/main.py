from fastapi import FastAPI

import urllib.request
import json
import time

import psutil
import os

from models import User
from models import Option

users :list[User] = []



def get_current_memory_usage() -> str:
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Convert to MB

print(f"Current memory usage: {get_current_memory_usage():.2f} MB")

app = FastAPI(title="test-app")

@app.get("/")
async def root():
    return {
        "name": "shiraz",
        "age": 18
    }

@app.post("/add/user")
async def add_user(user: User):
    users.append(user)
    print(get_current_memory_usage())
    return {
        "success": "ok"
    }


names = ["ali", "abubakar", "umer", "ahmad"]

@app.get("/names/{id}")
async def getName(id: int):
    return names[0:id]

@app.get("/joke")
async def getJoke():
    start = time.time() * 100

    # some heavy task

    end  = time.time() * 100

    duration = end - start
    print(f"Time taken: {duration:.8f} seconds")

    return "Read coulndt react in time"   


# This is how you input predefined values else return a 422 error
@app.get("/help/{option}")
async def enum_explanation(option: Option):
    # this is the explanation of enum 
    if option is Option.DETAILED:
        print("Detailed was mentioned")
        return {
            "success": "ok",
            "message": Option.DETAILED
        }
    
    if option == Option.SIMPLE:
        print("Simple was mentioned")
        return {
            "success": "ok",
            "message": Option.SIMPLE
        }
    
    if option is Option.WITH_EXAMPLE:
        print("Simple was mentioned")
        return {
            "success": "ok",
            "message": Option.WITH_EXAMPLE
        }
    

# Paths
    # you can also see the docs to process paths (OPENAPI specs dont have this option but fastapi does have it)



# if __name__ == "__main__":


# Query params
    # When you declare other function parameters that are not part of the path parameters,
    # they are automatically interpreted as "query" parameters.
    # if query param is not set as = None, then it is required

@app.get("/query/{id}")
async def query_params(description: bool | None, id: int = 3, name: str | None = None):

    # url will be like
    # YOU NEED TO ENCODE THE STRING THAT HAS SPACES THEN SEND IT TO BACKEND
    # localhost:8000/query/1?description=I%20AM%20SHIRAZ&short=true

    item = {
        'id': id,
        'tag': 'lamp',
        'username': name if name else 'default'
    }

    if description:
        item.update({
            'description': 'this is a nice lamp of price 4000pkr'
        })
    
    return item


# Using enum with queryparams
@app.get("/query/data/2")
async def enum_query(option: Option):
    return {
        'success': 'ok',
        'option': option
    }

