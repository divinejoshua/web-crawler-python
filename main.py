import requests
from bs4 import BeautifulSoup

# Define starting URL and crawl depth
start_url = "https://pdfcharm.com/"
crawl_depth = 1

# Visited URLs to avoid duplicates
visited_urls = set()

# Queue for URLs to be crawled
queue = [start_url]

# Crawl until queue is empty or depth reached
while queue and crawl_depth > 0:
    url = queue.pop(0)
    if url not in visited_urls:
        # Download and parse the page
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract header title
        title = soup.find("title").text

        # Extract meta description
        meta_description = soup.find("meta", attrs={"name": "description"})
        if meta_description:
            meta_description = meta_description["content"]
        else:
            meta_description = None

        # Extract H1 elements (you can modify to select specific classes/ids)
        h1_elements = [h1.text for h1 in soup.find_all("h1")]

        # Extract links (fix the undefined variable issue)
        links = [a["href"] for a in soup.find_all("a")]

        # Print extracted data
        print(f"URL: {url}")
        print(f"Title: {title}")
        print(f"Meta Description: {meta_description}")
        print(f"H1 Elements: {h1_elements}")
        print(f"Links: {links}")

        # Add new links to queue (only if not already visited)
        queue.extend([link for link in links if link not in visited_urls])

        # Mark URL as visited
        visited_urls.add(url)

    crawl_depth -= 1

print("Crawling completed!")
