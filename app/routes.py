from flask import render_template, request, flash
from app import app
from app.forms import CourseForm
from app.Web_Scraping_Grade_Distribution import link, table_data


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CourseForm()

    grades = [10, 20, 30, 5]

    if request.method == 'POST':
        department = request.form['DepartmentInput']
        course_subject = request.form['CourseSubjectInput']
        catalog_number = request.form['CatalogNumberInput']
        class_number = request.form['ClassNumberInput']
        instructor = request.form['InstructorInput']

        gd_urls = link(department, course_subject, catalog_number, class_number)
        gd_dataframe = table_data(gd_urls)

        flash("Avg Grade Distribution: {}, {}, {}, {}".format(round(gd_dataframe['A%'].mean(), 2),
                                                              round(gd_dataframe['B%'].mean(), 2),
                                                              round(gd_dataframe['C%'].mean(), 2),
                                                              round(gd_dataframe['D%'].mean(), 2)))
        flash("Avg Class GPA: {}".format(gd_dataframe['CLS GPA'].mean()))
        flash("Instructors: {}".format(gd_dataframe['Instructor'].unique()))

        grades = [round(gd_dataframe['A%'].mean(), 2),
                  round(gd_dataframe['B%'].mean(), 2),
                  round(gd_dataframe['C%'].mean(), 2),
                  round(gd_dataframe['D%'].mean(), 2)]

        course = "{}-{} {}".format(department, course_subject, catalog_number)

        return render_template('index.html', form=form, grades=grades, course=course)

    return render_template('index.html', form=form, grades=grades)

# TODO: Learn how to integrate AJAX into the form! https://www.youtube.com/watch?v=IZWtHsM3Y5A
