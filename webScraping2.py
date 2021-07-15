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
    soup = BeautifulSoup(content, 'lxml')
    
    course_cards = soup.find_all('div', class_='card')
    
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        
        print(f'{course_name} costs {course_price}')