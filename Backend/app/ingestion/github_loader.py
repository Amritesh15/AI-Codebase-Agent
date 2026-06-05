from git import Repo
import os

def clone_repo(repo_url: str):

    repo_name = repo_url.split("/")[-1].replace(".git", "")

    clone_path = f"repos/{repo_name}"

    if not os.path.exists("repos"):
        os.makedirs("repos")

    if not os.path.exists(clone_path):
        Repo.clone_from(repo_url, clone_path)

    return clone_path