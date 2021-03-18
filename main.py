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
    
    commits_desc = sort_commits(commits, reverse=True)
    commits = sort_commits(commits_desc[0:7])

    with open("commits.json", "w") as f:
        f.write(json.dumps(commits))

        
def sort_commits(commits, reverse=False):
    return sorted(commits, key=lambda c: c["date"], reverse=reverse)
        
    
if __name__ == "__main__":
    main()
