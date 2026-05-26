from fastapi import FastAPI , Query ,Path ,APIRouter
from typing import Optional , List
from uuid import UUID

app=FastAPI(
    title="My Api"
    
)
router=APIRouter()

@app.get("/home/{id}")
def home(id:int):
    return {
        "id":id
    }
    
@app.get("/home/{group_user}/user/{user_id}")
def h(group_user: str,user_id: int):
    return {
        "group":group_user,
        "user_id":user_id
    }
    
@app.get("/items")
def item(Name: str=Query(...,max_length=20),
        Password: str=Query(...,min_length=8),
        ids:List[int]=Query([]),
        skip: int=0,
        limit:Optional[int]=None):
    return {
        "Name":Name,
        "Password":Password,
        "skip":skip,
        "Limit":limit,
        "List":ids
    }  

@app.get("/{file_p}")
def read_file(file_path: str):
    return {
        "path":file_path
    }
    
from enum import Enum
class Color(str,Enum):
    red="red"
    green='green'
    
@app.get("/color/{color}")
def color_test(color:Color):
    return {
        "color":color
    }
    

@router.get("/{item_id}")
def itemm(item_id:int):
    return {
        "UUID":item_id
    }
app.include_router(
    router,
    prefix="/product"
)


