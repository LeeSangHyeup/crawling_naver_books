# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib
 
class BookCategory:
    name=''
    code=''
    def __init__(self, name, code):
        self.name = name
        self.code = code

humanitiesCode = '120'#인문
novelCode = '100'#소설
selfdevelopmentCode = '170'#자기개발
foreignCountryCode = '340'#해외
youthCode = '300'#청소년

bookCategoryList =[]
bookCategoryList.append(BookCategory('인문',humanitiesCode))
bookCategoryList.append(BookCategory('소설',novelCode))
bookCategoryList.append(BookCategory('자기개발',selfdevelopmentCode))
bookCategoryList.append(BookCategory('해외',foreignCountryCode))
bookCategoryList.append(BookCategory('청소년',youthCode)) 

detailBookCategoryCodes = ['010', '020', '030', '040', '050']

baseUrl = 'http://book.naver.com/category/index.nhn?cate_code='
basePageUrl = '&tab=top100&list_type=list&sort_type=publishday&page='

for bookCategory in bookCategoryList:
    urlTxtFile = open(bookCategory.name+'.txt', 'w')
    for detailBookCategoryCode in detailBookCategoryCodes:
        for pageNumber in range(10):
            targetUrl = baseUrl+bookCategory.code+detailBookCategoryCode+basePageUrl+str(pageNumber+1)

            targetWebPage = urllib.urlopen(targetUrl)
            soup = BeautifulSoup(targetWebPage.read())

            for eachATagLine in soup.find_all("a", class_="N=a:bta.thumb"):
                craweledUrl = eachATagLine['href']
                urlTxtFile.write(craweledUrl+'\n')
        
    
