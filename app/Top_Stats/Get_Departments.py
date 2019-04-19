from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup


def department(url):
    my_url = url
    uClient = ureq(my_url)

    # Open link, grab the page
    page_html = uClient.read()
    uClient.close()

    # html parse
    page_soup = soup(page_html, "html.parser")

    # grabs each class
    containers = page_soup.find("div", {"id": "crsebrowser"})

    a = []

    for string in page_soup.table.find_all("a", href=True):
        a.append(string.get_text())

    dict = {my_url: []}
    for i in a:
        dict[my_url].append(i)

    return (dict)


def department_depth(url, department):
    parse, later = url.split("index.shtml")
    attachment = "/index.shtml"

    end_result = {}

    for i in department.values():
        for k in i:
            compiled_link = parse + str(k) + attachment
            end_result.update({k: compiled_link})

    return (end_result)


def department_classes(url):
    my_url = url
    uClient = ureq(my_url)

    # Open link, grab the page
    page_html = uClient.read()
    uClient.close()

    # html parse
    page_soup = soup(page_html, "html.parser")

    # grabs each class
    containers = page_soup.find("div", {"id": "crsebrowser"})

    a = []

    for string in page_soup.table.find_all("a", href=True):
        a.append(string.get_text())

    return a


def get_all_courses(url):
    '''
    Returns all the course names for each department in a particular registrar link
    :param url: A String of a registrar link
    :return: A Dictionary of department codes to a list of corresponding courses
    (Ex: 'BUS': ['BUS-A 100', 'BUS-A 201', ...]
    '''
    final = {}

    for key, value in department_depth(url, department(url)).items():
        add = department_classes(value)
        final.update({key: add})

    return final


url = 'https://registrar.indiana.edu/browser/soc4198/index.shtml'

# print(value(url))
