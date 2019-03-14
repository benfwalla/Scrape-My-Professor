from flask import render_template, request, flash, redirect, url_for
from app import app
from app.forms import CourseForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CourseForm()

    grades = [10, 20, 30]

    if request.method == 'POST':
        department = request.form['DepartmentInput']
        course_subject = request.form['CourseSubjectInput']
        catalog_number = request.form['CatalogNumberInput']
        class_number = request.form['ClassNumberInput']
        instructor = request.form['InstructorInput']

        flash("{}, {}, {}, {}, {}".format(department, course_subject, catalog_number, class_number, instructor))

        grades = [14, 33, 11]

        return redirect(url_for('index'))

    return render_template('index.html', form=form, grades=grades)

# TODO: Learn how to integrate AJAX into the form! https://www.youtube.com/watch?v=IZWtHsM3Y5A
