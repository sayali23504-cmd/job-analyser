import re
import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url: str) -> str:
    response = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text("\n")
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()
