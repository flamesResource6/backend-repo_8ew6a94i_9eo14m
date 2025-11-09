from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional
from database import create_document, get_documents

app = FastAPI(title="Video Editor Portfolio API")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VideoIn(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    url: str = Field(..., description="Video URL (Google Drive/YouTube/Vimeo)")
    description: Optional[str] = Field(None, max_length=500)


class ProfileIn(BaseModel):
    name: str
    bio: Optional[str] = None
    image: Optional[HttpUrl] = None
    location: Optional[str] = None
    website: Optional[HttpUrl] = None
    instagram: Optional[str] = None
    youtube: Optional[str] = None
    vimeo: Optional[str] = None


@app.get("/test")
async def test():
    return {"status": "ok"}


@app.get("/videos", response_model=List[dict])
async def list_videos():
    docs = await get_documents("video", {}, limit=100)
    return docs


@app.post("/videos", status_code=201)
async def create_video(video: VideoIn):
    data = video.dict()
    doc = await create_document("video", data)
    return doc


@app.get("/profile")
async def get_profile():
    docs = await get_documents("profile", {}, limit=1)
    if not docs:
        return {}
    return docs[0]


@app.post("/profile", status_code=201)
async def set_profile(profile: ProfileIn):
    doc = await create_document("profile", profile.dict())
    return doc
