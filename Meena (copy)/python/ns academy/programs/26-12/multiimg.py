import urllib2,os,time
startts=time.time()
urls=['https://www.tutorialspoint.com/python/images/python-mini.jpg','http://images.all-free-download.com/images/graphiclarge/beautiful_flowers_background_05_hd_picture_167019.jpg'
     ,'http://images.all-free-download.com/images/graphiclarge/flowers_in_full_bloom_hd_picture_166891.jpg']
#filepostfix=1
for url in urls:
    print 'loop entry'
    print url
    filepath=os.getcwd()+'/'+str(url.split('/')[-1:])
    #filepath=os.getcwd()+'/'+str(filepostfix)
    print filepath
    fp=urllib2.urlopen(url)
    fw=open(filepath,'wb')
    fw.write(fp.read())
    fp.close()
    fw.close()
    #filepostfix+=1

totaltime=time.time()-startts
print ((totaltime))
