import requests
from bs4 import BeautifulSoup

input_url=input("Enter the url to be fetched: ")
response=requests.get(input_url)

soup=BeautifulSoup(response.text,'html.parser')
#print(type(soup))
#print(soup)
saver=input("Enter the file name to be saved")+".html"
formattedText=soup.prettify()
with open(saver,"w+") as s:
    s.write(formattedText)

print("Title of the page is:",soup.title.text)

no_a=soup.find_all('a')
print("The no of links available in the targetted page is:",len(no_a))

no_img=soup.find_all('img')
print("The no of links available in the targetted page is:",len(no_img))

