from fastapi import FastAPI, UploadFile, File
import shutil
import pandas as pd
from src.scan import init, process
import os

app = FastAPI(
    docs_url = "/api/v1/docs",
    redoc_url="/api/v1/redocs",
    title="DF Scan API",
    version="0.1.1",
    openapi_url="/api/v1/openapi.json"
)

items = {}

@app.on_event("startup")
async def startup_event():
    init()
    return print("Application started")

@app.post("/video/scan")

async def scan(video: UploadFile = File(...)):
    video_name = f'{video.filename}'
    report_name = 'result.csv'
    with open(video_name,"wb+") as buffer:
        shutil.copyfileobj(video.file, buffer)
    
    prediction = process(video_name)
    
    with open(report_name,'w') as f:
        print('filename, label', file=f)
        print('%s,%.4f'%(video_name, prediction), file=f)
    
    items['video_name'] = video_name
    items['report_name'] = report_name
    return {"file_name": video_name}

@app.get("/video/report")

async def parse_and_delete():
    df =  pd.read_csv(items["report_name"])
    result = df.to_dict('records')
    os.remove("./" + items['video_name'])
    os.remove("./" + items['report_name'])
    return result

@app.on_event("shutdown")
async def shutdown_event():
    return print("Application shutted down")
