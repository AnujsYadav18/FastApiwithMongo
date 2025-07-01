from fastapi import FastAPI,APIRouter,HTTPException
from config import collection
from database import schemas,models
from bson import ObjectId

 
app = FastAPI()

router = APIRouter()
#Read
@router.get("/")
async def get_all_employee():
    data = collection.find()
    return schemas.get_all_data(data)
#Create
@router.post("/")
async def get_one_employee(new_emp:models.Employee):
    try:

        resp = collection.insert_one(dict(new_emp))
        return {"status_code":200,"id":str(resp.inserted_id)}
    
    except Exception as e:
        return HTTPException(status_code=500,detail=f"Some Error Occured{e}")
#Update
@router.put("/{emp_id}")
async def update_employee(emp_id:str,updated_emp:models.Employee):
    try:
        #check the id in collection or not
        id = ObjectId(emp_id)
        exist_doc = collection.find_one({"_id":id})
        if not exist_doc:
            return HTTPException(status_code=404,detail=f"Employee not found")
        collection.update_one({"_id":id},{"$set":dict(updated_emp)})
        return  {"status_code":200,"message":"Updated Successfully!!"}
    except Exception as e:
        return HTTPException(status_code=500,detail=f"Some Error Occured{e}")
    
#Delete
@router.delete("/{emp_id}")
async def delete_employee(emp_id:str):
    try:
        #check the id in collection or not
        id = ObjectId(emp_id)
        exist_doc = collection.find_one({"_id":id})
        if not exist_doc:
            return HTTPException(status_code=404,detail=f"Employee not found")
        collection.delete_one({"_id":id})
        return  {"status_code":200,"message":"Deleted Successfully!!"}
    except Exception as e:
        return HTTPException(status_code=500,detail=f"Some Error Occured{e}")
    
app.include_router(router)