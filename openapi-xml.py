# -*- coding: utf-8 -*-
import sys
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from commonEnum import Cover,OutputType,QueryType,SearchTarget,Sort

def imageCoverter(img) : 
    return img.replace( "/cover/" , "/cover500/" , 1);

def checkbs4Item (obj, field):
     return obj.find(field).get_text() if obj.find(field) else None

def toOutput( obj) : 
    output = {
        'itemId': obj["itemId"] if "itemId" in obj.attrs else '' ,
        'isbn13': checkbs4Item(obj, 'isbn13') ,
        'cover_image': checkbs4Item(obj, 'cover'),
        'title' :checkbs4Item(obj, 'title'),
        'author':checkbs4Item(obj, 'author'), 
    }
    return output;

def fetchFromAladin(apikey, query):
    params = {
        'ttbkey' : apikey, 
        'QueryType' : QueryType.Title.value, 
        'MaxResults':'3', 
        'start':'1', 
        'SearchTarget':SearchTarget.Book.value, 
        'output':OutputType.XML.value, 
        'Query':query,
        'Sort':Sort.PublishTime.value,
        'inputencoding':'utf-8',
        'Cover': Cover.Big.value,
        'Version':'20131101'
    }
    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8') # 데이터를 바이트로 인코딩합니다.
    url = 'http://www.aladdin.co.kr/ttb/api/ItemSearch.aspx'
    # 요청을 보내고 응답을 받습니다.
    with urllib.request.urlopen(url + '?' + data.decode('utf-8')) as response:
        xmlData = response.read()

    soup = BeautifulSoup(xmlData, features='xml')
    outputArray = []
    for s in soup('item'):
        outputArray.append(toOutput(s));
    return outputArray
        

APIKEY= "ttbxivic0044001"
output = fetchFromAladin(APIKEY, "역행자")
print(output)
		# print (toString(s.title.contents[0]), '-' , toString(s.link.contents[0]))

# BeautifulSoup 객체를 생성합니다.
# soup = BeautifulStoneSoup(xmlData, 'lxml-xml')


# url = 'http://www.aladdin.co.kr/ttb/api/ItemSearch.aspx'
# con = urllib.urlopen(url +'?' + data)

# print (url , '?' , data);
# objectXml = con.read()
# con.close()

# soup = BeautifulStoneSoup(objectXml)
# soupString = str(soup)

# if soupString.find('<error xml') > -1:
# 	for s in soup('errormessage'):
# 		print "Error Message: " + toString(s.contents[0])
# else:
# 	for s in soup('item'):
# 		print toString(s.title.contents[0]), '-' , toString(s.link.contents[0])