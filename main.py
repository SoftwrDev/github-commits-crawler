import json

from bs4 import BeautifulSoup
import requests


def main():
    response = requests.get("https://www.github.com/SoftwrDev")
    soup = BeautifulSoup(response.text, "html.parser")
    g = soup.find_all("g")
    commits = [{"commits": rect.get("data-count"), "date": rect.get("data-date")} for rect in g[52].find_all("rect")]
    commits = [*commits, {"commits": rect.get("data-count"), "date": rect.get("data-date")} for rect in g[53].find_all("rect")]    
    commits = sort_commits(sort_commits(commits, reverse=True)[0:7])

    with open("commits.json", "w") as f:
        f.write(json.dumps(commits))

        
def sort_commits(commits, reverse=False):
    return sorted(commits, key=lambda c: c["date"], reverse=reverse)
        
    
if __name__ == "__main__":
    main()
