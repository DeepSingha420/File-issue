from fastapi import FastAPI, File, UploadFile
from typing import List, Annotated

app = FastAPI()

@app.post("/upload1/")
async def upload_file(file: UploadFile= File(...)):
    contents = await file.read()
    with open(f'sent/{file.filename}', 'wb') as file_handle:
        file_handle.write(contents)
    return {"message": "File uploaded successfully"}

@app.post("/upload2/")
async def upload_file(files: List[UploadFile] = File(...)):
    for f in files:
        contents = await f.read()
        with open(f'sent/{f.filename}', 'wb') as file_handle:
            file_handle.write(contents)
    return {"message": "Files uploaded successfully"}

@app.post("/upload3/")
async def upload_file(file: Annotated[List[UploadFile], File(...)]):
    for f in file:
        contents = await f.read()
        with open(f'sent/{f.filename}', 'wb') as file_handle:
            file_handle.write(contents)
    return {"message": "Files uploaded successfully"}