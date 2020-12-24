# Scraping Numbers from HTML using BeautifulSoup
# The program will use urllib to read the HTML from data files, and parse the data, extracting numbers and compute
# the sum of the numbers in the file.
#
# Data Format
# The file is a table of names and comment counts. You can ignore most of the data in the file except for lines with
# span. You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
#
# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1109153.html (Sum ends with 82)


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

# getting info from a url
url = input("Enter URL here: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

# find all the numbers in the span tag and add them
tags = soup('span')
vals = [re.findall('>([0-9]+)<',tag.decode()) for tag in tags]
nums = [int(num) for val in vals for num in val]
print(sum(nums))