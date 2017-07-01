#!/usr/local/bin/python

import urllib
import shutil

#page = urllib.urlopen('https://www.jcq.org.uk/Download/examination-results/a-levels/2016/a-as-and-aea-results')

BaseUrl = 'https://www.jcq.org.uk/Download/examination-results/a-levels/{}/{}'
FileNameList = [
    ['a-as-and-aea-results','a-as-and-aea-results-summer-{}'],
    ['gce-trends-{}']
    ]

YearList = ['2001-2006']
for Year in range(2007,2017):
    YearList.append(str(Year))

for Year in YearList:
    for FileName in FileNameList:

        for FileNameVersion in FileName:

            FullUrl = BaseUrl.format(Year,FileNameVersion.format(Year))
            #print FullUrl

            InFile = urllib.urlopen(FullUrl)

            if InFile.getcode() == 200:
                OutFileName = FileNameVersion.format(Year) + '_' + Year + '.pdf'
                OutFile = open(OutFileName,'wb',0)

                shutil.copyfileobj(InFile, OutFile)

                OutFile.close()

        # print FullUrl
        # print OutFileName
