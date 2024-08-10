
import shutil
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from models.School import School, SchoolType,SchoolList
from pathlib import Path


from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def home():
    return {"message": "Welcome to CG schools API !"}


@app.get("/api/v1/schools", response_model=SchoolList)
async def get_schools():
    schools = {
        "schools": [
        {
            "name": "College-Lycee Anne Marie-Javouhey",
            "img": "/api/v1/images/Javouhey.jpg",
            "address": "P7CF+PV7, Av. d'Ornano, Brazzaville, Congo-Brazzaville", 
            "category": SchoolType.PRIVATE,
            "description": None,
            "city": "Brazzaville"
        },
        {
            "name": "Groupe Scolaire REMO",
            "img": "/api/v1/images/Remo.jpg",
            "address": "10-11 Avenue du Maréchal Lyautey, Quartier Clairon, Congo-Brazzaville", 
            "category": SchoolType.PRIVATE,
            "description": None,
            "city": "Brazzaville"
        }
    ]
    }

    return schools

# Needed endpoint to upload file to the server
@app.post("/api/v1/images/upload")
async def upload_file(file: UploadFile = File(...)):
    with open(f"images/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}


@app.get("/api/v1/images/{filename}", response_class=FileResponse)
async def download_file(filename: str):
    if not Path(f"images/{filename}").exists():
        raise HTTPException(status_code=404, detail=f"file {filename} not found.",)
    return FileResponse(path=f"images/{filename}")
# later endpoint
