from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
import uuid
import cv2

app = FastAPI()

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    # Check file type
    if file.content_type not in ["image/png", "image/jpeg", "image/jpg"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Create directory if it doesn't exist
    os.makedirs("uploaded_images", exist_ok=True)

    # Generate UUID filename
    ext = os.path.splitext(file.filename)[1]   # Keep original extension
    unique_filename = f"{uuid.uuid4()}{ext}"   # Example: 4f3c9e6d-3f2f-4bcf-8f91.jpg
    save_path = os.path.join("uploaded_images", unique_filename)

    # Save file
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Analyze with OpenCV (optional)
    image = cv2.imread(save_path)
    if image is None:
        raise HTTPException(status_code=400, detail="Invalid image data")

    height, width, channels = image.shape

    return {
        "filename": unique_filename,
        "width": width,
        "height": height,
        "channels": channels,
        "message": "Image uploaded and analyzed successfully"
    }

