import requests

def readme():
    '''Print our own project's readme using requests library as a demo'''
    url = "https://raw.githubusercontent.com/JohnLockwood/ptestcs/master/README.md"
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    print(readme())