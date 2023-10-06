from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Profile(BaseModel):
    name: str
    about: str



@app.get("/")
async def root():
    return {"message": "This is the backend to the Lovoofarmer Extension"}


@app.put("v1/profile/{profile_id}")
async def profile(profile_id: str, profile: Profile):
    print(profile_id)
    print(profile)
    return 200