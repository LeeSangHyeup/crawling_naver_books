# -*- coding:utf-8 -*-
import psycopg2
import os

dbConnectionString = "host='localhost' dbname='bookstore' user='postgres' password='00000NUL(null)'"
dbConnection = psycopg2.connect(dbConnectionString)
dbCursor = dbConnection.cursor()

dataForderNames = ['소설','인문','자기개발','청소년','해외']
ForderPath = '/home/lsh/crawlNaverBookInformationScript/'

baseInsertQuery = "insert into book(book_number, name, author,publisher,cost,introduce,authorIntroduce,category)values('BOOK_NUMBER', 'NAME', 'AUTHOR', 'PUBLISHER', COST, 'INTRODUCE', 'AUTHOR_INTRODUCE', 'CATEGORY')";

fileName=0
for eachCategory in dataForderNames:
    fileCount = (len(os.walk(ForderPath + eachCategory).next()[2]))/2
    
    for NEVER_USER in range(fileCount):
        fileName += 1

        namePath = ForderPath + eachCategory +'/'+str(fileName)
        
        try:
            txtFile = open(namePath+'.txt')
        except:
            continue
        content = txtFile.read().replace("'", "''")
        content = content.replace('&nbsp;', '')
        contentList = content.split('@')

        try:
	    bookNumber = contentList[0].strip()
            bookname = contentList[1].strip()
            author = contentList[2].strip()
            publisher = contentList[3].strip()
            cost = contentList[4].strip()
            introduce = contentList[5].strip()
            authorIntroduce = contentList[6].strip()
        except:
            continue

        query = baseInsertQuery.replace('NAME', bookname)
	query = query.replace('BOOK_NUMBER', bookNumber)
        query = query.replace('AUTHOR', author)
        query = query.replace('PUBLISHER', publisher)
        query = query.replace('COST', cost)
        query = query.replace('INTRODUCE', introduce)
        query = query.replace('AUTHOR_INTRODUCE', authorIntroduce)
	query = query.replace('CATEGORY', eachCategory)
        
        dbCursor.execute(query)
        dbConnection.commit()

