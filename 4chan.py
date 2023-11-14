# 4chan Board Files Downloader


import requests, bs4, sys, os

def getName(src):
    return src[src.rindex('/')+1:]


def FileDownload(url):
    name = getName(url)
    print(f"Downloading {name} {url}")
    req = requests.get(url)
    with open(name, "wb") as Vd:
        for chunk in req.iter_content(chunk_size=100000000):
            Vd.write(chunk)
def FileElems(url):
    req = requests.get(url)
    if req.status_code != 200:
        print("END")
        sys.exit()
    soup = bs4.BeautifulSoup( req.text, 'html.parser')
    ELEMS = ['https:'+k['href'] for k in soup.find_all('a',class_="fileThumb")]
    return ELEMS
os.system('cls')
Realurl = input("Enter Board URL : ")
url = Realurl
i = 1
while True:
    for src in FileElems(url):
        FileDownload(src)
    i+=1
    url = Realurl+str(i)
