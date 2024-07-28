import markdown
import os
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    with open(os.path.join(os.getcwd(), "README.md"), "r") as file:
        md_text = file.read()
    html = markdown.markdown(md_text)
    return HttpResponse(html)


def fetch_content(request):
    url = "http://noskill.pages.dev"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Обработка относительных URL для CSS, JS и изображений
        for tag in soup.find_all(["link", "script", "img"]):
            if tag.name == "link" and tag.get("href"):
                tag["href"] = requests.compat.urljoin(url, tag["href"])
            elif tag.name == "script" and tag.get("src"):
                tag["src"] = requests.compat.urljoin(url, tag["src"])
            elif tag.name == "img" and tag.get("src"):
                tag["src"] = requests.compat.urljoin(url, tag["src"])

        content = str(soup)

    except requests.exceptions.RequestException as e:
        content = f"An error occurred: {e}"

    return render(request, "display_content.html", {"content": content})
