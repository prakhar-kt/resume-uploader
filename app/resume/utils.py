import os
from uuid import uuid4
from fastapi import HTTPException, UploadFile

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_uploaded_file(upload_file: UploadFile, sub_dir: str) -> str:
    original_name: str = upload_file.filename or ""
    if original_name == "":
        raise HTTPException(status_code=400, detail="No File to upload")
    ext = os.path.splitext(original_name)[-1]
    filename = f"{uuid4().hex}{ext}"
    dir_path = os.path.join(UPLOAD_DIR, sub_dir)
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, filename)
    with open(file_path, "wb") as f:
        content = await upload_file.read()
        f.write(content)

    return file_path
