import requests
def readme():
    url = "https://raw.githubusercontent.com/JohnLockwood/python-package-test/master/README.md"
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    print(readme())