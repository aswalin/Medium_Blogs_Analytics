from bs4 import BeautifulSoup
import requests

r  = requests.get("https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4")
data = r.text
soup = BeautifulSoup(data)

title = soup.title.text[0:-23]
claps = soup.find('button', class_="button button--chromeless u-baseColor--buttonNormal js-multirecommendCountButton").text
para = [hit.text.strip() for hit in soup.find_all('p')] # this contains linkedin id and description as well
tags = [hit.text.strip() for hit in soup.find_all('a', class_="link u-baseColor--link")]
bullets = [hit.text.strip() for hit in soup.select('li[class*="graf graf--li"]')]
images = soup.find_all('img', class_="graf-image")




