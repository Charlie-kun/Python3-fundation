# class 22
'''
from bs4 import BeautifulSoup

import requests

page=requests.get("http://www.naver.com")

soup=BeautifulSoup(page.content, 'html.parser')

title=soup.find('title')

links=soup.find_all(class_="link_partner")

print(title.get_text())

for link in links:
    print(link.get_text())
'''
#import nltk        #install nltk after 'pip install nltk'
#nltk.download()

from nltk.tokenize import sent_tokenize, word_tokenize

text = "Natural language processing (NLP) is a field" +\
    "of computer science, artificial intelligence" +\
    "and computational linguistics concerned with " +\
    "the interactions between computers and human " +\
    "(natural) languages, and, in particular, " +\
    "concerned with programming computers to " +\
    "fruitfully process large natural language " +\
    "corpora."

print(sent_tokenize(text))
print(word_tokenize(text))
