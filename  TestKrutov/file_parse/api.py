import os
import shutil
import tempfile
import aiofiles
from typing import List
from fastapi import APIRouter, UploadFile, HTTPException
from file_parse.process_file.file_parser import FileParser

ALLOWED_EXTENSIONS = ['.json', '.xml']

SUMMARY = ""

POST_DESCRIPTION = ("".format(ALLOWED_EXTENSIONS))

fp_router = APIRouter()


async def process_file(file_path: str):
    file_reader = FileParser(file_path, supported_file_types=ALLOWED_EXTENSIONS)
    text = await file_reader.read_file()
    return text


@fp_router.post("/file_parser/", summary=SUMMARY, description=POST_DESCRIPTION, )
async def file_parser(files: List[UploadFile]):
    success_files = []
    failed_files = []
    tmp_dir = tempfile.mkdtemp()
    try:
        for uploaded_file in files:
            file_extension = os.path.splitext(uploaded_file.filename)[1]
            if file_extension not in ALLOWED_EXTENSIONS:
                failed_files.append(
                    {"code": 500, "file_name": uploaded_file.filename, "error": f"{file_extension}"})
                continue

            tmp_file_path = os.path.join(tmp_dir, uploaded_file.filename)
            data = await uploaded_file.read()
            async with aiofiles.open(tmp_file_path, 'wb') as out_file:
                await out_file.write(data)

            try:
                data = await process_file(tmp_file_path)
                data["file"] = uploaded_file.filename
                success_files.append({"code": 200, "data": data})
            except HTTPException as e:
                failed_files.append({"code": 500, "file_name": uploaded_file.filename, "error": e.detail})
            os.remove(tmp_file_path)
    except Exception as e:
        shutil.rmtree(tmp_dir)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir)

    return {"status_code": 200, "success_files": success_files, "failed_files": failed_files}
