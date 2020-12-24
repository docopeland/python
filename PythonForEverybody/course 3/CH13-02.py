# Extracting Data from JSON
#
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the
# comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1109156.json (Sum ends with 37)

import urllib.request, urllib.error, urllib.parse
import json

#access the website
url = input("Enter URL: ")
data = urllib.request.urlopen(url).read().decode()
print("Retrieved",len(data),"characters")

#gets the JSON data in python form
js = json.loads(data)

#find all nums in ["comments"][iterable]["count"] and add them up
counts = [int(js["comments"][num]["count"]) for num in range(len(js["comments"]))]
print(sum(counts))