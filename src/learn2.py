from urllib.parse import uses_fragment
from fastapi import FastAPI, Query
from pydantic import AfterValidator

from models import User, Option

from typing import Annotated


app: FastAPI = FastAPI(title="learning-app")


# 1 String validation and Query params validation
    # 1. you can and should perform qeury param validations
    # 2. they throw the nice error that fastapi uses
    # 3.1 You should use "param: Annotated[int, Query(le=30)] = 3" in newer codespaces >0.95.0
    # 3.2 adjust accordingly if you want default or req param
    # 4 use "param: int = Query(default=4, ge=50)" in older codebases, fastapi < 0.95.0
    # 5 use @AfterValidator for custom validations

ids: list[int] = [x for x in range(1,31)]

# for custom validation
# refer to https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#custom-validation
def check_id(id: int):
    if len(str(id)) <= 2:
            raise ValueError("Error in id length") 
    return id

@app.get("/users/check")
async def check_user(id: Annotated[int | None, Query(ge=1,le=30), AfterValidator(check_id)] = None):
    return {
        'id': id if id else 99,
        'content': f"{id if id else 99} is queried" 
    }



#2. you can also input list (multiple values) in query param
    # refer to https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-parameter-list-multiple-values


