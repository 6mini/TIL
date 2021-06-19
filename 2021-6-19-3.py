'''
#pip install
#pypi
#pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
'''

# 파이썬에서 제공되는 내장함수, 외장함수가 있음.

import glob
print(glob.glob('*.py'))