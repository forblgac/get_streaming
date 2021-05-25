from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://wikiwiki.jp/774inc/%E9%85%8D%E4%BF%A1/2021-05-24'
site = 774

def get_stream(url: str, site: int):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    # selector = 'h3.date_weekday'
    selector = 'div#body'
    lis = soup.select(selector)[0].select('ul.list1 > li')
    count = 0
    stream_data = pd.DataFrame(index=['time', 'member', 'title', 'url'])
    for li in lis:
        time = li.text.split()[0]
        member = li.text.split()[1].split('：')[0]
        title = li.select('a')[0].text
        url = li.select('a')[0]['href']
        stream_data[count] = [time, member, title, url]
        count += 1
    return stream_data

print(get_stream(url, site).to_json('./774inc.json'))
