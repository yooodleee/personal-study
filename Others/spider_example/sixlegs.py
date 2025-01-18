import pymysql.connections
import pymysql

conn=pymysql.connections(host='127.0.0.1', user='root', db='mysql', charset='utf8')
cur=conn.cursor()
cur.execute('UES wikipedia')

def getUrl(pageId):
    cur.execute('select url from pages where id=%s', (int(pageId)))
    return cur.fetchone()[0]

def getLinks(fromPageId):
    fromId=int(fromPageId)
    cur.execute('select toPageId from links where fromPageId=%s', (fromId))
    if cur.rowcount==0:
        return []
    return [x[0] for x in cur.fetchall()]

def searchBreadth(targetPageId, paths=[[1]]):
    newPaths=[]
    for path in paths:
        links=getLinks(path[-1])
        for link in links:
            if link==targetPageId:
                return path+[link]
            else:
                newPaths.append(path+[link])
    return searchBreadth(targetPageId, newPaths)