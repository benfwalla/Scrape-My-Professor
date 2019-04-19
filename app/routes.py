from flask import render_template, request, flash
from app import app
from app.forms import CourseForm
from app.Web_Scraping_Grade_Distribution import link, make_class_name, table_data
from app.Web_Scraping_Rate_My_Professor import find_teachergrade


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CourseForm()

    grades = [10, 20, 30, 5]

    if request.method == 'POST':
        department = request.form['DepartmentInput']
        course_subject = str(request.form['CourseSubjectInput']).upper()
        catalog_number = request.form['CatalogNumberInput']

        gd_urls = link(department, course_subject, catalog_number, '')
        class_name = make_class_name(department, course_subject, catalog_number)
        gd_dataframe = table_data(gd_urls, class_name)

        avg_gpa = round(gd_dataframe['CLS GPA'].mean(), 2)

        flash("Avg Grade Distribution: {}, {}, {}, {}".format(round(gd_dataframe['A%'].mean(), 2),
                                                              round(gd_dataframe['B%'].mean(), 2),
                                                              round(gd_dataframe['C%'].mean(), 2),
                                                              round(gd_dataframe['D%'].mean(), 2)))
        flash("Avg Class GPA: {}".format(avg_gpa))

        grades = [round(gd_dataframe['A%'].mean(), 2),
                  round(gd_dataframe['B%'].mean(), 2),
                  round(gd_dataframe['C%'].mean(), 2),
                  round(gd_dataframe['D%'].mean(), 2)]

        course = "{}-{} {}".format(department, course_subject, catalog_number)

        list_of_teachers = gd_dataframe['Instructor'].unique()
        teacher_ratings = []
        for teacher in list_of_teachers:
            teacher_rating = find_teachergrade(teacher)
            teacher_ratings.append(teacher_rating)

        return render_template('index.html', form=form, grades=grades, course=course, teachers=teacher_ratings)

    return render_template('index.html', form=form, grades=grades)

# TODO: Learn how to integrate AJAX into the form! https://www.youtube.com/watch?v=IZWtHsM3Y5A
