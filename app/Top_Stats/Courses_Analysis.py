from app.Top_Stats.Get_Class_Schedule_URL import get_term_url
from app.Top_Stats.Get_Departments import get_all_courses
from app.Web_Scraping_Grade_Distribution import link, table_data
from datetime import datetime
import time
import pandas as pd
from tqdm import tqdm


def output_top_stats():
    '''
    Scrapes the IU Grade Distribution data of every class of the past semester, analyzes each class, and outputs
    the classes with the top results into a JSON Object
    :return: null. However, it does overwrite an existing JSON file
    '''
    url = get_term_url(datetime.today())
    print(url)

    courses_dict = get_all_courses(url)

    top_stats_df = pd.DataFrame([])

    for department in courses_dict:
        for course in tqdm(courses_dict[department], desc=department):
            if course != "[CROSSLISTED COURSES]":
                course_split = course.replace("-", " ").split()
                department = course_split[0]
                course_subject = course_split[1]
                catalog_number = course_split[2]

                url = link(department, course_subject, catalog_number)

                table_df = table_data(url, course)
                a_average = round(table_df['A%'].mean(), 2)
                b_average = round(table_df['B%'].mean(), 2)

                top_stats_df = top_stats_df.append(pd.DataFrame({'COURSE': course,
                                                                 'A%': a_average,
                                                                 'B%': b_average}, index=[0]),
                                                   ignore_index=True)

    return top_stats_df


print(output_top_stats())
