# main.py
from fastapi import FastAPI, File, UploadFile
import shutil
import os

app = FastAPI()

# Create upload folder if not exists
UPLOAD_FOLDER = "uploaded_images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    
    # Save the uploaded file
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # ✅ Later here you can call your AI/ML model or do processing
    
    return {"status": "success", "filename": file.filename}
