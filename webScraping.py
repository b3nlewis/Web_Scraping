# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 16:50:55 2021

@author: b3nle
"""

'''
Import Statements
'''

from bs4 import BeautifulSoup

'''
Step 1
'''
with open('home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)
    
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    
    courses_html_tags = soup.find_all('h5')
    #print(courses_html_tags)
    
    # prints out only the text in html
    for course in courses_html_tags:
        print(course.text)