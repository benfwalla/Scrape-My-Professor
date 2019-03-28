#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

# IN: Teacher Name
# Out: Dictionary Overall Grade, Retake, Level of Difficulty, Found
def find_teachergrade(name):
   # teacher = input("Enter Teacher Name: ")

    space = name.split(" ")

    school = "Indiana University"
    ss= school.split(" ")

    webpage = "https://www.ratemyprofessors.com/search.jsp?query=" + space[0] + "+" +space[1] + "+" + ss[0] + "+" + ss[1]

    page = urllib.request.urlopen(webpage)
    soup = BeautifulSoup(page, 'html.parser')


    dict = {'Overall': 0,'Retake': 0, 'Lod': 0, 'Found': 0}
    links=[]
    for link in soup.find_all('a'):
        links.append(str(link.get('href')))

    #'/ShowRatings.jsp?tid=149625'

    for link in links:
        if(link.startswith('/ShowRatings')):
            fr = link
    try:
        fw = "https://www.ratemyprofessors.com/" + fr
    except:
        dict['Overall'] = "N/A"
        dict['Retake'] = "N/A"
        dict['Lod'] = "N/A"
        dict['Found'] = "0"
        return dict

    fb = urllib.request.urlopen(fw)

    stew= BeautifulSoup(fb, 'html.parser')

    grade = stew.findAll("div", {"class": "grade"})
    dict['Overall'] = grade[0].text.strip()
    dict['Retake']= grade[1].text.strip()
    dict['Lod']= grade[2].text.strip()
    dict['Found'] = "1"
    return dict

def main():
    name = input("Enter Teacher Name: ")
    output = find_teachergrade(name)
    print(output)

if __name__== "__main__":
    main()