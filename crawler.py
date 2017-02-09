import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


#get soup from request.get response
def getSoup(url):
	fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
	return BeautifulSoup(requests.get(url, headers=fakeHeader).content, 'html.parser');

#get next page url
def nextPage(url):
	return url[:-1] + str(int(url[-1])+1)

#get article titles
def getArticleList():

	url = "http://www.zdnet.co.kr/news/news_list.asp?zdknum=0000&page=1"

	articleList = []
	yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
	stop = False

	print("crawling...")

	while True:
		for articleTag in getSoup(url).find_all("div", class_="article_li"):
			date = (articleTag.find(class_= "article_date").string[1:11]).replace(".","")
			
			if int(date) == int(yesterday):
				title = articleTag.h2.a.string
				link = "http://www.zdnet.co.kr" + articleTag.h2.a.get("href")
				articleList.append({'title':title, 'link':link})

			elif int(date) < int(yesterday):
				stop = True
				break
		if stop:
			break
		
		url = nextPage(url)

	print("done!\n")
	return articleList