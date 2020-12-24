# Extracting Data from XML
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the
# comment counts from the XML data, compute the sum of the numbers in the file.
#
# Data Format and Approach
# The data consists of a number of names and comment counts in XML as follows:
# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>
# You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code
# that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the
# data we are parsing in that sample code you will have to make real changes to the code.
# To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for
# any tag named 'count' with the following line of code: counts = tree.findall('.//count')
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1109155.xml (Sum ends with 62)

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
tree = ET.fromstring(html)
counts = tree.findall('.//count')
val = [int(count.text) for count in counts]
print(sum(val))