from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

class Video(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    url: str = Field(..., description="Video URL (Google Drive/YouTube/Vimeo)")
    description: Optional[str] = Field(None, max_length=500)

class Profile(BaseModel):
    name: str
    bio: Optional[str] = None
    image: Optional[HttpUrl] = None
    location: Optional[str] = None
    website: Optional[HttpUrl] = None
    instagram: Optional[str] = None
    youtube: Optional[str] = None
    vimeo: Optional[str] = None
