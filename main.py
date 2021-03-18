import json

from bs4 import BeautifulSoup
import requests


def main():
    response = requests.get("https://www.github.com/SoftwrDev")
    soup = BeautifulSoup(response.text, "html.parser")
    g = soup.find_all("g")
    rect1 = g[52]
    rect2 = g[53]
    commits = []

    for rect in rect1.find_all("rect"):
        commits.append({"commits": rect.get("data-count"), "date": rect.get("data-date")})

    for rect in rect2.find_all("rect"):
        commits.append({"commits": rect.get("data-count"), "date": rect.get("data-date")})
    
    commits_desc = sorted(commits, key=lambda c: c["date"], reverse=True)
    commits = sorted(commits_desc[0:7], key=lambda c: c["date"])

    with open("commits.json", "w") as f:
        f.write(json.dumps(commits))

if __name__ == "__main__":
    main()