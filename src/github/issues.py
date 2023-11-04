from __future__ import annotations

import os

import requests
from dotenv import find_dotenv
from dotenv import load_dotenv

from src.utils import config

# Load Env Vars
_ = load_dotenv(find_dotenv())

# Constants
API_BASE_URL = "https://api.github.com"
AUTH_TOKEN = os.environ.get("GITHUB_AUTH_TOKEN")
OWNER = config.config()["github"]["owner"]
REPO = config.config()["github"]["repo"]


def get_issues(owner: str = OWNER, repo: str = REPO) -> dict:
    """_summary_

    Args:
        owner (str, optional): _description_. Defaults to "".
        repo (str, optional): _description_. Defaults to "".

    Returns:
        dict: _description_
    """

    request = requests.get(
        url=f"{API_BASE_URL}/{owner}/{repo}/issues",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}", "Accept": "application/vnd.github+json"},
    )
    return request.json()
