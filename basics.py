from bs4 import BeautifulSoup
import requests


with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#print(soup.prettify())

#print Title of the website
match = soup.title.text
#print(match)

#printing footer section
match = soup.find('div', class_='footer')
#print(match)

#find all the elements
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)



