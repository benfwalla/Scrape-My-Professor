""" Matthew Cummings
    Sophmore 2nd semester
"""
import urllib.request, re
from bs4 import BeautifulSoup
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def link(department, courseSub, catNum, clsnb):
    urls = []
    url = ("http://gradedistribution.registrar.indiana.edu/index.php?dept="+department.upper() +
           "&subject=" +
           courseSub.upper() +
           "&crse=" +
           catNum +
           "&clsnbr="
           +clsnb+"&instrname=&go=i")
    urls.append(url)
    if len(clsnb) == 0:
        url = ("http://gradedistribution.registrar.indiana.edu/index.php?&dept="+department.upper()+"&subject="+courseSub.upper()+"&crse="+catNum+"&c=desc&go=i&r=gradedist&page=2#result")
        urls.append(url)
    return urls


def table_data(urls):
    allData = []
    for url in urls:
        try:
            web_page = urllib.request.urlopen(url)
            contents = web_page.read().decode(errors="replace")
            web_page.close()
        except:
            pass
        table = re.findall('(?<=<table class="distribution">).+?(?=</table>)',contents,re.DOTALL)[0]
        soup = BeautifulSoup(table, 'html.parser')
        tempList = []
        for data in soup.find_all('td'):
            if data.text == 'Grade Distribution Not Available - Small Class Size':
                tempList = []
            elif data.text != '':
                tempList.append(data.text.strip())
            if len(tempList) == 12:
                allData.append(tempList)
                tempList = []

    df = pd.DataFrame(data=allData, columns=['#', 'TERM', 'DEPT', 'COURSE', 'CLS #',
                                             'Instructor', 'CLS GPA', 'STU GPA',
                                             'A%', 'B%', 'C%', 'D%'])

    df = df.set_index('#')
    df[['CLS GPA', 'STU GPA', 'A%', 'B%', 'C%', 'D%']] = df[['CLS GPA', 'STU GPA', 'A%', 'B%', 'C%', 'D%']].apply(pd.to_numeric)

    return df
#nothing this wass to get each teachers average gpa early dev 
##def averageGPA(datas):
##    teacherGPA ={}
##    division = {}
##    for data in datas:
##        if data[5] not in teacherGPA.keys():
##            teacherGPA[data[5]] = float(data[6])
##            division[data[5]] = 1
##        else:
##            gpa = teacherGPA.get(data[5])
##            newGpa = gpa + float(data[6])
##            teacherGPA[data[5]] = newGpa
##            old = division.get(data[5])
##            division[data[5]] = (old+1)
##    return teacherGPA, division
##    


#for mac import ssl and add context = ssl._create_unverified_context() and also inside of web_page add , context=context
# department = input("Deparment: ")
# courseSub = input("Course Subject: ")
# catNum = input("Catalog number: ")
# userInput = input("Is there a class number(yes or no)? ")
# if userInput.upper() == "YES":
#     clsnb = input("Class Number: ")
# else:
#     clsnb = ""
# website = link(department,courseSub,catNum,clsnb)
#
# result = table_data(website)
# size = len(result)
# print(result.head(size))
# print()
# print(result.describe())
# print(result['CLS GPA'].mean())

# BUS-S 433