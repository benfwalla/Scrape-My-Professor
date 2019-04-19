import datetime


def get_term_url(date):
    '''
    Returns the url of the term closest to the input data
    :param date: A datetime object (usually datetime.today())
    :return: The Registrar url that points to the most recent completed semester relative to the date
    '''
    year = date.year
    month = date.strftime("%m")
    if datetime.datetime.now().year == year:
        sameyear = True
    else:
        sameyear = False

    if 3 <= int(month) <= 8:
        fall = True
    else:
        fall = False

    year_diff = year - 2004

    if fall:
        code = year_diff+4
        if code < 10:
            full_code = "40" + str(code)+"8"
        else:
            full_code="4" + str(code)+"8"

        if not sameyear and year > 2012:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc"+full_code+"/index.shtml"
        elif year < 2012:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc"+full_code+"/index.html"
        elif year == 2012:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc" + full_code + "/index.php"
        else:
            return "https://registrar.indiana.edu/browser/soc"+full_code+"/index.shtml"
    else:
        code = year_diff+4
        if code < 10:
            full_code = "40" + str(code) + "2"
        else:
            full_code = "4" + str(code) + "2"

        if not sameyear and year > 2013:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc" + full_code + "/index.shtml"
        elif year < 2013:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc" + full_code + "/index.html"
        elif year == 2013:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc" + full_code + "/index.php"
        else:
            return "https://registrar.indiana.edu/browser/soc" + full_code + "/index.shtml"


# # can take in either the current date or an older date
# current_date = datetime.datetime.now()
# old_date = datetime.datetime(2012, 4, 7)
#
# url = get_term_url(datetime.datetime.now())
# print(url)
#
# try:
#     web_page = urllib.request.urlopen(url)
#     contents = web_page.read().decode(errors="replace")
#     web_page.close()
# except:
#     print("URL Error")