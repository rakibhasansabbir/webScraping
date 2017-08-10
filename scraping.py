import urllib2
from bs4 import BeautifulSoup

root_address = "https://www.rottentomatoes.com/m/spider_man_homecoming/reviews/"
psge = urllib2.urlopen(root_address)
soup = BeautifulSoup(psge,'html.parser')

## print html content
# print soup.prettify()

critic_review = soup.find_all('div', attrs={'class':'the_review'})
for i in critic_review:
    print "Review :",
    print i.get_text(),"\n"