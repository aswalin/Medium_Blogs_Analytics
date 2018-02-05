from bs4 import BeautifulSoup
import requests
import ast
from datetime import datetime

r  = requests.get("https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4")
data = r.text
soup = BeautifulSoup(data)

title = soup.title.text[0:-23]
claps = soup.find('button', class_="button button--chromeless u-baseColor--buttonNormal js-multirecommendCountButton").text
para = [hit.text.strip() for hit in soup.find_all('p')] # this contains linkedin id and description as well
tags = ast.literal_eval(soup.find('script').text)["keywords"]
bullets = [hit.text.strip() for hit in soup.select('li[class*="graf graf--li"]')]
images = soup.find_all('img', class_="graf-image")
format = "%Y-%m-%d"
datePublished =  datetime.strptime(ast.literal_eval(soup.find('script').text)["datePublished"][0:10], format)
days_passed = (datetime.now() - datePublished).days





