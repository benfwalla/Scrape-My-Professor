"""
Created on Thu Feb 21 12:22:18 2019
@author: michaelgaj
"""
import urllib.request
from bs4 import BeautifulSoup

teacher = input("Enter Teacher Name: ")
space = teacher.split(" ")
school = input("Enter School Name: ")
ss = school.split(" ")
webpage = "https://www.ratemyprofessors.com/search.jsp?query=" + space[0] + "+" + space[1] + "+" + ss[0] + "+" + ss[1]
page = urllib.request.urlopen(webpage)
soup = BeautifulSoup(page, 'html.parser')
links = []
for link in soup.find_all('a'):
    links.append(str(link.get('href')))
# '/ShowRatings.jsp?tid=149625'


for link in links:
    if (link.startswith('/ShowRatings')):
        fr = link

fw = "https://www.ratemyprofessors.com/" + fr
fb = urllib.request.urlopen(fw)
stew = BeautifulSoup(fb, 'html.parser')
grade = stew.findAll("div", {"class": "grade"})
overall = grade[0].text.strip()
retake = grade[1].text.strip()
lod = grade[2].text.strip()
scale = "out of 5"
print()
print()
print("{0:22} {1}".format("Professor Name:", teacher))
print("{0:22} {1}".format("School Name:", school))
print()
print("{0:22} {1} {2}".format("Overall Grade:", overall, scale))
print("{0:22} {1} {2}".format("Retake Grade:", retake, scale))
print("{0:22} {1} {2}".format("Level of Difficulty:", lod, scale))