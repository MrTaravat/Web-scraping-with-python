#exm1
import requests
from bs4 import BeautifulSoup
listurl=[]
url="http://www.tsetmc.com/Loader.aspx?ParTree=111C1417" #url
response=requests.get(url)      #response
soup = BeautifulSoup(response.content,"html.parser")
for a_href in soup.find_all("a", href=True):
    listurl.append('http://www.tsetmc.com/'+a_href["href"])
listurl=list(set(listurl))
print(listurl)