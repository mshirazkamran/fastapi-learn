from turtle import title
from urllib.parse import uses_fragment
from fastapi import Body, FastAPI, Path, Query
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


#3. You can use Path for the path params just as you use Query for query params

@app.get("/users/check/{id}")
async def user_check_id(id: Annotated[int, Path(title="This is a an id", gt=10)]):
    pass


# You can add multiple body parameters to your path operation function,
# even though a request can only have a single body.

# But FastAPI will handle it, give you the correct data in your function, 
# and validate and document the correct schema in the path operation.

# You can also declare singular values to be received as part of the body.
# Ex:
@app.post("/endpoint/user")
async def endpoint(user: User, importance: Annotated[int, Body()]):
    pass

# And you can instruct FastAPI to embed the body in a key even when there is only a single parameter declared.
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[User, Body(embed=True)]):
    pass


