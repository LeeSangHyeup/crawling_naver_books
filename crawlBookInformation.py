# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import os

categoryNames = ['소설', '인문', '자기개발', '청소년', '해외']

bookNumber= 0
for eachCategory in categoryNames:
    if os.path.exists(eachCategory):continue
    categoryUrlFile = open(eachCategory+'.txt', 'r')
    os.makedirs(eachCategory)

    for bookInformationUrl in categoryUrlFile.readlines():
        targetWebPage = urllib.urlopen(bookInformationUrl.strip())
        soup = BeautifulSoup(targetWebPage.read(), 'lxml')
        
        try:
            bookName = soup.select('a[class^="N=a:bil.title"]')[0].next_element.string.encode('utf8')
            author = soup.select('a[class^="N=a:bil.author"]')[0].string.encode('utf8')
            publisher = soup.select('a[class^="N=a:bil.publisher"]')[0].string.encode('utf8')
            cost = soup.find('span', class_='won').previous_element.string.encode('utf8')
            bookIntroduce = soup.find('div', id='bookIntroContent').get_text().encode('utf8')
            authorIntroduce = soup.find('div', id='authorIntroContent').get_text().encode('utf8')
        except:
            continue
        testFile = open('./'+eachCategory+'/'+str(bookNumber)+'.txt', 'a')
        image = soup.find('img', onerror="emptyImg(this, 'm140')")['src']
        try:
            image = urllib2.urlopen(image)
        except:
            continue
	bookNumber += 1
	try:
	    file('./'+eachCategory+'/'+str(bookNumber)+'.jpg','wb').write(image.read())     
	except:
	    continue
	testFile.write(str(bookNumber)+'@'+bookName+'@'+author+'@'+publisher+'@'+cost+'@'+bookIntroduce+'@'+authorIntroduce)
