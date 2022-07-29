#exm1
import requests
url="https://www.python.org" #url
response=requests.get(url)      #response
print(response.headers)    
#download the png file
url="https://avatars.githubusercontent.com/u/56771263?v=4"
response=requests.get(url) 
with open("avatar.png","wb") as f:
    f.write(response.content)