from app.Web_Scraping_Grade_Distribution import make_course_name, table_data, link

# TODO: JeVante- figure out a way to find the average grade distribution for each professor in the DataFrame
urls = link('INFO', 'I', '201')
class_name = make_course_name('INFO', 'I', '201')
df = table_data(urls, class_name)

print(df)

