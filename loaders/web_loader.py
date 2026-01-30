import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_internal_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        full_url = urljoin(base_url, href)

        if urlparse(full_url).netloc == urlparse(base_url).netloc:
            links.add(full_url)

    return links


def crawl_website(start_url, max_depth=1, max_pages=5):
    visited = set()
    documents = []

    def crawl(url, depth):
        if depth > max_depth or url in visited or len(visited) >= max_pages:
            return

        visited.add(url)

        try:
            headers = {
               "User-Agent": "Trapti (Educational Project; contact: traptijindal5678@gmail.com)"
                  }

            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            # Remove scripts, styles, nav, footer
            for tag in soup(["script", "style", "nav", "footer", "header"]):
               tag.decompose()

            main = soup.find("div", {"id": "mw-content-text"})
            if main:
                text = main.get_text(separator=" ", strip=True)
            else:
                text = soup.get_text(separator=" ", strip=True)
            
            if "wikipedia.org" in url:
               text = text[:8000]

            documents.append({
                "source": url,
                "content": text
            })

            for link in extract_internal_links(response.text, url):
                crawl(link, depth + 1)

        except Exception:
            pass

    crawl(start_url, 0)
    return documents
