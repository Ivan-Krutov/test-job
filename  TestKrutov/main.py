import uvicorn
from pathlib import Path
from fastapi import FastAPI
from file_parse.api import fp_router

ROOT_PATH = Path(__file__).parent

app = FastAPI(
    title="Test",
    default_language="en",
    debug=True
)


app.include_router(fp_router, prefix="/file_parse", tags=["parse"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1701, log_level="debug", reload=True)