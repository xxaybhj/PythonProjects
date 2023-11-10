import requests, bs4, os
def searchLastC(c,ch):
    pos = -1
    for i in range(len(ch)):
        if c == ch[i]:
            pos = i

    return pos
def DownloadImg(src,FolderName):
    if ("https" in src or "static" in src):
        return
    # find name of image
    imgName = src[searchLastC("/",src)+1:]
    print(imgName+" ...")

    # Download process
    
    Req = requests.get("https:"+src)
    pic = open(f"{FolderName}/{imgName}","wb")
    for chunk in Req.iter_content(1000000000):
        pic.write(chunk)
    pic.close()


url = input("URL ==> ")
urlReq = requests.get(url)

html = urlReq.text
soup = bs4.BeautifulSoup(html,"html.parser")

folder = input("Enter a folder name : ")
os.mkdir(folder)

picElems = soup.select('img')
for i in range(len(picElems)):
    DownloadImg(picElems[i].get('src'),folder)
    
