import urllib.request
import datetime

# returns the url of the term closest to the input date
# input date should be in the format of month, year
def get_term_url(date):
    year = date.year
    month = date.strftime("%m")
    if datetime.datetime.now().year == year:
        sameyear = True
    else:
        sameyear = False

    if int(month) >= 3 and int(month) <= 8:
        fall = True
    else:
        fall = False

    yeardiff = year - 2004

    if fall:
        code = yeardiff+4
        if code < 10:
            fullcode = "40" + str(code)+"8"
        else:
            fullcode="4" + str(code)+"8"

        if not sameyear and year > 2012:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc"+fullcode+"/index.shtml"
        elif year < 2012:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc"+fullcode+"/index.html"
        elif year == 2012:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc" + fullcode + "/index.php"
        else:
            return "https://registrar.indiana.edu/browser/soc"+fullcode+"/index.shtml"
    else:
        code = yeardiff+4
        if code < 10:
            fullcode = "40" + str(code) + "2"
        else:
            fullcode = "4" + str(code) + "2"

        if not sameyear and year > 2013:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc" + fullcode + "/index.shtml"
        elif year < 2013:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc" + fullcode + "/index.html"
        elif year == 2013:
            return "http://wwwreg.indiana.edu/ScheduleOfClasses/prl/soc" + fullcode + "/index.php"
        else:
            return "https://registrar.indiana.edu/browser/soc" + fullcode + "/index.shtml"


# can take in either the current date or an older date
current_date = datetime.datetime.now()
old_date = datetime.datetime(2012, 4, 7)

url = get_term_url(datetime.datetime.now())
print(url)

try:
    web_page = urllib.request.urlopen(url)
    contents = web_page.read().decode(errors="replace")
    web_page.close()
except:
    print("URL Error")