from app.Web_Scraping_Rate_My_Professor import find_teachergrade
from app.Web_Scraping_Grade_Distribution import make_class_name, table_data, link

urls = link('CSCI', 'C', '200', '')
class_name = make_class_name('CSCI', 'C', '200')
df = table_data(urls, class_name)

list_of_teachers = df['Instructor'].unique()

for teacher in list_of_teachers:
    print(find_teachergrade(teacher))
