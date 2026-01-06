##### FINAL - Part 1 #####
##### CSEC-380/480 - Kurt Wickboldt ####


'''
1) 10 Points: GitHub API. See PDF for Instructions.
'''
import requests
github_api_url = "https://api.github.com"
auth_token = ""
headers = {
    "Authorization": f"Bearer {auth_token}",
    "Accept": "application/vnd.github+json"
}

def list_repos(username):
    """Fetch repositories for a specific user"""
    url = f"{github_api_url}/users/{username}/repos"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            name = repo.get("name", "No name")
            desc = repo.get("description", "No description")
            print(f"Repo: {name}\nDescription: {desc}\n")
    else:
        print(f"Request failed with status code: {response.status_code}")

def create_issue(repo, title, body):
    """Create GitHub Issue for specific repo"""
    url = f"{github_api_url}/repos/{repo}/issues"
    data ={
        "title": title,
        "body": body
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        issue_url = response.json().get("html_url", "")
        print(f"Issue created: {issue_url}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.json())


def add_comment(repo, issue_number, comment):
    """Add a comment to an existing issue."""
    url = f"{github_api_url}/repos/{repo}/issues/{issue_number}/comments"
    data = {"body": comment}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        comment_url = response.json().get("html_url", "")
        print(f"Comment added: {comment_url}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.json())

list_repos("PRENGARA")
create_issue("PRENGARA/CSEC-380_Final", "issue name", "issue description") 
add_comment("PRENGARA/CSEC-380_Final", 1, "This is an issue comment")  # Issue number is whatever issue you want to add a comment to
