import os

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()


def get_client() -> Anthropic:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("Set ANTHROPIC_API_KEY in your .env file")
    return Anthropic(api_key=api_key)


MODEL = "claude-sonnet-5"
