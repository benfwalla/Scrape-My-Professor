import urllib.request, re
from bs4 import BeautifulSoup
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def link(department, courseSub, catNum, clsnb):
    '''
    Creates the search query url to look up a class on the IU Grade Distribution site
    (http://gradedistribution.registrar.indiana.edu)
    :param department: A String of a course department (Ex: 'BUS')
    :param courseSub: A String of a course subject (Ex: 'K')
    :param catNum: A String of a course catalog number (Ex: '201')
    :param clsnb: A String of a specific class number (Ex: '10488')
    :return: A String of a url
    '''
    urls = []
    url = ("http://gradedistribution.registrar.indiana.edu/index.php?dept=" + department.upper() +
           "&subject=" + courseSub.upper() +
           "&crse=" + catNum +
           "&clsnbr=" + clsnb +
           "&instrname=&go=i")
    urls.append(url)
    if len(clsnb) == 0:
        url = ("http://gradedistribution.registrar.indiana.edu/index.php?&dept=" + department.upper() +
               "&subject=" + courseSub.upper() +
               "&crse=" + catNum +
               "&c=desc&go=i&r=gradedist&page=2#result")
        urls.append(url)

    return urls


def make_course_name(department, course_subject, catalog_number):
    '''
    Formats course name attributes into the proper format
    :param department: A String of a course department (Ex: 'BUS')
    :param course_subject: A String of a course subject (Ex: 'K')
    :param catalog_number: A String of a course catalog number (Ex: '201')
    :return: A String of a course name (Ex: 'BUS-K 201')
    '''
    return "{}-{} {}".format(department, course_subject, catalog_number)


def table_data(urls, class_name):
    '''
    Scrapes the results of a list of search query urls for IU's Grade Distribution Website into a pandas DataFrame
    :param urls: A List of search query urls
    :param class_name: A String of a course name
    :return: A pandas DataFrame of cleaned Grade Distribution results
    '''
    allData = []
    for url in urls:
        try:
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
                elif len(tempList) == 6:
                    if tempList[3] != class_name:
                        tempList = []
                    else:
                        content = str(data)
                        name = re.findall('(?<=title=").+?(?=")',content,re.DOTALL)[0]

                        # Turn given full name into a clear first name and last name
                        name = name.replace(',', ' ')
                        name = name.split()
                        name = name[1] + ' ' + name[0]

                        tempList[5] = name
        except:
            pass
        df = pd.DataFrame(data=allData, columns=['#', 'TERM', 'DEPT', 'COURSE', 'CLS #',
                                                 'Instructor', 'CLS GPA', 'STU GPA',
                                                 'A%', 'B%', 'C%', 'D%'])
    df = df.set_index('#')
    df[['CLS GPA', 'STU GPA', 'A%', 'B%', 'C%', 'D%']] = df[['CLS GPA', 'STU GPA', 'A%', 'B%', 'C%', 'D%']].apply(pd.to_numeric)

    return df
