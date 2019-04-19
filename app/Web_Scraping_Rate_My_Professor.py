import urllib.request
from bs4 import BeautifulSoup


def find_teachergrade(name):
    '''
    Scrapes the information of a given IU professor on ratemyprofessor.com
    :param name: A String of an IU Professor
    :return: A Dictionary of information about the professor
    '''

    space = name.split(" ")

    school = "Indiana University"
    ss = school.split(" ")

    webpage = "https://www.ratemyprofessors.com/search.jsp?query=" + \
              space[0] + "+" + \
              space[1] + "+" + \
              ss[0] + "+" + \
              ss[1]

    page = urllib.request.urlopen(webpage)
    soup = BeautifulSoup(page, 'html.parser')

    teacher_dict = {'Name': name}

    links = []
    for link in soup.find_all('a'):
        links.append(str(link.get('href')))

    # '/ShowRatings.jsp?tid=149625'

    for link in links:
        if link.startswith('/ShowRatings'):
            fr = link
    try:
        fw = "https://www.ratemyprofessors.com/" + fr
    except:
        teacher_dict['Found'] = False
        teacher_dict['Overall'] = "N/A"
        teacher_dict['Retake'] = "N/A"
        teacher_dict['Level of Difficulty'] = "N/A"
        return teacher_dict

    fb = urllib.request.urlopen(fw)

    stew = BeautifulSoup(fb, 'html.parser')

    grade = stew.findAll("div", {"class": "grade"})
    teacher_dict['Link'] = fw
    teacher_dict['Found'] = True
    try:
        teacher_dict['Overall'] = grade[0].text.strip()
        teacher_dict['Retake'] = grade[1].text.strip()
        teacher_dict['Level of Difficulty'] = grade[2].text.strip()
    except:
        teacher_dict['Found'] = False
        teacher_dict['Overall'] = "N/A"
        teacher_dict['Retake'] = "N/A"
        teacher_dict['Level of Difficulty'] = "N/A"
        return teacher_dict

    return teacher_dict
