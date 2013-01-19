from bs4 import BeautifulSoup
import urllib2
import re
import os

CACHEFILE = "cachefile"

if not os.path.isfile(CACHEFILE):
    req = urllib2.urlopen("http://www.seek.com.au/JobSearch?DateRange=31&"
                          "SearchFrom=quick&Keywords=&nation=3000&page=185")
    with open(CACHEFILE, 'w') as cache:
        cache.write(req.read())

with open(CACHEFILE, 'r') as cache:
    data = cache.read()

def strip_html(text):
    return re.sub('<[^<]+?>', '', text).strip()

soup = BeautifulSoup(data)
classmatcher = re.compile(".*mod-searchresult-entry.*")
jobsli = soup.findAll("li", attrs={'class': classmatcher})
job_datas = []
for job in jobsli:
    title = job.find("h2")
    sector = job.find(
        "div", attrs={'class': "state-fixedtobase"}).findAll("div")[0]
    location = job.findAll("dd")[0]
    date_posible = job.findAll("dd")
    print strip_html(title.text)
    for isdate in date_posible:
        for small in isdate.findAll("small"):
            print strip_html(small.text)
        for location in isdate.findAll('span'):
            print strip_html(location.text)
    job_data = dict(
        title=title.text.strip() if title else '',
        sector=sector.text.strip() if sector else '',
        location=location.text.strip() if location else '',
        #date=date.text.strip() if date else ''
    )
    job_datas.append(job_data)
    #print job_data

#print job_datas
