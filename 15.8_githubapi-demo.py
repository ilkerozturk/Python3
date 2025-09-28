import requests
import json

class GitHubAPI:
    BASE_URL = "https://api.github.com"
    Access_Token = ""  # Add your GitHub access token here if needed


def get_github_user_info(username):
    url = f"{GitHubAPI.BASE_URL}/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_info = response.json()
        
        info = f"GitHub Kullanıcısı: {user_info.get('login')}, Repository Sayısı: {user_info.get('public_repos')}, Takipçi Sayısı: {user_info.get('followers')}"
        
        return info
    else:
        return {"error": f"User {username} not found."}

def select_repository():
    username = input("Enter a GitHub username: ")
    url = f"{GitHubAPI.BASE_URL}/users/{username}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repos = response.json()
        if not repos:
            print(f"No repositories found for user {username}.")
            return
        
        print("\n",f"Repositories of {username}:")
        for idx, repo in enumerate(repos, start=1):
            print("\n",f"{idx}. {repo['name']}")
        
        choice = int(input("Select a repository by number: ")) - 1
        if 0 <= choice < len(repos):
            selected_repo = repos[choice]
            print("\n",f"Selected Repository: {selected_repo['name']}")
            print(f"Description: {selected_repo.get('description', 'No description')}")
            print(f"Stars: {selected_repo['stargazers_count']}")
            print(f"Forks: {selected_repo['forks_count']}")
            print(f"Language: {selected_repo.get('language', 'Not specified')}")
        else:
            print("Invalid selection.")
    else:
        print(f"Failed to fetch repositories for user {username}.")

def create_repository(repo_name, description="", private=False):
    url = f"{GitHubAPI.BASE_URL}/user/repos"

    headers = {
        "Authorization": f"token {GitHubAPI.Access_Token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "description": description,
        "private": private
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository '{repo_name}'.")

while True:
    print("\n", "1- Users Info\n", "2- Select Repository\n", "3- Create Repository\n", "5- Exit\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        username = input("Enter a GitHub username: ")
        user_info = get_github_user_info(username)
        print("\n",json.dumps(user_info, indent=4 , ensure_ascii=False))
    elif choice == "2":
        select_repository()
    elif choice == "3":
        repo_name = input("Enter the name of the new repository: ")
        description = input("Enter a description for the repository (optional): ")
        private = input("Should the repository be private? (yes/no): ").lower() == 'yes'
        create_repository(repo_name, description, private = private   )
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")