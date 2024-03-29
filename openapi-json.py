# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import json
from commonEnum import Cover,OutputType,QueryType,SearchTarget,Sort
from dotenv import load_dotenv
import os

def fetchFromAladin(apikey, query):
    params = {
        'ttbkey' : apikey, 
        'QueryType' : QueryType.Title.value, 
        'MaxResults':'2', 
        'start':'1', 
        'SearchTarget':SearchTarget.Book.value, 
        'output':OutputType.JSON.value, 
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
        jsonData = json.loads(response.read().decode('utf-8'))
        return jsonData
        

load_dotenv()
API_KEY = os.getenv('API_KEY')
output = fetchFromAladin(API_KEY, "역행자")
print(output)