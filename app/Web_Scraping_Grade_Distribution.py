import urllib.request, re
from bs4 import BeautifulSoup
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def link():
    department = input("Deparment: ")
    courseSub = input("Course Subject: ")
    catNum = input("Catalog number: ")
    userInput = input("Is there a class number(yes or no)? ")
    if userInput.upper() == "YES":
        clsnb = input("Class Number: ")
    else:
        clsnb = ""
    url = ("http://gradedistribution.registrar.indiana.edu/index.php?dept="+department.upper()+"&subject="+courseSub.upper()+"&crse="+catNum+"&clsnbr="+clsnb+"&instrname=&go=i")
    return url


def tableData(url):
    web_page = urllib.request.urlopen(url)
    contents = web_page.read().decode(errors="replace")
    web_page.close()
    table = re.findall('(?<=<table class="distribution">).+?(?=</table>)',contents,re.DOTALL)[0]
    soup = BeautifulSoup(table, 'html.parser')
    print(soup)
    tempList = []
    allData = []
    for data in soup.find_all('td'):
        if data.text != '':
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


#for mac import ssl and add context = ssl._create_unverified_context() and also inside of web_page add , context=context
website = link()
print(website)

# result = pd.DataFrame
result = tableData(website)
print(result.head(20))

print()
print(result.describe())
print(result['CLS GPA'].mean())

