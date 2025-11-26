import requests
from linkedin_praser import LinkedInParser


def fetch_page(url):
    print("Fetching:",url)
    r = requests.get(url)
    r.raise_for_status()
    return r.text



if __name__ == "__main__":
    url = "https://www.linkedin.com/jobs/view/4338837519"
    html = fetch_page(url)

    parser = LinkedInParser(html)
    print("Title:   ", parser.title())
    print("Company: ", parser.company())
    print("Location:", parser.location())
    desc = parser.description()
    print("Description (first 800 chars):\n", (desc[:800] + "...") if desc else "No description found")
