import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/transcript")
def proxy_to_local(video_id: str):
    try:
        # Route the request to your ngrok proxy
        proxy_url = f"https://cd23-185-187-168-171.ngrok-free.app/transcript?video_id={video_id}"
        response = requests.get(proxy_url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Proxy failed: {str(e)}")
