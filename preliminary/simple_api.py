"""Provides a simple API for your basic OCR client

Drive the API to complete "interprocess communication"

Requirements
"""
from email.policy import default

from fastapi import FastAPI, HTTPException
from fastapi import Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from pathlib import Path
from library_basics import CodingVideo


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


# We'll create a lightweight "database" for our videos
# You can add uploads later (not required for assessment)
# For now, we will just hardcode are samples
VIDEOS: dict[str, Path] = {
    "demo": Path("resources/oop.mp4")
}

class VideoMetaData(BaseModel):
    fps: float
    frame_count: int
    duration_seconds: float
    #pydantic treat name with "_" as private and leave them out of the response
    #the field is called "links" abd show as "_links" in json
    links: dict | None = Field(default=None, serialization_alias="_links")

@app.get("/video")
def list_videos():
    """List all available videos with HATEOAS-style links."""
    return {
        "count": len(VIDEOS),
        "videos": [
            {
                "id": vid,
                "path": str(path), # Not standard for debug only
                "_links": {
                    "self": f"/video/{vid}",
                    "frame_example": f"/video/{vid}/frame/1.0"
                }
            }
            for vid, path in VIDEOS.items()
        ]
    }

def _open_vid_or_404(vid: str) -> CodingVideo:
    path = VIDEOS.get(vid)
    if not path or not path.is_file():
        raise HTTPException(status_code=404, detail="Video not found")
    try:
        return CodingVideo(path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Could not open video {e}")

def _meta(video: CodingVideo) -> VideoMetaData:
    return VideoMetaData(
            fps=video.fps,
            frame_count=video.frame_count,
            duration_seconds=video.duration
    )


@app.get("/video/{vid}", response_model=VideoMetaData)
def video(vid: str):
    video = _open_vid_or_404(vid)
    try:
            meta = _meta(video)
            meta.links = {
                "self": f"/video/{vid}",
                "frames": f"/video/{vid}/frame/{{seconds}}"
            }
            return meta
    finally:
        video.capture.release()


@app.get("/video/{vid}/frame/{t}", response_class=Response)
def video_frame(vid: str, t: float):
    #open video before "try", if it's not found, 404 return
    video = _open_vid_or_404(vid)
    try:
        return Response(content=video.get_image_as_bytes(t), media_type="image/png")
    finally:
      video.capture.release()

@app.get("/video/{vid}/frame/{t}/ocr")
def video_frame_ocr(vid: str, t: float):
    """return the text shown in the video ar time t seconds"""
    video = _open_vid_or_404(vid)
    try:
        #read text in the frame with Tesseract
        text = video.get_text_at_time(t)
        return {"text": text}
    finally:
        #close the video file when finished
        video.capture.release()

@app.get("/video/{vid}/stream")
def video_stream(vid: str):
    """send the whole video file so frontend can play"""
    path = VIDEOS.get(vid)
    if not path or not path.is_file():
        raise HTTPException(status_code=404, detail="Video not found")
    return FileResponse(path, media_type="video/mp4")