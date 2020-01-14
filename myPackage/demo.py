import requests
def get_readme():
    url = "https://raw.githubusercontent.com/JohnLockwood/python-package-test/master/README.md"
    r = requests.get(url)
    return r.content

if __name__ == "__main__":
    print(get_readme())