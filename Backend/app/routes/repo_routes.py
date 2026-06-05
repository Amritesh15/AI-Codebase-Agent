from fastapi import APIRouter
from pydantic import BaseModel

from app.ingestion.github_loader import clone_repo

router = APIRouter()

class RepoRequest(BaseModel):
    repo_url: str

@router.post("/upload-repo")
def upload_repo(request: RepoRequest):

    repo_path = clone_repo(request.repo_url)

    return {
        "message": "Repository cloned successfully",
        "path": repo_path
    }