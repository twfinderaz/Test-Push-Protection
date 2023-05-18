from git import Repo

def commit_secret_to_repo(repo_path, file_path, commit_message):
    repo = Repo(repo_path)

    repo.git.add(file_path)
    repo.git.commit('-m', commit_message)

    try:
        repo.git.push()
        print("Push successful!")
    except Exception as e:
        print(f"Push failed: {e}")

# 請將以下的參數替換成你的實際情況
repo_path = "/home/xuser/Test-Push-Protection-main"
SECRET_KEY = "123456789abcdefg"
commit_message = "Test commit for secret scanning"

commit_secret_to_repo(repo_path, file_path, commit_message)
