import requests
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
import array as arr
import pandas as pd
import json



def get_data():
    req = requests.get(
        url="https://1plus1.ua/novyny",
        headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}
    #                 headers={'user-agent':f'{ua.random}'}
    )
    with open("dataSource/project.html", "w", encoding="utf-8") as file:
        file.write(req.text)

    with open("dataSource/project.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    articlesHashTagList = soup.select('.tips__item-date-hashTag a')
    articlesTimeStampList = soup.select('.smallData-regular')
    articlesTextList = soup.select('div.tips__item a h2')
    articlesUrlList = soup.select('div.tips__item div:nth-child(1) a')

    articleList = dict()
    for n in range(len(articlesHashTagList)):
        articleList.update(
            [{
                    "#": articlesHashTagList[n].text.strip(),
                    "timeStamp": articlesTimeStampList[n].text.strip(),
                    "article_Title": articlesTextList[n].text.strip(),
                    "url": articlesUrlList[n].get('href')
            }])

    with open("dataSource/result.json", "w", encoding="utf-8") as file:
        op = json.dumps(articleList)
        file.write(op)

#
def main():
    get_data()

if __name__=='__main__':
    main()
