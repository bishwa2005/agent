import requests

def search_repos(query: str):
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
    response = requests.get(url, timeout=10)
    items = response.json().get("items", [])

    results = []
    for repo in items[:3]:
        results.append({
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "description": repo["description"]
        })

    return results
