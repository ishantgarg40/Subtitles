import requests
from bs4 import BeautifulSoup as bs
import zipfile,io

n = input("Enter name of the movie in its correct form:-")
movie = list(n.split(' '))
movie = '+'.join(movie)

url = 'http://www.yifysubtitles.com/search?q='+str(movie)

resp = requests.get(url)

#if str(resp)=='<Response [200]>':
    
soup = bs(resp.text,"html.parser")

a_tags = soup.find_all('a')

for link in a_tags:
    if 'movie-imdb' in str(link.get('href')):
        x = link.get('href')
        break
    
url = 'http://www.yifysubtitles.com'+str(x)

resp1 = requests.get(url)

#if str(resp1)=='<Response [200]>':
        
soup = bs(resp1.text,"html.parser")

a_tags = soup.find_all('a')

for link in a_tags:
    if 'english' in str(link.get('href')):
                
        x = link.get('href')
        break
        
url = "http://www.yifysubtitles.com"+str(x)
        
resp2 = requests.get(url)

#        if str(resp2)=='<Response [200]>':
            
soup = bs(resp2.text,"html.parser")

a_tags = soup.find_all('a')

for link in a_tags:
    if 'zip' in str(link.get('href')):
                    
        x = link.get('href')
        break
url = str(x)

#print(url)

r = requests.get(url, stream=True)

z = zipfile.ZipFile(io.BytesIO(r.content))

z.extractall()



            
