# Following Links in Python
# The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat
# the process a number of times and report the last name you find.

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the
# last name that you retrieve. Sequence: Fikret Montgomery Mhairade Butchi Anayah; Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Conli.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the
# last name that you retrieve.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

# choose the beginner url, number of times to repeat the process, the position to use
url = input("Enter URL: ")
ranges = int(input("Enter count: "))
position = int(input("Enter position: "))

for i in range(ranges+1):
    print(url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    urls = [re.findall('href="(\S+)"', tag.decode()) for tag in tags]
    allLinks = [subSubUrls for subUrls in urls for subSubUrls in subUrls]
    url = allLinks[position-1]