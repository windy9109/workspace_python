# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import html
import os
import sys
import urllib.request
from xml.etree.ElementTree import Element, dump, ElementTree

from bs4 import BeautifulSoup

from day12.dao_emp import DaoBlog
import json


blog = DaoBlog()

client_id = "lXxuBhYwBxTxTZC7HvUh"
client_secret = "W0VjKuzIDI"
encText = urllib.parse.quote("대전오류동맛집")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
#url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText# xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    text = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)


#print(text)

jsonObject = json.loads(text)
print(jsonObject['items'])
for key in jsonObject['items']:
    title = key['title'].replace("'","")
    link = key['link'].replace("'","")
    description = key['description']
    bloggername = key['bloggername']
    bloggerlink = key['bloggerlink']
    postdate = key['postdate']
    
    cnt = blog.myinsert(title,link,description,bloggername,bloggerlink,postdate)
    print(cnt)


# soup = BeautifulSoup(text, "html.parser") 
# items = soup.select("item")
# for i in items:
#     title = i.select_one("title").text.replace("'","")
#     link = i.select_one("link").text
#     description = i.select_one("description").text
#     bloggername = i.select_one("bloggername").text
#     bloggerlink = i.select_one("bloggerlink").text
#     postdate = i.select_one("postdate").text
#
#
#     cnt = blog.myinsert(title,link,description,bloggername,bloggerlink,postdate)
#     print(cnt)
#


     
     
     
