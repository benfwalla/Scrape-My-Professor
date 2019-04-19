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

    teacher_dict = {}
    teacher_dict['Name'] = name

    links = []
    for link in soup.find_all('a'):
        links.append(str(link.get('href')))

    #'/ShowRatings.jsp?tid=149625'

    for link in links:
        if(link.startswith('/ShowRatings')):
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

def main():
    name = input("Enter Teacher Name: ")
    output = find_teachergrade(name)
    print(output)

if __name__== "__main__":
    main()