from pydantic import BaseModel, Field
from pprint import pprint
import json
from enum import Enum

class User(BaseModel):
    id: str = Field(...,min_length=14,max_length=14)
    name: str = Field(...,min_length=3, max_length=50)
    age: int = Field(...,gt=12,lt=90)

json_data = {
    "id": "abc12345abcabc",
    "name": "ahmed",
    "age": 44
}

class Option(Enum):
    DETAILED = "detailed"
    SIMPLE = "simple"
    WITH_EXAMPLE = "withexample"


if __name__ == "__main__":
    user = User(**json_data)
    print(user)
    print(user.model_dump_json())
    print(json.dumps(json.loads(user.model_dump_json()), indent=4))
