import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url)  

html = response.content # html koduna çevirdi
soup = BeautifulSoup(html, "html.parser") # soup üzerinden istediğimiz etiketlere ve divlere ulaşabilicez 

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr") 
count = 1

for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find(class_ = "secondaryInfo").text.strip("()")
    rating = tr.find("td",{"class":"ratingColumn"}).text.strip("\n")
    print(f"{count}- Movie Name: {title.ljust(50)} Year: {year.ljust(15)} Rating: {rating}")
    count += 1


#print(list)