from fastapi import FastAPI, UploadFile, File
from pipeline import reconstruct_artifact
import io
from starlette.responses import StreamingResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI artifact reconstruction service is running!"}

@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    content = await file.read()
    processed_img = reconstruct_artifact(content)

    img_byte_arr = io.BytesIO()
    processed_img.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)

    return StreamingResponse(img_byte_arr, media_type="image/png")